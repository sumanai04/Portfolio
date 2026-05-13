# Portfolio — Fathi Al Adha Hylmi

Static portfolio site hosted on GitHub Pages. Projects section auto-updates from GitHub repos.

## How to add a new project

1. Go to [`projects_config.json`](projects_config.json) and click the pencil icon (Edit)
2. Add an entry at the bottom of the `"repos"` block:

```json
"repo-name-exactly-as-on-github": {
  "category": "ml",
  "display_name": "My Cool Project",
  "description": "What it does in one sentence.",
  "tech": ["Python", "PyTorch", "FastAPI"]
}
```

3. **Category** must be one of: `ml` (ML / DL), `sw` (Software Dev), `ds` (Data Science)
4. Commit directly to `main`
5. The GitHub Action rebuilds the site automatically (~30 seconds)

That's it — no cloning, no terminal. Do it from your phone if you want.

## How auto-update works

| Trigger | What happens |
|---------|-------------|
| You push to `projects_config.json` | Action runs instantly, rebuilds project cards |
| Daily at 07:13 UTC | Action fetches live repo data, refreshes descriptions |
| Manual via Actions tab | Click "Run workflow" anytime |

The Python script (`update_projects.py`) fetches repo metadata from the GitHub API and merges it with your curated config. Everything between `<!-- PROJECTS_START -->` and `<!-- PROJECTS_END -->` in `index.html` gets regenerated.

## Project structure

```
index.html              — Single-page portfolio
style.css               — All styles (glass-morphism dark theme)
projects_config.json    — Curated repo metadata (you edit this)
update_projects.py      — Rebuild script (stdlib only, no deps)
.github/workflows/      — GitHub Action for auto-updates
resources/              — Images, thumbnails, CV PDF
```

## Local development

```bash
python update_projects.py   # rebuild project cards manually
```

Then open `index.html` in a browser. No build step, no server needed.
