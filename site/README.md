# Octavebytes site, Phase 3 prototype

A static site built from the Phase 2 design (`../design/`). Plain HTML, one CSS file, one small JS file. The only tool needed is Python 3 (standard library only). Built and tested on Python 3.13.

```bash
python3 build.py --serve      # build and open http://localhost:4321
python3 tools/check.py        # quality gate: links, headings, titles, forms, JSON-LD, redirects
```

## What is in it

| | |
|---|---|
| **25 pages** | Home, 4 product pages, pricing (with a working cost estimator), start-trial form, 2 solutions pages, customers + 1 case study, docs / security / changelog / guides, 2 partner pages, about, contact, careers, government, 3 legal stubs, 404 |
| **Design** | Tokens and components from `design/03-design-direction.md`. Inter and JetBrains Mono self-hosted (87 KB), contrast-checked palette, one `<h1>` per page, keyboard-operable menus, visible focus, reduced-motion support |
| **SEO** | Titles and meta descriptions, canonical URLs, sitemap, robots, JSON-LD (`Organization`, `SoftwareApplication` with offers, `FAQPage` built from the visible FAQ text, `BreadcrumbList`) |
| **Conversion** | One trial CTA in the header and on every page; six forms that post to HubSpot; GA4 events in a `dataLayer`; HubSpot tracking and GA4 load only after consent |
| **Migration** | All 50 legacy URLs redirect (`deploy/redirects.csv`, generated `.htaccess` and nginx rules) |
| **Weight** | About 20 KB CSS, 11 KB JS, no images except the logo. Largest page about 25 KB HTML |

## Colour options

Four palettes are built in, all measured for accessibility (36 text and interface pairs each, all passing):

| | Name | Logo |
|---|---|---|
| **A** | Current blue (the live site's `#3762EC`) | Existing logo |
| **B** | Indigo and amber | Existing logo (still fits) |
| **C** | Teal | Recoloured logo (`logo-c.png`) |
| **D** | Graphite and orange | Recoloured logo (`logo-d.png`) |

- Switch live with the **Colour option** menu in the bar at the top of any page, or add `?theme=b`, `?theme=c`, `?theme=d`. Your choice is remembered in that browser.
- `/theme-preview/` shows all four side by side with the measured contrast tables. It is prototype-only and is never included in a launch build.
- To finalise: set `"theme": "c"` (or your pick) in `site.json`. A launch build then ships only that theme's logo and no switcher.
- `python3 tools/contrast.py` re-measures every pair from the real CSS; `tools/check.py` runs it too, so a colour change that breaks accessibility fails the build.
- The recoloured logos are previews made from the existing PNG. If you choose C or D, get a proper vector logo in that colour from a designer.

## Review mode and the launch gate

Every unconfirmed fact, price, proof point or asset is marked in the source as `[[CONFIRM: …]]`, `[[PROOF NEEDED: …]]`, `[[OWNER DECISION: …]]`, `[[ASSET NEEDED: …]]` or `[[DATA NEEDED: …]]`. While you review, they show as coloured chips and a bar at the top of each page lets you hide them ("Show review flags"). Add `?review=off` to any URL to see the clean version.

- `FLAGS.md` is the **punch list**: every open flag, by page. It is regenerated on every build.
- `python3 build.py --launch` **refuses to build while any flag is open**, so an unverified claim cannot go live by accident. When you resolve one, delete the marker (or replace it with the confirmed text) in `src/pages/…`.

## Editing

| To change | Edit |
|---|---|
| A page's copy | `src/pages/*.html` (front matter at the top sets URL, title, description) |
| Prices, phone, email, marketplace links | `site.json` → `vars`. Used everywhere as `{{var:core}}` and so on |
| Menu | `site.json` → `nav` |
| Header, footer, consent banner | `src/layout.html` |
| Repeated blocks (CTA band, price cards, product mock, diagram) | `src/partials/*.html` |
| Look and feel | `src/assets/css/site.css` (colour tokens at the top) |
| Redirects | the table in `../design/05-seo-and-migration-plan.md` (the build reads it) |

## Connecting the forms to HubSpot

Forms work now in **prototype mode**: on submit they show the thank-you state and the payload that *would* be sent. To go live:

1. In HubSpot, create six forms: `trial`, `estimate`, `aws`, `regulated`, `partner`, `contact`. (The site currently uses `trial`, `aws`, `partner` and `contact`; the estimate and regulated-sector routes reuse the trial and contact forms with an `intent` or `topic` value.)
2. Give each form these fields, using the **internal names** below. Hidden fields are filled by the site.

| Internal name | Where |
|---|---|
| `firstname`, `lastname`, `email`, `company` | all forms |
| `crm_used`, `connect_status`, `aws_region`, `agent_band`, `channels`, `plan_interest`, `message` | trial |
| `intent`, `source_page`, `referrer`, `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content` | hidden, all forms |
| `agent_count`, `timeline`, `ace_id` | AWS opportunity |
| `partner_type`, `aws_partner_tier`, `company_website` | partner |
| `topic` | contact |

3. Copy each form's GUID into `site.json` → `hubspot.formGuids`. The portal ID (`9426463`) is already set.
4. Submit a test request. In HubSpot, check the contact, and add a workflow that creates the deal (see `../design/04-conversion-plan.md` §3).

The consent checkbox is sent through HubSpot's `legalConsentOptions`, not as a field. Empty fields are omitted.

## Known limits of this prototype

- **Copy is a draft.** 130 flags are open; `FLAGS.md` lists them. Prices are proposals.
- **The hero visual is an illustration** with sample data, labelled as such. It must be replaced with a real screenshot.
- **Logo:** the existing PNG with the tagline removed. An SVG is needed.
- **Not written yet:** the six guides, the docs site, the changelog entries, the status page, real legal text, the team section, customer profiles.
- **Redirects and server configs were self-tested, not run on Apache or nginx.**
- **Not tested:** real browsers other than the built-in one; screen readers; Lighthouse or Core Web Vitals; real HubSpot submission.
