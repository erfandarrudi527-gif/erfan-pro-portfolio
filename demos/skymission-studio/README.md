# SkyMission Studio — Hero + How It Works

Plain HTML / CSS / JS. Rebuilt using **real data pulled directly from the
Figma file** via the Figma MCP connector (exact copy, colors, fonts, spacing) —
not guessed from the screenshot.

## Run it

Open `index.html` in a browser, or serve the folder:

```bash
npx serve .
```

## What's included

1. **Navbar** — logo mark + "SkyMission / STUDIO" wordmark, links (Blog,
   Services, Aerial, Portfolio, About Us — "About Us" active), outlined
   "Contact Us" button, burger menu on mobile, backdrop blur.
2. **Hero** — "Brisbane, Australia — CASA Certified" label, the
   "Visual Media for Construction Development Projects" headline, supporting
   paragraph, "Book a Mission" button, subtle vertical grid lines, and the
   exact navy gradient overlay over the background photo.
3. **How It Works** — "A Structured Approach / for Real Projects." heading,
   three numbered steps (1st/2nd/3rd) with glowing violet numerals, and a
   closing CTA bar ("Request Your Project Quote" + "Flexible scheduling •
   Reliable delivery").
4. **Services** (bento grid) — "Visual Solutions / Tailored for Construction
   & Development." heading, a 4-card bento layout (a large photo-backed
   featured card spanning two rows, two stacked text cards, and a wide card
   with a "Request This Service" glass button), plus a full-width photo
   panel with a bottom CTA bar. Includes the soft violet decorative glow
   in the corner from the original design. Typography (font sizes,
   line-heights, letter-spacing) now uses the exact px values from Figma
   at the desktop breakpoint rather than rounded rem approximations.
5. **Why Choose SkyMission Studio** — "Why Developers & Builders Choose
   SkyMission Studio." heading, and a 3×2 grid of six cards (icon, title,
   description) covering compliance, workflow, output quality, delivery
   speed, and communication — each with the same hover top-border glow as
   the other card grids, plus a matching decorative violet orb in the
   opposite corner.

## Design tokens (sampled straight from the Figma file)

| Token | Value |
|---|---|
| Background | `#040D2E` (Deep Cove) |
| Card background | `rgba(7,21,68,0.55)` |
| Card border | `rgba(143,74,216,0.18)` |
| Accent violet | `#8F4AD8` |
| Light violet (numerals/labels) | `#A96EE8` |
| Primary text | `#F4F2FF` |
| Secondary text | `rgba(244,242,255,0.65)` |
| Display/body font | Inter (300–900) |
| Label/mono font | Syne Mono |

## Notes

- The background photo and logo mark are stand-ins (the real image assets
  live on Figma's temporary CDN and expire after 7 days) — swap
  `.hero__bg-img` and `.navbar__logo` for your real files.
- **Important**: I can't preview or fetch images from `images.unsplash.com`
  in this sandbox (it isn't on my network allowlist), so I can't visually
  verify stock photo picks before using them. To avoid mismatched photos,
  every placeholder image on this page now points to the *same* single
  Unsplash photo, repeated across the hero, the Services featured card,
  and the showcase panel — so at least it's consistent until you swap in
  your real site photography.
- Everything else — copy, colors, type scale, spacing, and layout — was
  pulled directly from the Figma node tree, so it should match closely.
