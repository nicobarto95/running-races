# running-races

A small toolkit to extract, store and publish running race listings from HTML sources.

This repository contains a simple scraper that extracts race tables from HTML pages and saves the cleaned data into `data/` (JSON and CSV). It also includes a utility to inject a small Markdown table of races into the repository `README.md`.

**Quick overview**

- **Scraper:** `scripts/scraper.py` — parses HTML tables into a pandas DataFrame and writes `data/gare.json`, `data/gare.csv`, and `data/last_update.txt`.
- **README generator:** `scripts/generate_readme.py` — converts `data/gare.json` into a Markdown table and inserts it into the README (see instructions below).

## Why this is useful

- Collect and standardize public race listings from HTML pages.
- Produce lightweight JSON/CSV outputs for downstream consumption (websites, APIs, spreadsheets).
- Keep a small, human-friendly race table in this repository's README for quick visibility.

## Requirements

- Python 3.8 or newer
- The project uses `pandas` for HTML parsing and table handling. Install dependencies with pip.

## Get started

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install required packages (this project currently requires `pandas`; add more to `requirements.txt` if needed):

```bash
pip install pandas
# or, if you plan to use a requirements file later:
# pip install -r requirements.txt
```

3. Prepare the source HTML

- If you have a local HTML file with race tables, place it and set `SOURCE_PATH` in `scripts/scraper.py` to the filename (default in the script: `input_gare.html`).
- If you want to scrape a remote page, set `SOURCE_PATH` to the URL (uncomment the example in the script).

4. Run the scraper

```bash
python scripts/scraper.py
```

Outputs will be written to the `data/` directory:

- `data/gare.json` — JSON array of race objects (orient: records)
- `data/gare.csv` — CSV export useful for spreadsheets
- `data/last_update.txt` — timestamp of the last successful save

5. Generate the README table (optional)

`scripts/generate_readme.py` converts `data/gare.json` into a Markdown table and replaces a block in `README.md` between explicit start/end markers.

Before running the generator, make sure `scripts/generate_readme.py` has `START_TAG` and `END_TAG` set to the same markers present in this README. Example markers you can add to the README where you want the auto-generated table to appear:

```markdown
<!-- RACES START -->
<!-- RACES END -->
```

Then set `START_TAG = "<!-- RACES START -->"` and `END_TAG = "<!-- RACES END -->"` inside `scripts/generate_readme.py` and run:

```bash
python scripts/generate_readme.py
```

Note: the included `generate_readme.py` file currently uses `DATA_PATH = 'data/gare.json'` and will error if the markers are not present in the README. Update the marker constants in the script to match the markers you place in this README.

## Project layout

- `scripts/`
  - `scraper.py` — main scraping + cleaning script (uses `pandas.read_html`)
  - `generate_readme.py` — helper to build/insert a Markdown table from JSON data
- `data/` — output folder for `gare.json`, `gare.csv`, and `last_update.txt`

## Contributing

- Open an issue for feature requests or bugs: `https://github.com/nicobarto95/running-races/issues`
- Contributions are welcome — please follow the repository's `CONTRIBUTING.md` if present. If you don't have a `CONTRIBUTING.md` yet, open a pull request and describe the change.

Do not include large scraped datasets in pull requests; use sample HTML input or small fixture data for tests.

## Where to get help

- File issues at: `https://github.com/nicobarto95/running-races/issues`
- For discussion or questions, open an issue or reach out via your GitHub profile.

## Maintainers

- Repository owner: `nicobarto95` — see the GitHub repo for contact details and contributions.

## License

See the `LICENSE` file in the repository (if present) for license details.

## Notes & next steps

- Consider adding a `requirements.txt` with pinned versions (e.g., `pandas>=1.4`).
- Optionally set `START_TAG`/`END_TAG` in `scripts/generate_readme.py` and add the marker pair shown above to enable direct README updates.
- Add small sample input HTML to `tests/` or `data/samples/` to make development and CI reproducible.

---

<!-- Add auto-generated races between the markers below (if you enable `generate_readme.py`) -->

<!-- RACES START -->

**No automatic race table inserted.**

<!-- RACES END -->
# running-races