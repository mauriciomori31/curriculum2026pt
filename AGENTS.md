# AGENTS.md

## Project Overview

Personal curriculum/landing page for Braz Maurício Silva (Executivo em Tecnologia & IA). Static HTML site with PDF export capability.

## Key Files

| File | Purpose |
|------|---------|
| `index.html` | Main landing page (deployed to Vercel) |
| `landing/landing.html` | Backup version |
| `curriculum/curriculum.html` | Spanish version |
| `curriculum-braz-mauricio.pdf` | PDF export |
| `html_to_pdf.py` | PDF generator script |

## Developer Commands

```bash
# Generate PDF from HTML
python html_to_pdf.py

# Deploy to Vercel (automatic on push to main)
git push origin main
```

## Architecture

- Static HTML/CSS/JS site
- Uses Font Awesome icons and Google Fonts (Sora, JetBrains Mono)
- No build step required for HTML
- Vercel serves `index.html` as static site

## Important Notes

- PDF generation uses Playwright - run `python -m playwright install chromium` if not installed
- `vercel.json` configures rewrites for static hosting
- Keep `index.html` in root for Vercel deployment
- Landing page in pt-br, curriculum in es (Spanish)

## Adding New Content

1. Edit `index.html` 
2. Regenerate PDF: `python html_to_pdf.py`
3. Commit all: `git add . && git commit -m "description" && git push origin main`