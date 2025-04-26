# src/cli.py

import asyncio
import importlib
from src.config.settings import SCRAPERS

async def launch_scraper(scraper_name):
    scraper_path = SCRAPERS.get(scraper_name)
    if not scraper_path:
        raise ValueError(f"Scraper '{scraper_name}' not found.")

    module_name, class_name = scraper_path.rsplit(".", 1)
    module = importlib.import_module(module_name)
    scraper_class = getattr(module, class_name)

    scraper = scraper_class()
    await scraper.run()
