# Scraper Boilerplate (Playwright + Python)

⚡ A clean, scalable, and stealth-ready boilerplate for building Playwright-powered web scrapers fast and easily.

Built with:
- [Playwright](https://playwright.dev/)
- [Playwright-Stealth](https://github.com/AtuboDad/playwright-stealth)
- [uv](https://docs.astral.sh/uv/) for dependency management
- [python-dotenv](https://pypi.org/project/python-dotenv/) for environment variables
- [rich](https://rich.readthedocs.io/) for better logging
- Python 3.12+

---

## 🚀 Project Features

- ✅ Fast, reliable Playwright browser automation
- ✅ Stealth mode (enabled by default) to bypass bot detections
- ✅ Clean modular architecture (core/, scrapers/, config/)
- ✅ Easy to add new scrapers
- ✅ Proxy support (future-ready)
- ✅ Async and scalable
- ✅ dotenv support (load config from .env)
- ✅ Pre-commit hooks with Ruff for autoformat and auto-import sorting
- ✅ Rich colorful logging

---

## 📦 Installation

1. Clone the project:

```bash
git clone https://your-repo-url.git
cd scr-boilerplate-playwright
```

2. Create and activate a virtual environment:

```bash
uv venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
uv pip install -r pyproject.toml
```

4. Install Playwright browsers:

```bash
playwright install
```

5. (Optional) Install pre-commit hooks:

```bash
uv add pre-commit
pre-commit install
```

---

## 🧩 Project Structure

```
scr-boilerplate-playwright/
├── main.py              # Main entrypoint
├── src/
│   ├── cli.py           # CLI runner
│   ├── config/          # Settings
│   ├── core/            # Browser management, logger, scraper base
│   └── scrapers/        # Your individual scrapers
├── pyproject.toml       # Dependency manager (uv)
├── uv.lock              # Lock file
├── .env                 # Environment variables
├── README.md            # Project documentation
├── .pre-commit-config.yaml  # Pre-commit configuration (if set)
```

---

## 🏁 How to Run a Scraper

Run an available scraper by name:

```bash
python main.py <scraper_name>
```

Example:

```bash
python main.py example
```

---

## ⚙️ Options

By default, all scrapers:
- Run in **headless mode** (`headless=True`)
- Use **stealth mode** (`stealth=True`)
- Use **no proxy** (yet)

If needed, you can later control these options dynamically per scraper by editing `main.py` and `cli.py`.

Environment variables from `.env` are automatically loaded (e.g., PROXY_URL, HEADLESS).

---

## ✨ How to Add a New Scraper

1. Create a new file in `src/scrapers/`:

```bash
touch src/scrapers/my_new_scraper.py
```

2. Inherit from `ScraperBase`:

```python
from src.core.scraper_base import ScraperBase
from src.core.page_utils import safe_goto, extract_text

class MyNewScraper(ScraperBase):
    async def scrape(self, page):
        await safe_goto(page, "https://example.com")
        title = await extract_text(page, "h1")
        print(f"Page Title: {title}")
```

3. Register the new scraper in `src/config/settings.py`:

```python
SCRAPERS = {
    "example": "src.scrapers.example_scraper.ExampleScraper",
    "my_new": "src.scrapers.my_new_scraper.MyNewScraper",
}
```

4. Run it:

```bash
python main.py my_new
```

---

## 📋 TODO (Future Enhancements)

- Proxy rotation
- Smart retries on failed pages
- Parallel scraping (multiple tabs/pages)
- Dockerfile for easy containerization
- Exporting scraped data (CSV, JSON, SQLite)
- CLI argument parsing (headless, stealth, proxy flags)

---

## 🤝 License

This project is provided without warranty for personal or commercial use.
