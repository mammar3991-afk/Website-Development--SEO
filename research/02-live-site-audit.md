# Live site audit: octavebytes.com

Audited 21 September 2026. Method: Rank Math sitemaps, then every URL fetched and read as raw HTML and extracted text (50 content URLs plus 2 Elementor header/footer templates). Full list in [`data/url-inventory.csv`](data/url-inventory.csv).

**What I could not see.** No Google Search Console, GA4, backlink, rankings, Core Web Vitals or heatmap data. Everything about traffic, indexing and speed below is *structural evidence only*. Where I say "no H1" or "missing alt text", that is what the server sends in raw HTML; a page builder could patch some of it in with JavaScript.

## 1. URL inventory

| Sitemap | URLs | Notes |
|---|---|---|
| `page-sitemap.xml` | 37 | Home, about, contact, partner, careers, legal, 15 product pages, 8 service pages, case-study index, blog index, a Clutch reviews page |
| `post-sitemap.xml` | 14 | About 9 case studies, 5 blog posts. Latest post is 7 May 2026 (bank fraud robocall case study). Before that, nothing since September 2024 |
| `category-sitemap.xml` | 6 | Chatbots, CTI, cloud CC technologies, wallboard, case study, uncategorised |
| `elementor-hf-sitemap.xml` | 2 | Header/footer templates that should not be indexed at all |

Last-modified by year: 2023 → 1, 2024 → 23, 2025 → 20, 2026 → 6. About half the site has not been touched in 18+ months. The home page's footer still says © 2025.

## 2. What the site claims

**Positioning line (home, meta, about):** *"Octavebytes is innovating the customer experience. As an AWS Select Tier Services partner, Amazon Connect Service Delivery Partner & Amazon Connect Ready partner, we specialize in the design, delivery & migration of businesses to Amazon Connect."*

**Credentials asserted:** AWS Select Tier Services Partner, Amazon Connect Service Delivery Partner, Amazon Connect Ready Partner, "Available on HubSpot Marketplace", an AWS Marketplace link, and (on a page of its own) a SAM.gov registration with UEI and CAGE code.
- The emails confirm the AWS designations and the Marketplace listings are real.
- **The AWS Marketplace listing says "AWS FTR Certified". The site never uses the words "FTR" or "Foundational Technical Review".** The strongest technical credential OB holds for the connector is missing from the site.

**Product claims with no evidence on the page:** "Increase outbound call efficiency by up to 300%" (robocall page); "24/7 Octave Standard Support included" (repeated on many pages); "Flexible pricing" (no numbers, anywhere).

## 3. How the site is structured

**Navigation.** One "Menu" with three groups (Company, Products, Services) and about 30 links, repeated twice in the HTML. The same "Request a Demo" button sits under nearly every block. There is no search and no "Pricing", "Docs", "Customers" or "Resources" item.

**Homepage (319 words).** It opens with nav, then four cards: Agent Desktop, Amazon Connect, HubSpot CTI Connector, CTI Connectors. Then Amazon Lex bots, DevOps, Amazon Connect again, "Our Integrations", About. There is no headline that says what OB is for; no customer, number or quote anywhere. Meta description is a sentence fragment ("As AWS Select Tier Services partner , Amazon Connect Service Delivery Partner & Amazon Connect Ready Partner.").

**Products, 15 pages, four families mixed together:**
1. CTI connectors: HubSpot, MS Dynamics ("MSCRM"), GoHighLevel, SuiteCRM
2. Agent-side software: Octave Agent Desktop, Supervisor Case Management, MultiChat, Voice Recording
3. Reporting: Octave Vision wallboard, QuickSight page
4. Outbound and AI: Robocall for Banking, AWS SMS & Outbound Calling Campaign, Celesta AI voice agent, AI chatbot, Queue Selection (two near-duplicate pages)

**Services, 8 pages.** Amazon Connect (a generic explainer), Migration, Dynamic Caller ID, Amazon Connect automation, DevOps, WhatsApp Business API, "Hiredeveloper", QuickSight.

**Case studies (index + about 9).** Every one is anonymous: "Global Consumer Corporation", "a Leading Bank in Pakistan", "Australian customer". Almost all were published in mid-2024. Only one has appeared since. None carries a named customer, quote, photo or hard number (the fraud case study lists features and qualitative results).

**Partner page.** Headline "Working Together to Secure Your First Customer". It has no terms, no tiers, no commission or discount model, no list of what OB provides to a partner, and its contact block shows a different US phone number (+12 027 886467) from every other page (+1 855 681 4627).

**Contact page (82 words).** A form and addresses. The UK address that shows in the footer of every other page is blank here. Phone numbers appear in three different formats.

## 4. Technical and hygiene findings

| Finding | Evidence | Why it matters |
|---|---|---|
| **Comment spam has taken over three posts.** | The posts `whycti`, `chatgpt-cc` and the Australian energy case study together carry **11,543 injected comments** (4,795 / 3,119 / 3,629), advertising escort services, casinos, weighing scales and more, in Russian, Arabic and English. Each page's HTML is 3.3–5 MB. | Damages trust, adds 3–5 MB of HTML to each of these pages, and is a spam-content risk for search. It also shows that comments are open and unmoderated on the site. I have not reproduced any of it. |
| **Almost no H1 tags.** | 49 of 50 pages return zero `<h1>` tags in raw HTML. | Weak on-page signal, and screen readers get no page title. |
| **Images lack alt text.** | Most `<img>` tags on almost every page have no `alt`. | Accessibility and image-search loss. |
| **Duplicate pages.** | `/queueselection/` and `/queueselection-2/`; `/case-studies/` plus separate case-study posts and an older `/case-studies/amazonconnect-migration-project/`. | Splits ranking signals, confuses the reader. |
| **Empty stubs in the sitemap.** | `why-kpis-is-important-for-business` and `why-cloud-contact-center-is-important-for-businesses` are 14 words each. | Thin content. |
| **Bad titles / metas.** | Case-study titles run 97–114 characters (truncated in results); `/blog/`, `/case-studies/`, cookie policy have no meta description; meta descriptions on two posts are 38–46 characters. | Snippet quality. |
| **Cookie banner leaks template placeholders.** | The consent text shows "Manage {vendor_count} vendors" and "{title}". | Looks broken on first load, on every page. |
| **Forms deliver by email, not to HubSpot.** | Forms are Contact Form 7. No HubSpot form or tracking script found in raw HTML. One email subject template arrived unfilled: `octavebytes "[your-subject]"` (a 58-message thread has that subject). | Leads cannot be attributed; CRM shows almost every contact as "Offline". |
| **Header and footer templates are in the sitemap.** | `elementor-hf` URLs in `sitemap_index.xml`. | Should not be indexed. |
| **Inconsistent contact facts.** | Three US phone formats/numbers; UK address present or blank; partner page says "offices in Europe, Middle East and Asia" while other pages say "USA and Asia". | Undermines trust; makes local SEO signals unreliable. |
| **Platform.** | WordPress on Apache, PHP 8.4, Elementor, Rank Math, Contact Form 7, GA4 (`G-PQXZPMEVBF`). | Standard, but page-builder bloat plus 5 MB spam pages will hurt speed. |

## 5. What is missing

1. **A price**, though prices exist and are stable enough to publish.
2. **Named or numbered proof.** No logos, testimonials, metrics, review scores.
3. **A "how it works and what you need" page for the connector**, the product most buyers want. There are no docs, deployment guide, requirements, security page, changelog, or status information.
4. **A self-serve action.** There is no "Start trial", "Buy on AWS Marketplace" or "Buy on HubSpot Marketplace" button. The only CTA is "Request a Demo".
5. **A page for AWS staff.** Amazon's solutions architects and partner managers write to OB about 100 times in the data. They ask for cost estimates and SoWs. Nothing on the site is addressed to them.
6. **A real partner offer** with terms.
7. **Trust and compliance pages:** security, data handling, where the connector runs, uptime, support hours and process.
8. **Comparison / decision content:** OB vs Odea, native AWS/Salesforce adapters, or a HubSpot-native phone. Buyers do ask about alternatives.
9. **Current news/blog.** Nothing since a single May 2026 case study; 2025 has almost no content.

## 6. What feels dated

- Nav with about 30 items and the same CTA everywhere.
- "Innovating the customer experience" and other slogans that could describe any vendor.
- Template-style About copy ("Our Passion: Elevating the Customer Experience").
- AI positioning bolted on ("Celesta") with no proof and 23 images with no alt.
- Stock-style hero and icon cards.
- Anonymous case studies from 2024.
- © 2025.
- A Clutch page as a standalone URL.
- A government-procurement page presented as a top-level nav item, with **no US government deals visible in the CRM**.

## 7. Things worth keeping

- The **HubSpot connector page's feature list** is accurate, specific and matches the AWS Marketplace listing (call control, screen pop, click-to-dial, recording, transcription, wrap-up codes). It only needs a price, proof and a place to start.
- The **bank fraud robocall case study** is the most concrete and recent piece of proof on the site.
- The **Octave Vision** wallboard and **Agent Desktop** pages (each is a real product, but neither appears in the last 18 months of live deals).
- **Existing URLs with inbound value** (can't confirm without backlink data): `/hubspot-cti-connector/`, `/amazon-connect/`, `/mscrm-cti-connector-for-amazon-connect/`, `/gohighlevel-cti-connector/`, `/octave-vision/`, `/octave-agent-desktop/`.
