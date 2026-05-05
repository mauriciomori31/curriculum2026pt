import asyncio
from playwright.async_api import async_playwright
import os

async def html_to_pdf_white():
    html_path = os.path.abspath("index.html")
    pdf_path = os.path.abspath("curriculum-braz-mauricio-impressao.pdf")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1200, "height": 1600})
        
        await page.goto(f"file://{html_path}", wait_until="networkidle")
        
        # Inject CSS for white background print
        await page.evaluate('''() => {
            const style = document.createElement('style');
            style.textContent = `
                @media print {
                    * { color: #111 !important; }
                    body { background: #fff !important; }
                    body::before { display: none !important; }
                    nav { display: none !important; }
                    .glow-orb { display: none !important; }
                    .hero { background: #fff !important; min-height: auto !important; padding: 60px 0 30px !important; }
                    .hero-title .highlight { background: none !important; -webkit-text-fill-color: #111 !important; color: #111 !important; }
                    .hero-subtitle { color: #333 !important; }
                    .hero-description { color: #555 !important; }
                    .hero-badge { background: #f3f3f3 !important; border-color: #ddd !important; color: #333 !important; }
                    .stat-number { color: #111 !important; }
                    .stat-label { color: #666 !important; }
                    .hero-stats { border-color: #ddd !important; }
                    .hero-buttons { display: none !important; }
                    .pdf-contact-info { display: block !important; margin-top: 1rem; }
                    .pdf-contact-info p { color: #333 !important; font-size: 11px; }
                    .pdf-contact-info strong { color: #111 !important; }
                    
                    section { background: #fff !important; padding: 30px 0 !important; border-bottom: 1px solid #ddd; }
                    .section-title { color: #111 !important; font-size: 18pt; }
                    .section-label, .section-subtitle, .section-header p { display: none !important; }
                    
                    .about-card, .skill-item, .education-card, .language-card, .availability-card, .contact-card {
                        background: #f9f9f9 !important;
                        border: 1px solid #ddd !important;
                        color: #333;
                    }
                    .about-card-icon { background: #f3f3f3 !important; color: #111 !important; }
                    .about-card h3 { color: #111 !important; }
                    .about-card p { color: #555 !important; }
                    .skill-name { color: #111 !important; }
                    .skill-value { color: #111 !important; }
                    .skill-bar { background: #e0e0e0 !important; }
                    .skill-progress { background: #333 !important; }
                    
                    .timeline::before { background: #ddd !important; }
                    .timeline-dot { background: #fff !important; border-color: #333 !important; }
                    .timeline-item:last-child .timeline-dot { background: #333 !important; box-shadow: none; }
                    .timeline-title { color: #111 !important; }
                    .timeline-date { background: #f3f3f3 !important; color: #333 !important; }
                    .timeline-company { color: #555 !important; }
                    .timeline-tasks li { color: #555 !important; }
                    .timeline-tasks li::before { background: #333 !important; }
                    
                    .education-info h4 { color: #111 !important; }
                    .education-info p { color: #555 !important; }
                    .education-badge { border: 1px solid #ddd !important; }
                    .education-badge.completed { color: #111 !important; background: #f3f3f3 !important; }
                    .education-badge.incomplete { color: #555 !important; background: #f3f3f3 !important; }
                    .education-badge.current { color: #111 !important; background: #f3f3f3 !important; }
                    
                    .language-name { color: #111 !important; }
                    .language-level { color: #111 !important; }
                    
                    .availability-card { color: #333 !important; }
                    .availability-card i { color: #333 !important; }
                    
                    .contact-section { background: #fff !important; border: none; }
                    .contact-cards { display: flex !important; gap: 8px; }
                    .contact-card { 
                        background: #f9f9f9 !important; 
                        border: 1px solid #ddd !important; 
                        color: #333 !important;
                    }
                    .contact-card i { color: #333 !important; }
                    
                    footer { display: none !important; }
                }
            `;
            document.head.appendChild(style);
        }''')
        
        await page.pdf(
            path=pdf_path,
            format="A4",
            margin={"top": "12mm", "right": "12mm", "bottom": "12mm", "left": "12mm"},
            print_background=True,
            scale=0.8,
            prefer_css_page_size=True
        )
        
        await browser.close()
    
    print(f"PDF created: {pdf_path}")

asyncio.run(html_to_pdf_white())