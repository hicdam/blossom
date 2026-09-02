# Blossom Garden Design & Project Management

Complete launch package built 31 Aug 2026: competitive research, strategy, evolved brand identity and a working 17-page website for Surrey, Hampshire and Sussex.

## Folder map
- `site/` - the website. Static HTML, no frameworks. Open `index.html` or serve the folder.
- `site/_build/` - page generator. Edit content in `pages_a.py` / `pages_b.py` / `templates.py`, then run `python3 _build/build.py` from inside `site/`. `index.html` is standalone (edit directly).
- `research/` - competitor, pricing and SEO research with source URLs for every claim.
- `strategy/` - `strategy.md` (master strategy) and `launch-book.html` (published artifact).
- `brand/` - design system notes + original reference images (old logo, tree illustration, inspiration photo).

## Run locally
```
cd site && python3 -m http.server 8901
```
Then open http://localhost:8901/ (was left running and open in Chrome).

## Before launch (required inputs, marked in pink on the site)
1. Founder name, background, photo, qualifications, memberships (About page).
2. Phone, email, address, legal entity name (footer, contact, legal pages).
3. Domain: update `DOMAIN` in `site/_build/templates.py`, also in `index.html` head, rebuild.
4. Form endpoint: replace `REPLACE_WITH_FORM_ENDPOINT...` action in contact.html + welcome.html (or in `pages_b.py`/`build.py` and rebuild). Formspree or similar.
5. GA4 measurement ID: `GA_MEASUREMENT_ID` in `site/assets/js/main.js`.
6. Pricing sign-off: every figure on the site is a guide pending approval (see strategy.md).
7. Project photos + testimonials as they exist. Never invent.

## QR codes for print
Once the domain is live, generate one QR per publication:
```
URL: https://<domain>/welcome.html?utm_source=print&utm_medium=qr&utm_campaign=local-launch-2026&utm_content=<publication-slug>
```
Any QR generator works (or `pip install qrcode` then `qrcode "URL" > qr.png`). One URL per advert so each reports its own enquiries.

## Rules baked into everything
- No em dashes. British English. No invented credentials, testimonials, photos or history.
- All guide pricing labelled "as a guide, confirmed in writing".
- Placeholders are visibly marked "Required input", never fake-real.
