# src/core/scraper_base.py

from src.core.browser_manager import BrowserManager

class ScraperBase:
    def __init__(self, headless=True, proxy=None, stealth=True):
        self.headless = headless
        self.proxy = proxy
        self.stealth = stealth

    async def run(self):
        async with BrowserManager(headless=self.headless, proxy=self.proxy, stealth=self.stealth) as browser:
            manager = BrowserManager(headless=self.headless, proxy=self.proxy, stealth=self.stealth)
            async with manager as browser:
                page = await manager.new_page()
                await self.scrape(page)

    async def scrape(self, page):
        raise NotImplementedError("Scraper must implement scrape() method.")
