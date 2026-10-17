import json, os, re

# Issue body GitHub event se aata hai
with open(os.environ["GITHUB_EVENT_PATH"], encoding="utf-8") as f:
    body = json.load(f)["issue"].get("body") or ""

done = len(re.findall(r"^\s*[-*] \[[xX]\]", body, re.M))
todo = len(re.findall(r"^\s*[-*] \[ \]", body, re.M))
total = done + todo
pct = round(done * 100 / total) if total else 0

filled = round(pct / 10)
bar = "🟩" * filled + "⬜" * (10 - filled)
color = "red" if pct < 30 else "yellow" if pct < 70 else "brightgreen"

block = (
    "<!-- PROGRESS:START -->\n"
    f"![Progress](https://img.shields.io/badge/Progress-{pct}%25-{color}?style=for-the-badge) "
    f"![Tasks](https://img.shields.io/badge/Tasks-{done}%2F{total}-blue?style=for-the-badge)\n\n"
    f"**Overall:** `{bar}` **{pct}%** ({done}/{total} tasks done)\n"
    "<!-- PROGRESS:END -->"
)

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

new = re.sub(r"<!-- PROGRESS:START -->.*?<!-- PROGRESS:END -->", block, readme, flags=re.S)

if new != readme:
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new)
    print(f"Updated: {pct}% ({done}/{total})")
else:
    print("No change")
