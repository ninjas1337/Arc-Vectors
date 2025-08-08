# make_downloads_table.py
# Run from the repo root: python make_downloads_table.py
import pathlib, urllib.parse

paper = pathlib.Path("paper")
pdfs = sorted(paper.glob("**/*.pdf"))

print("## Downloads\n")
print("| Title | PDF |")
print("|---|---|")
for p in pdfs:
    rel = p.as_posix()
    title = p.stem.replace("-", " ").replace("_", " ").title()
    print(f"| {title} | [{rel}]({urllib.parse.quote(rel)}) |")
