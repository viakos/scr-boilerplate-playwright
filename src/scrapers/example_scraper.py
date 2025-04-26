from src.core.scraper_base import ScraperBase
from src.core.page_utils import safe_goto, extract_text

class ExampleScraper(ScraperBase):
    async def scrape(self, page):
        await safe_goto(page, "https://quotes.toscrape.com")
        title = await extract_text(page, "h1")
        print(f"Page Title: {title}")
