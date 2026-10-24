# Colrae

Public site for Colrae: <https://colrae-studio.github.io/>

The site is built with MkDocs. Paths under `/thronefold/` are used in the App Store listing and in the app, so leave them as they are.

`docs/stylesheets/extra.css` is original work for Colrae.

## Preview

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Open <http://127.0.0.1:8000/>.

## Add an app

1. Copy `docs/thronefold/` to `docs/<app>/`.
2. Rewrite the pages in that folder. Link to `/about/` for the studio. Don't copy the company description into the app folder.
3. Add a section for the app under `nav` in `mkdocs.yml`.
4. Add a card on `docs/index.md` that links to the new app's `index.md`.
5. Run `mkdocs build --strict`.

## Publish

Pull requests run `mkdocs build --strict`. A push to `main` deploys the site.

Before the first deploy, open the repository **Settings → Pages → Build and deployment** and set **Source** to **GitHub Actions**.
