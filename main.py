# src/main.py

import asyncio
import sys
import traceback
from src.cli import launch_scraper
from dotenv import load_dotenv
from src.core.logger import logger

load_dotenv()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python src/main.py <scraper_name>")
        sys.exit(1)

    scraper_name = sys.argv[1]

    try:
        logger.info("Scraper start")
        asyncio.run(launch_scraper(scraper_name))
        logger.info("Scraper end")
    except Exception as e:
        print(f"[ERROR] {e}")
        traceback.print_exc()
        logger.error("Something failed.")
