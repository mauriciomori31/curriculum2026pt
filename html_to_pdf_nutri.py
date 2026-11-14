import asyncio
from playwright.async_api import async_playwright
import os

async def html_to_pdf_nutri():
    html_path = os.path.abspath("nutri.html")
    pdf_path = os.path.abspath("curriculum-nutri-braz-mauricio.pdf")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1200, "height": 1600})
        
        await page.goto(f"file://{html_path}", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        
        # Generate PDF using native CSS print media defined in nutri.html
        await page.pdf(
            path=pdf_path,
            format="A4",
            margin={"top": "10mm", "right": "10mm", "bottom": "10mm", "left": "10mm"},
            print_background=True,
            scale=0.85,
            prefer_css_page_size=True
        )
        
        await browser.close()
    
    print(f"PDF created: {pdf_path}")

if __name__ == "__main__":
    asyncio.run(html_to_pdf_nutri())
