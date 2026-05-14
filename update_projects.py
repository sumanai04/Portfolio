#!/usr/bin/env python3
"""Fetch GitHub repos and regenerate project cards in index.html.

Uses only stdlib — no pip install needed. Reads projects_config.json for
curated metadata, fetches live repo data from the GitHub API, and replaces
everything between <!-- PROJECTS_START --> and <!-- PROJECTS_END -->.
"""

import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "index.html"
CONFIG = ROOT / "projects_config.json"

CATEGORY_LABELS = {
    "ml": "ML / DL",
    "sw": "Software Dev",
    "ds": "Data Science",
}


def fetch_repos(user: str) -> list[dict]:
    """Fetch all public repos for a GitHub user (no auth)."""
    url = f"https://api.github.com/users/{user}/repos?per_page=100&sort=updated"
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json",
                                                 "User-Agent": "portfolio-builder"})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def build_card(repo_name: str, owner: str, meta: dict, gh_data: dict | None) -> str:
    """Build a single project-card <a> element."""
    cat = meta["category"]
    display = meta.get("display_name", repo_name)
    desc = meta.get("description", "")
    tech = meta.get("tech", [])
    featured = meta.get("featured", False)
    thumbnail = meta.get("thumbnail", "")

    # Prefer config description; fall back to GitHub description
    if not desc and gh_data and gh_data.get("description"):
        desc = gh_data["description"]

    tech_html = "\n".join(
        f'          <span class="tech-pill">{t}</span>' for t in tech
    )

    card_class = "glass project-card featured" if featured else "glass project-card"

    thumbnail_html = ""
    if thumbnail:
        thumbnail_html = f"""        <div class="project-card-thumb">
          <img src="{thumbnail}" loading="lazy" alt="{display} screenshot"/>
        </div>
"""

    return f"""      <a class="{card_class}" data-cat="{cat}" href="https://github.com/{owner}/{repo_name}" target="_blank">
{thumbnail_html}        <div class="project-card-top">
          <span class="project-type {cat}">{CATEGORY_LABELS[cat]}</span>
        </div>
        <div class="project-title">{display}</div>
        <div class="project-desc">
          {desc}
        </div>
        <div class="project-tech">
{tech_html}
        </div>
        <div class="project-links">
          <span class="project-link">GitHub ↗</span>
        </div>
      </a>"""


def main() -> None:
    # 1. Load config
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    user = config["github_user"]
    repos_config = config["repos"]

    # 2. Fetch live GitHub data
    try:
        gh_repos = fetch_repos(user)
        gh_map = {r["name"].lower(): r for r in gh_repos}
    except Exception as exc:
        print(f"Warning: could not fetch GitHub repos ({exc}), using config data only")
        gh_map = {}

    # 3. Build cards (in config file order)
    cards: list[str] = []
    for repo_name, meta in repos_config.items():
        owner = meta.get("owner_override", user)
        gh_data = gh_map.get(repo_name.lower())
        cards.append(build_card(repo_name, owner, meta, gh_data))

    cards_block = "\n".join(cards)

    # 4. Inject into index.html
    html = INDEX.read_text(encoding="utf-8")

    pattern = r"(<!-- PROJECTS_START -->\n).*?(\n\s*<!-- PROJECTS_END -->)"
    if not re.search(pattern, html, re.DOTALL):
        print("Error: could not find PROJECTS_START / PROJECTS_END markers in index.html")
        return

    new_html = re.sub(
        pattern,
        rf"\1{cards_block}\2",
        html,
        count=1,
        flags=re.DOTALL,
    )

    INDEX.write_text(new_html, encoding="utf-8")
    print(f"Updated {INDEX} with {len(cards)} project cards.")


if __name__ == "__main__":
    main()
