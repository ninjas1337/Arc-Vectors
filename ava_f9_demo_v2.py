#!/usr/bin/env python3
# AVA Falcon 9 Entry — Upgraded Demo Generator
# Run: python ava_f9_demo_v2.py
import numpy as np, pandas as pd, matplotlib.pyplot as plt
from pathlib import Path

outdir = Path("./ava_f9_demo_v2_output")
outdir.mkdir(parents=True, exist_ok=True)

g0=9.80665; Re=6371e3; rho0=1.225; H=7200.0
def rho(h): return rho0*np.exp(-max(h,0.0)/H)
def a_sound(h):
    T = max(216.0, 288.15 - 0.0065*h)
    return (1.4*287.0*T)**0.5
def aero_coeffs(v,h):
    M = max(0.01, v/a_sound(h))
    if M<0.8: Cd=0.8
    elif M<1.2: Cd=1.0+0.5*(M-0.8)/0.4
    elif M<3.0: Cd=1.5-0.2*(M-1.2)/1.8
    else: Cd=1.3
    if M<0.8: L_over_D=0.3
    elif M<3.0: L_over_D=0.2
    else: L_over_D=0.15
    return Cd, L_over_D

m_entry=25000.0; A_ref=10.8; a_eff_land=22.0
h0=80e3; v0=2200.0; gamma0_deg=-20.0
x0=0.0; y0=h0; vx0=v0*np.cos(np.deg2rad(gamma0_deg)); vy0=v0*np.sin(np.deg2rad(gamma0_deg))
x_target_km=200.0; x_tol_km=15.0; h_end=1500.0
g_limit=6.0

def wind_field(h): # deterministic profile for repeatability
    if h>12000.0: base=-10.0
    elif h>3000.0: base=-15.0 + 5.0*(h-3000.0)/9000.0
    else: base=-20.0
    return base

def gravity(h): return g0*(Re/(Re+h))**2

def forces(vx,vy,h,bank_deg):
    v_air_x = vx - wind_field(h); v_air_y = vy
    v_air = (v_air_x**2+v_air_y**2)**0.5
    Cd,L_over_D = aero_coeffs(v_air,h)
    q = 0.5*rho(h)*v_air**2; D = q*Cd*A_ref
    if v_air<1e-3: tx,ty=1.0,0.0
    else: tx,ty=v_air_x/v_air, v_air_y/v_air
    nx,ny = -ty, tx
    L = L_over_D*D
    sigma=np.deg2rad(bank_deg)
    lx=np.cos(sigma)*nx + np.sin(sigma)*tx
    ly=np.cos(sigma)*ny + np.sin(sigma)*ty
    ax = (-D*tx + L*lx)/m_entry
    ay = (-D*ty + L*ly)/m_entry - gravity(h)
    return ax,ay,q,v_air

def landing_delta_v(v_end): return v_end + g0*v_end/22.0

def simulate(entry_impulse=None, bank_deg=0.0, dt=0.05):
    x,y=x0,y0; vx,vy=vx0,vy0; used_dv=0.0; peak_q=0.0; peak_g=0.0; burned=False
    hb=dm=da=None
    if entry_impulse:
        hb=entry_impulse["h_burn"]; dm=entry_impulse["dv_mag"]; da=np.deg2rad(entry_impulse["dv_angle_deg"])
    t=0.0
    while y>h_end and t<900.0:
        ax,ay,q,va = forces(vx,vy,y,bank_deg)
        a_tot=(ax**2+ay**2)**0.5; peak_q=max(peak_q,q); peak_g=max(peak_g, a_tot+gravity(y))
        if (not burned) and entry_impulse and (y<=hb) and vy<0.0:
            v=(vx**2+vy**2)**0.5; tx,ty=vx/v,vy/v; nx,ny=-ty,tx
            dvx=-dm*tx*np.cos(da)+dm*nx*np.sin(da); dvy=-dm*ty*np.cos(da)+dm*ny*np.sin(da)
            vx+=dvx; vy+=dvy; used_dv=(dvx**2+dvy**2)**0.5; burned=True
        vx+=ax*dt; vy+=ay*dt; x+=vx*dt; y+=vy*dt; t+=dt
        if y<0: break
    v_end=(vx**2+vy**2)**0.5
    dv_land=landing_delta_v(v_end); total=used_dv+dv_land
    return dict(total_dv=total, dv_entry=used_dv, dv_landing=dv_land, peak_q=peak_q, peak_q_kPa=peak_q/1000.0,
                peak_g=peak_g/g0, x_downrange_km=x/1000.0)

# Baseline bank sweep
banks=np.linspace(-20,20,81); base=[]
for b in banks:
    base.append({**simulate(None,b), "bank":b})
base_df=pd.DataFrame(base); base_df["x_err"]=abs(base_df["x_downrange_km"]-x_target_km)
baseline=base_df.sort_values("x_err").iloc[0]
baseline_q=float(baseline["peak_q"])

# Feasibility test wrapper
def feasible(res): 
    return (abs(res["x_downrange_km"]-x_target_km)<=x_tol_km) and (res["peak_q"]<=baseline_q) and (res["peak_g"]<=6.0)

# Search
rng=np.random.default_rng(5)
cand=[]
for _ in range(1200):
    hb=rng.uniform(40e3,70e3); dm=rng.uniform(0,220); da=rng.uniform(-10,10); b=rng.uniform(-20,20)
    r=simulate({"h_burn":hb,"dv_mag":dm,"dv_angle_deg":da}, b)
    if feasible(r):
        cand.append({"h_burn_km":hb/1000,"dv_mag":dm,"dv_angle_deg":da,"bank_deg":b,**r})
cand_df=pd.DataFrame(cand).sort_values("total_dv")
cand_df.to_csv(outdir/"candidates_stage1.csv", index=False)
best = cand_df.iloc[0] if not cand_df.empty else None

plt.figure(figsize=(8,6))
plt.scatter(base_df["total_dv"], base_df["peak_q"]/1000.0, s=8, alpha=0.4, label="Baseline bank sweep")
if not cand_df.empty:
    plt.scatter(cand_df["total_dv"], cand_df["peak_q_kPa"], s=10, alpha=0.7, label="AVA feasible")
plt.scatter([baseline["total_dv"]],[baseline["peak_q"]/1000.0], marker='x', s=140, label="Baseline best")
plt.title("Falcon 9 Entry — AVA-on-Top (Upgraded)")
plt.xlabel("Total Δv (m/s)"); plt.ylabel("Peak q (kPa)")
plt.legend(); plt.tight_layout(); plt.savefig(outdir/"pareto.png", dpi=160); plt.show()

print("Baseline:", dict(baseline))
if best is not None:
    print("Best feasible:", dict(best))
    print("Output folder:", outdir)
else:
    print("No feasible candidates found. Try increasing sample count.")
