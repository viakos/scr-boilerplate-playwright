# src/core/browser_manager.py

from playwright.async_api import async_playwright
from playwright_stealth import stealth_async

class BrowserManager:
    def __init__(self, headless=True, proxy=None, stealth=True):
        self.headless = headless
        self.proxy = proxy
        self.stealth = stealth
        self.playwright = None
        self.browser = None

    async def __aenter__(self):
        self.playwright = await async_playwright().start()
        args = ["--no-sandbox", "--disable-blink-features=AutomationControlled"]
        launch_options = {
            "headless": self.headless,
            "args": args,
        }
        if self.proxy:
            launch_options["proxy"] = {"server": self.proxy}

        self.browser = await self.playwright.chromium.launch(**launch_options)
        return self.browser

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.browser.close()
        await self.playwright.stop()

    async def new_page(self):
        """Create a new page, optionally with stealth."""
        context = await self.browser.new_context()
        page = await context.new_page()
        if self.stealth:
            await stealth_async(page)
        return page
