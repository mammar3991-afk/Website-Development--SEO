# Design direction

Every choice below has one reason tied to the audience or the evidence. The audience is **technical and cautious**: HubSpot admins, AWS architects, contact-centre leads and AWS account staff, reading pricing tables, requirement lists and docs. They are deciding whether a small vendor can be trusted with production calls.

## 1. Identity in one line

**Precise, calm and evidence-first: it should feel like good technical documentation with a friendly face, not a marketing brochure.**

*Why:* the current site's problem is that it says nothing specific. The fix is specificity, and the visual style should make specifics easy to scan and hard to fake.

## 2. Logo and brand mark

- **Keep the blue-cloud "OB" mark and the wordmark.** Continuity with the AWS Marketplace and HubSpot listings and the brand's existing recognition matter more than a fresh logo for a company this size.
- **Retire the "Innovating Customer Experience" tagline** under the wordmark (it is baked into the logo image). Replace with the wordmark alone; the site's tagline becomes *"Amazon Connect, inside your CRM."*
- **Ask the owner for the original vector logo.** The site has a 374 × 124 px PNG only. `[ASSET NEEDED: SVG]`

*Why:* the tagline is generic and could describe any vendor; the new one is specific.

## 3. Colour

| Token | Hex | Use | Contrast (measured) |
|---|---|---|---|
| **Ink** | `#0E1A33` | Headings, body text, dark bands | 17.3:1 on white |
| **Slate** | `#46526B` | Secondary text | 7.8:1 on white |
| **Brand blue** | `#3762EC` | Buttons, links, key accents (**the site's existing blue**) | 5.1:1 on white; white text on it 5.1:1 |
| **Brand dark** | `#2748C2` | Hover and pressed states | 7.5:1 with white text |
| **Tint** | `#EEF2FF` | Panels, highlighted table column | dark-blue text 6.7:1 on it |
| **Surface** | `#F6F7FA` | Page sections | |
| **Border** | `#DDE2EC` | Dividers, table lines | |
| **Included** | `#0B7A53` | "Included" ticks in pricing | 5.4:1 on white |
| **Dark band** | `#0E1A33` with white text, links `#9DB4FF` | One dark section per page for "how it deploys" | 17.3:1 and 8.6:1 |

*Why:* one accent colour keeps the eye on the primary action (trial). The blue is inherited from the brand, so nothing needs re-approving. **The old site's grey `#8C94B0` fails accessibility contrast at 3.0:1 on white; every colour above was checked at 4.5:1 or better.** Colour is never the only signal (ticks use a shape as well).

> **Update (Phase 3):** the palette above is **Option A**. Three alternatives (B indigo and amber, C teal, D graphite and orange) are built into the prototype so they can be compared live; see `../site/README.md` (Colour options). The choice is pending the owner's decision.

## 4. Typography

| Role | Family | Why |
|---|---|---|
| Headings and body | **Inter** (variable, self-hosted) | Very legible at small sizes in tables and forms, neutral and technical in tone, free to license, and one family means fewer downloads |
| Code, config, ARNs, API paths | **JetBrains Mono** (or system monospace) | The site will show real deployment steps and requirement lists; mono text signals "this is exact" |

- **Scale (desktop):** 56 / 40 / 28 / 20 / 17 (body) / 14 (caption). **Body 17 px, line-height 1.6, measure 60–72 characters.**
- Sentence case for headings. No all-caps except tiny labels.
- Replaces the current Rubik and Roboto (rounded and dated), with the added benefit of dropping a font family.

## 5. Layout principles

1. **One job per page, one primary action.** The header button is always "Start a 7-day trial" (not "free trial" until the owner confirms the trial is free). Each page ends with the same action.
2. **Answer the buyer's question in the first screen.** The hero states what it is, for whom and the price. No carousel, no video autoplay.
3. **Show the product, not stock people.** The hero visual is a **real screenshot of the connector inside HubSpot** (softphone panel plus contact record). `[ASSET NEEDED]`. The second visual is a **simple diagram of the deployment**: *Amazon Connect → Octave connector in your AWS account → HubSpot*. It makes "runs in your AWS account" concrete and reassures the AWS audience.
4. **Tables over cards for comparisons.** Price plans, "standard versus custom", and "you provide / we provide" are tables. Cards are used for navigation choices only.
5. **Generous whitespace, a 12-column grid, a maximum content width of 1160 px, and 68-character reading width for prose.**
6. **One dark section per page** for deployment or trust, to break rhythm without decoration.
7. **Proof close to the claim.** A badge or customer line sits beside the sentence it supports, not in a separate strip at the bottom.
8. **No hidden pricing, no hidden contact numbers.** Prices in the header row of the pricing table; one footer address block.
9. **Icons: one line-icon set (Lucide)** at 20–24 px, used only for scanning feature lists.
10. **Motion:** only for focus, hover, and accordion open/close (150–200 ms). Respect `prefers-reduced-motion`.

## 6. Components (build list for Phase 3)

Header with two-level nav · trust strip · hero (text + screenshot) · feature list with icons · numbered steps · price cards and comparison table · "you provide / we provide" split · architecture diagram · FAQ accordion (with schema) · proof card · case-study sidebar · form (short, with inline validation and clear errors) · docs callout · badge row · footer with a single address component · cookie banner · 404 page.

## 7. Content style

- **Plain second person, short sentences.** "You provide… We provide…"
- **Say what it costs, what it needs and what it does not do.**
- **Ban list:** *innovating, seamless, cutting-edge, next-generation, unlock, empower, robust, world-class, elevate.*
- **Jargon:** "CTI" and "CCP" appear once on product pages, defined; the rest of the site says "softphone in your CRM".
- Use **"Amazon Connect"** on pages and mention **"Amazon Connect Customer"** once on the services and AWS pages, since AWS renamed the product in April 2026.
- **Numbers show the unit and source.** "$15 per agent per month" not "from $15".

## 8. Accessibility and performance targets (to verify in Phase 3)

- **WCAG 2.2 AA:** contrast as measured above; visible focus rings; full keyboard navigation; form labels and error text; skip link; alt text on every image; one `<h1>` per page; no colour-only meaning.
- **Speed budget (targets, not yet measured):** LCP under 2.5 s on a mid-range phone; total JavaScript under 100 KB before interaction; every image sized and lazy-loaded; fonts self-hosted, subset, `font-display: swap`.
- **Cookie banner:** replace the broken one (it shows `{title}` and `{vendor_count}`). Only load analytics after consent where required.

## 9. Recommended build approach (for approval in Phase 3)

| Option | Fit | Trade-off |
|---|---|---|
| **A. Static site with content in plain HTML/Markdown, HubSpot forms embedded, deployed to your own server (a Contabo VPS with nginx, or GoDaddy Apache hosting)** | **Chosen and built (Phase 3).** Content is mostly static; nothing to hack (no comments, no plugins); fastest; deployable on either host you have | The marketing team needs an editing workflow (edit files and run one build command); one-time setup |
| **B. Stay on WordPress with a clean new theme** | Familiar to the team | Keeps the plugin, spam and page-builder weight that caused the current problems; needs ongoing hardening |
| **C. Full framework (Next.js) with a headless CMS** | Flexible | More engineering than a 30-page site needs |

Option A was approved and prototyped in Phase 3 (`../site/`). The deployment host is Contabo or GoDaddy (the owner's choice); deployment files for both are in `../site/deploy/`.

## 10. What is deliberately not in the design

- No stock photos of headset-wearing agents or handshake images.
- No auto-playing video, no sliders, no pop-ups on first load.
- No chat widget unless it is staffed (the old chat produced "missed chat" emails in 2023 and 2025).
- No "AI" imagery (glowing brains, robots). The AI story is shown with a real transcript-and-summary screenshot. `[ASSET NEEDED]`
