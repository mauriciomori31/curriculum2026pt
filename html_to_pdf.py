import asyncio
from playwright.async_api import async_playwright
import os

async def html_to_pdf():
    html_path = os.path.abspath("index.html")
    pdf_path = os.path.abspath("curriculum-braz-mauricio.pdf")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        await page.goto(f"file://{html_path}", wait_until="networkidle")
        
        # Generate PDF with specific settings
        await page.pdf(
            path=pdf_path,
            format="A4",
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            print_background=True,
            scale=1.0
        )
        
        await browser.close()
    
    print(f"PDF created: {pdf_path}")

asyncio.run(html_to_pdf())