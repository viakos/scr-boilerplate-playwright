import asyncio

async def smart_click(page, selector, timeout=10000):
    await page.wait_for_selector(selector, timeout=timeout)
    await page.click(selector)

async def extract_text(page, selector, timeout=10000):
    await page.wait_for_selector(selector, timeout=timeout)
    element = await page.query_selector(selector)
    return await element.text_content()

async def safe_goto(page, url, timeout=30000):
    try:
        await page.goto(url, timeout=timeout, wait_until="domcontentloaded")
    except Exception as e:
        print(f"[WARN] Failed to load {url}: {e}")
