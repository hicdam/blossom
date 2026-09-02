# Blossom Garden Design & Project Management: visual identity and design system

## Identity evolution

The original logo (bright green and candy pink tree, chunky serif) reads as clip art next to the
premium editorial website direction. The evolved identity keeps the leaning blossom tree silhouette
but redraws it as a stylised botanical illustration:

- Trunk and branches: deep bark charcoal (#3A2E29), drawn as tapered organic curves, roots visible
  (established, not floating).
- Blossom: five-petal flowers in three dusty pinks (#EDD3CE light, #D6A0A4 mid, #B0767D deep),
  with occasional plum leaves (#7C4E55). No lime green anywhere.
- A few loose falling petals give the mark movement without animation.
- Wordmark: Cormorant Garamond, "Blossom" large, with a letter-spaced small-caps strapline
  "GARDEN DESIGN & PROJECT MANAGEMENT" in Mulish.

The tree becomes a system, not just a logo: a single branch device that enters from the edge of
sections, a three-blossom hairline divider, a petal bullet, and a seasonal ring for year-round care.

## Colour tokens

| Token | Hex | Use |
|---|---|---|
| --parchment | #F6F1E7 | Page background (warm ivory, never stark white) |
| --parchment-deep | #EFE7D8 | Alternate band background |
| --yew | #22382B | Deep botanical green: headers, footer, buttons |
| --yew-deep | #16261D | Hover state, near-black panels |
| --ink | #2B2A26 | Body text charcoal |
| --ink-soft | #5C594F | Secondary text |
| --blossom | #D6A0A4 | Restrained pink accent (petals, small highlights) |
| --blossom-light | #EDD3CE | Tint backgrounds, petal highlights |
| --rosewood | #9C5F66 | Deep pink: links, active states, key accents |
| --moss | #8A9480 | Support green: planting palette, icons |
| --bark | #3A2E29 | Trunk/branch illustration colour |
| --hairline | rgba(34,56,43,.18) | Rules and borders |

Contrast: body ink on parchment 12.4:1. Yew on parchment 9.9:1. Rosewood on parchment 4.9:1
(used at 18px+ or bold). White on yew 11.7:1. All AA or better.

## Typography

- Display: Cormorant Garamond 500/600, italics for standfirsts and pull quotes. Never below 22px.
- Functional: Mulish 400/600/700 for navigation, body, forms, captions.
- Eyebrows: Mulish 700, 12px, letter-spacing .18em, uppercase, yew or rosewood.
- Scale (desktop): 64/44/32/24/19/17/15. Mobile: 40/32/26/21/17/16/14.
- Long-form body: 17px Mulish, 1.7 line height, max measure 68ch.

## Layout

- Max content width 1200px; text measure capped separately.
- Section rhythm: 112px desktop, 64px mobile.
- Editorial devices: small-caps eyebrow + serif headline + serif italic standfirst.
- Numbered markers used ONLY for the delivery process (a true sequence).
- Hairline rules in green ink; no heavy boxes; cards use 1px hairline + parchment-deep fill.

## Signature and art direction

No stock photography. Imagery is drawn from what a garden design practice actually produces:
1. The masterplan: a top-down hand-drawn-style garden plan (SVG) used as hero art.
2. The planting palette: swatch strips of foliage and flower tones with plant names.
3. The blossom identity system (tree, branch, petals, seasonal ring).
Real project photography slots exist throughout and are marked REQUIRED INPUT. Nothing invented.

## Motion

- Hero: 4-6 petals drifting slowly (CSS, 25s+ loops), disabled under prefers-reduced-motion.
- Scroll reveals: single gentle fade-and-rise, 500ms, once per element.
- Nothing else moves. Calm is the brand.

---

## REBRAND v2 (31 Aug, Damo's direction; supersedes the section above)

- Logo: ORIGINAL tree logo restored (brand/reference/logo-original.png). Header uses tree crop
  (site/assets/img/logo-tree.png) + "Blossom" wordmark in Fraunces Bold magenta; footer uses the
  full lockup (logo-full.png) on a cream panel. Logo background is #FFFBF2 and so is the site.
- Type: Fraunces Bold (700) for all headers (matches the logo font); Plus Jakarta Sans for body,
  nav, forms. Standfirsts in Fraunces italic.
- Palette: Option A "Garden Modern" (chosen from colourboard/): cream #FFFBF2, leaf green #2E4A33,
  bark ink #33261C, blossom magenta #CC428A (accents/links, deep #B23578), petal tint #F7E0EC,
  leaf lime #AFCE50 (micro-accents only). Options B (Courtyard) and C (Bold Bloom) documented on
  the colour board at localhost:8903.
- Imagery: modern block-photo layout using Damo's 12 supplied Unsplash photos
  (site/assets/img/photos/). Photos illustrate services and mood; they are NEVER presented as
  Blossom projects. Projects placeholders stay honest.
- Process presentation: How It Works restructured referencing newbarngardendesign.co.uk/service
  and rainegardendesign.co.uk conventions: stage-by-stage commitment, "You receive" deliverables
  per stage, APL/BALI contractor preference, staged payments, weekly notes.

---

## LOCKED v3 (31 Aug evening, Damo's final picks; supersedes above)

- LOGO LOCKED: Desktop "blossom logo lockup.png" (Blossom wordmark magenta + tree, no strapline),
  used exactly as supplied, no deviation. Assets: site/assets/img/logo-lockup.png,
  brand/reference/logo-lockup-LOCKED.png. Presented on its own cream (#FFFCF3) chip on dark grounds.
- PALETTE LOCKED (built colour-by-colour in Palette Builder):
  BG #FDFBF0 (Meadow Cream) · INK #2C3947 (Slate Ink) · BUTTONS/FOOTER #F3EBCF (Gorse Wash)
  · ACCENT/LINKS #22382B (Yew Green) · TINT #E4EAD8 (Sage Wash). No pink outside the logo.
- Locked from chooser: B5 underline+arrow CTA · H1 "A beautiful garden, properly delivered." ·
  T8 tight lux type (Fraunces 700 tight; small-caps kicker; PJS body 16/1.65).
- Structure: single scrolling page, parallax transitions, sections L2 → L4 → L6 → L8 → L10.
- Current state: WIREFRAME ONLY at colourboard/wireframe.html (localhost:8903/wireframe.html).
  Site at 8901 still wears the earlier Option A skin; do not roll the new system onto the site
  until Damo approves the wireframe.
- ROLLED OUT (31 Aug late): locked system applied to all 17 site pages (style.css v3),
  homepage rebuilt as the approved parallax scroll (L2 hero sunbeams, L4 offset, L6 pure type,
  L8 daisies CTA card, L10 checkerboard), overlay-to-solid sticky nav, gorse footer with locked
  lockup, CTA band on inner pages = L8 card over grass-light. All 12 supplied photos in use.
