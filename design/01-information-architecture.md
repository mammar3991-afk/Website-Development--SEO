# Information architecture

**Principle.** The current site has about 30 menu items and 50 URLs, built around what Octavebytes *makes*. The new site has **5 menu items and about 28 pages**, built around what each visitor is trying to *do*. Anything the evidence does not support as a sales path is cut from the main navigation and redirected.

## 1. Sitemap (launch)

```
/                                   Home
│
├── /products/
│   ├── /products/hubspot/                 Amazon Connect for HubSpot        (lead product)
│   ├── /products/dynamics-365/            Amazon Connect for Dynamics 365
│   ├── /products/other-crms/              GoHighLevel, SuiteCRM, Salesforce, others
│   └── /products/call-intelligence/       Transcripts and AI summaries in your CRM
│
├── /solutions/
│   ├── /solutions/banking-and-regulated-voice/   AI voice and outbound campaigns for banks and regulated sectors
│   └── /solutions/amazon-connect-services/       Setup, migration and custom builds on Amazon Connect
│
├── /pricing/                          Price card, what is included, what AWS costs, FAQ
├── /start-trial/                      Trial request form (also the "contact / demo" page)
│
├── /customers/                        Case-study index
│   └── /customers/[slug]/             Case study (template)
│
├── /resources/
│   ├── /resources/security/           Security and data handling
│   ├── /resources/changelog/          Release notes and HubSpot/AWS compatibility log
│   ├── /resources/guides/             Guides index
│   │   └── /resources/guides/[slug]/  6 launch guides (see §5)
│   ├── docs.octavebytes.com           Deployment guide, requirements, FAQ (separate docs site)
│   └── status.octavebytes.com         Uptime and incident history (separate status page)
│
├── /partners/
│   ├── /partners/                     Partner programme (resellers, integrators, delivery capacity)
│   └── /partners/aws/                 For AWS account teams: fact sheet and cost-estimate inputs
│
├── /company/
│   ├── /company/about/
│   ├── /company/careers/
│   ├── /company/contact/              Sales, support, offices
│   └── /company/government/           SAM.gov registration (footer only)
│
└── /legal/  privacy · cookies · terms
```

**Counts:** 30 pages at launch, including the two external sites (docs, status). The old site has 50 content URLs.

## 2. Navigation

### Header (5 items and one button)

| Item | Opens | Why it is here |
|---|---|---|
| **Products** | HubSpot · Dynamics 365 · Other CRMs · Call intelligence | Audience 1 finds their CRM in one click |
| **Solutions** | Banking & regulated voice · Amazon Connect services | Audience 4, and anyone who needs help beyond the connector |
| **Pricing** | (no submenu) | The most-asked question, and now answered |
| **Resources** | Docs · Security · Changelog · Status · Guides · Customers | Audiences 1 and 3 |
| **Partners** | For AWS teams · Become a partner | Audiences 2 and 5 |
| **[Start free trial]** | `/start-trial/` | The homepage's single job, on every page |

A thin utility bar above the header holds **Sign in / Support** (links to docs and support), the phone number and the language/region if needed later.

### Footer

Four columns: **Products** (4 links) · **Solutions** (2) · **Company** (About, Careers, Contact, Government procurement) · **Trust** (Security, Status, Changelog, Privacy, Cookies, Terms). Below: AWS partner badges (real ones, see proof plan), HubSpot Marketplace and AWS Marketplace links, one address block **(single source of truth for offices and phone numbers)**.

### Rules

- Maximum two levels; no mega-menu.
- No product appears in the menu unless there is a live customer or a live trial for it.
- The trial button is always visible; every product page also carries its own trial call-to-action.
- A page appears in the footer only if it exists for compliance or completeness.

## 3. How each audience finds a path

| Audience | Enters via | Path | Ends at |
|---|---|---|---|
| **1. Amazon Connect + CRM teams** | Search ("Amazon Connect HubSpot integration"), Marketplace listing, AWS referral, HubSpot Marketplace | Home or product page → Pricing → Docs (requirements) → Start trial | `/start-trial/` |
| **2. AWS account teams** | Direct link in an email | `/partners/aws/` (one page: credentials, cost-estimate inputs, SoW outline, how to register a co-sell) → forwards to customer with `/pricing/` | Email or opportunity registration |
| **3. Existing customers** | Support email, docs, bookmarks | Resources → Docs / Status / Changelog → Contact support | Support request |
| **4. Regulated-sector buyers** | Referral, RFP, search ("robocall banking Pakistan", "Urdu voice bot") | `/solutions/banking-and-regulated-voice/` → case study → contact | Contact form (not trial) |
| **5. Partners and integrators** | Cold outreach replies, AWS partner events | `/partners/` → Contact | Partner enquiry form |

**Two conversion endpoints, not five.** The trial form and the contact form. Both write to HubSpot (see conversion plan).

## 4. What was cut from the front of the site, and why

Grouped; the URL-by-URL mapping is in `05-seo-and-migration-plan.md`.

| Group | Current pages | Decision | Reason (evidence) |
|---|---|---|---|
| **Agent-side products** | Octave Agent Desktop, MultiChat, Voice Recording, Supervisor Case Management | **Remove from nav; fold a short "also available" line into Amazon Connect services** | Agent Desktop appears in one open $300 deal; Local Measure, a similar desktop, has been absorbed by Zendesk; NeuraFlash sells a desktop too. No trial or live-customer evidence in the 2026 emails |
| **Reporting** | Octave Vision wallboard, QuickSight page | **Move under Amazon Connect services** | Wallboard appears as a cross-sell in emails (a customer was pitched it in June 2026) and in a 2024 deal, not as a lead product |
| **Queue Selection, Dynamic Caller ID, Amazon Connect Automation (MCP)** | 4 pages | **Merge into Amazon Connect services** | Custom-build features, not products; two pages are near-duplicates |
| **Other CRM connectors** | GoHighLevel, SuiteCRM | **One "Other CRMs" page** | GoHighLevel has real deals (2024) and a distinct buyer; SuiteCRM has none visible. Neither justifies a menu slot |
| **Outbound / AI** | Robocall for Banking, AWS SMS & Outbound Calling, Autocall for E-commerce, Celesta AI Voice Agent, AI Chatbot | **Merge into one banking-and-regulated page** | One delivered bank project; one US customer; a Saudi RFP. Five separate pages dilute a story that is not yet a product line |
| **Services** | Amazon Connect explainer, Migration, WhatsApp Business API, DevOps, Hiredeveloper | **Merge: explainer and migration → Amazon Connect services; DevOps and hiring → Partners** | The explainer duplicates AWS's own pages. Dev staffing is a partner-channel offering (Saudi telecom integrator engagement) |
| **Government procurement** | 1 page | **Move to footer** | No US-government deals in the CRM |
| **Clutch** | 1 page | **Retire; fold into proof** | A profile page has no search or buying purpose |
| **Case-study posts** | 9 posts | **Keep the bank fraud case study; rewrite the best 2–3 in the new template; retire the rest** | Anonymous, undated content from 2024 with no metrics |
| **Blog** | 5 posts, 2 stubs, 3 spam-flooded | **Delete spam posts and stubs; replace with 6 guides** | See §5 |
| **Elementor header/footer templates** | 2 URLs in sitemap | **Remove from the sitemap** | Not content |

## 5. The six launch guides

Chosen because buyers ask these questions in email and because they match search phrasing (to be confirmed with Search Console).

| # | Guide | Audience | Evidence it is needed |
|---|---|---|---|
| 1 | *Amazon Connect and HubSpot: your integration options compared* (native softphone, third-party connectors, build-your-own) | 1 | Buyers ask about alternatives; competitors publish tiers |
| 2 | *How the connector is deployed in your AWS account* (CloudFormation walk-through, permissions, what HubSpot Super Admin needs) | 1, 3 | Customers ask about deployment and HubSpot access |
| 3 | *What does Amazon Connect + HubSpot cost?* (licence, AWS usage, telephony) | 1, 2 | 75 pricing threads; AWS staff ask for calculators |
| 4 | *Getting phone numbers and carriers right* (DIDs, SIP trunks, international dialling) | 1 | SIP/carrier questions recur in 35 threads |
| 5 | *Call transcripts and AI summaries in HubSpot: what is captured and where it goes* | 1, 3 | Transcription is the most requested add-on |
| 6 | *Fraud verification calls for banks: how an automated call flow works with a fraud system* | 4 | Delivered bank project; needs customer approval (see proof plan) |

## 6. URL conventions

- Lowercase, hyphenated, no dates in URLs, no trailing query strings.
- Product names in URLs are plain-language (`/products/hubspot/`), not internal code names.
- Every page has one `<h1>`, one primary CTA and one canonical URL.
- Old URLs redirect one-to-one wherever a matching page exists (see the migration plan).

## 7. Internal linking rules (so the structure carries the strategy)

- Every page that mentions price links to `/pricing/`.
- Every product page links to Docs (requirements), Security, and the trial form.
- The AWS page links to Pricing, Security and the deployment guide.
- Case studies link to the product page they relate to, and back.
- The homepage links to exactly four things above the fold: **Start trial**, **See pricing**, **HubSpot**, **Dynamics 365**.
