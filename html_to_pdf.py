import asyncio
from playwright.async_api import async_playwright
import os

async def html_to_pdf():
    html_path = os.path.abspath("index.html")
    pdf_path = os.path.abspath("curriculum-braz-mauricio.pdf")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1200, "height": 1600})
        
        await page.goto(f"file://{html_path}", wait_until="networkidle")
        
        # Inject CSS for clean PDF output - hide nav, show contact info
        await page.evaluate('''() => {
            const style = document.createElement('style');
            style.textContent = `
                @media print {
                    nav { display: none !important; }
                    body::before { display: none !important; }
                    .glow-orb { display: none !important; }
                    .hero { min-height: auto !important; padding-top: 80px !important; padding-bottom: 40px !important; }
                    .hero-stats { margin-bottom: 1.5rem !important; }
                    .hero-buttons { display: none !important; }
                    .pdf-contact-info { display: block !important; margin-top: 1rem; }
                    .pdf-contact-info p { margin: 0.25rem 0; font-size: 12px; color: #9898a8; }
                    .pdf-contact-info strong { color: #fb923c; }
                    section { page-break-inside: avoid; padding: 40px 0 !important; }
                    .section-header { margin-bottom: 30px !important; }
                    .section-title { font-size: 20pt !important; }
                    .section-label, .section-subtitle { display: none !important; }
                    .about-grid, .skills-grid, .education-grid, .languages-grid, .timeline { gap: 12px !important; }
                    .about-card, .skill-item, .education-card { padding: 16px !important; }
                    .about-card h3 { font-size: 14pt !important; margin-bottom: 8px !important; }
                    .about-card p { font-size: 11pt !important; }
                    .timeline-tasks li { font-size: 11pt !important; }
                    .skill-header { margin-bottom: 8px !important; }
                    .contact-section { display: none !important; }
                    footer { display: none !important; }
                }
            `;
            document.head.appendChild(style);
        }''')
        
        # Generate PDF
        await page.pdf(
            path=pdf_path,
            format="A4",
            margin={"top": "15mm", "right": "15mm", "bottom": "15mm", "left": "15mm"},
            print_background=True,
            scale=0.85,
            prefer_css_page_size=True
        )
        
        await browser.close()
    
    print(f"PDF created: {pdf_path}")

asyncio.run(html_to_pdf())