# SEO and migration plan

## 1. What I know and what I do not

**Known (from the live site):** 50 content URLs; almost no H1 tags; missing alt text; three posts buried in about 11,500 spam comments; duplicate pages; empty stubs; header/footer templates listed in the sitemap; a comment feed and author archive that are publicly reachable.
**Not known (no access):** which pages get organic traffic, which queries they rank for, which pages have backlinks, indexing status, Core Web Vitals. **Every "keep" and "redirect" decision below is provisional until Google Search Console, GA4 and a backlink export are checked** (Section 6, step 1).

## 2. Keep, redirect, restore, remove

| Decision | What |
|---|---|
| **Keep (rewrite in place, same job)** | HubSpot connector page, Dynamics 365 connector page, About, Contact, Careers, Privacy and Cookie policies, the bank fraud case study |
| **Keep (assets and identifiers)** | Domain, HTTPS, the GA4 property, the logo, the AWS partner badge already on the site, links to AWS and HubSpot Marketplace listings, the SAM.gov page (moved to footer) |
| **Redirect (301)** | 48 of the 50 current URLs, one-to-one to the closest new page (table in Section 5) |
| **Remove (410 Gone)** | Two 14-word stub posts (`why-kpis…`, `why-cloud-contact-center…`) |
| **Clean, then redirect** | The three spam-flooded posts: `whycti`, `chatgpt-cc` and the Australian energy case study. Delete the injected comments first, or redirect straight away. **If the backlink export shows toxic links to them, use 410 instead** |
| **Restore (bring back what is missing)** | (a) The **AWS FTR-certified** credential, on the site today nowhere. (b) A **pricing page**: prices exist today only in individual email quotes. (c) A **docs site**, a **changelog** and a **status page**. (d) Real **case studies with permission**. (e) **A page for AWS teams.** (f) Working **HubSpot-connected forms** |
| **Remove from the index or the server** | The two Elementor header/footer URLs in the sitemap; `/comments/feed/`; `/author/admin/` (exposes a username); the WordPress feeds; theme-demo remnants. About 52 archived demo URLs (for example `/case-categories/…` and `/metform-form/…`) from an old theme return 404 today and need no action |

**Historical URLs (Wayback Machine).** I found 134 archived HTML URLs; 52 are not in the current sitemap. They are template-demo remnants plus three old paths: `/octave-pay/`, `/cloud-call-center/` and `/building-bots/`. All return 404 now. I cannot tell whether they ever had traffic or backlinks, so **check them in the backlink export before deciding whether any deserve a redirect**. `/octave-pay/` may be a retired product.

## 3. Search themes (hypotheses to validate)

These come from the buyers' own words in email and from how competitors title their pages. **Confirm volumes and current rankings in Search Console and a keyword tool before finalising.**

| Theme | Example queries | Target page |
|---|---|---|
| Amazon Connect + HubSpot | "amazon connect hubspot integration", "hubspot amazon connect softphone", "hubspot cti connector amazon connect" | `/products/hubspot/` |
| Amazon Connect + Dynamics 365 | "amazon connect dynamics 365 integration", "cif 2.0 amazon connect" | `/products/dynamics-365/` |
| Amazon Connect + GoHighLevel | "amazon connect gohighlevel" | `/products/other-crms/` |
| Transcripts and AI summaries in CRM | "amazon connect call transcript hubspot", "contact lens hubspot" | `/products/call-intelligence/` |
| Cost and pricing questions | "amazon connect hubspot cost", "connector pricing per agent" | `/pricing/` and guide 3 |
| Options and comparison | "hubspot phone integration options", "hubspot calling alternatives amazon connect" | Guide 1 |
| Telephony questions | "amazon connect sip trunk", "amazon connect international dialing" | Guide 4 |
| Bank and regulated voice | "fraud verification ivr bank", "outbound dialer bank pakistan", "urdu voice bot" | `/solutions/banking-and-regulated-voice/` |
| Partner credibility | "amazon connect service delivery partner" | Home, services, About |

**Naming.** AWS renamed the product **Amazon Connect Customer** in April 2026. Use **"Amazon Connect"** as the main phrase; put "Amazon Connect Customer" once on the services, AWS-teams and pricing pages so both search phrasings are covered. Check both terms in Search Console.

## 4. On-page and technical rules

**Every page**
- One `<h1>` that contains the page's main phrase in plain words.
- Title tag under 60 characters; meta description 140–160 characters; both written by hand (drafts are in `content/`).
- One canonical URL; no duplicate pages (the old `/queueselection-2/` type).
- Every image has meaningful `alt` text (decorative images have empty alt).
- Descriptive link text ("See HubSpot pricing", not "Read more").
- Breadcrumbs with `BreadcrumbList` schema.

**Structured data**
- `SoftwareApplication` with `Offer` on product pages; `FAQPage` on product and pricing pages (only for questions actually on the page); `Organization` on Home and About; `Article` on guides and case studies.

**Technical**
- XML sitemap: only indexable pages; regenerate on publish; submit to Search Console. Remove the two Elementor URLs.
- `robots.txt`: allow all; disallow only admin or preview paths.
- HTTPS everywhere, HSTS, one canonical host (no `www` duplicate).
- Comments **off**, and no comment feed; disable author archives; no user enumeration.
- Speed targets from `03-design-direction.md` §8.
- No client-side redirects. Server-level 301s only.

## 5. Redirect map (all 50 current URLs)

Server-level, one hop, exact match with and without a trailing slash. Categories and feeds are listed after the table.

| Old URL | New URL | Code | Note |
|---|---|---|---|
| `/` | `/` | none | Home stays at the same URL; content is replaced |
| `/about/` | `/company/about/` | 301 | Rewrite |
| `/ai-chatbot-solution/` | `/amazon-connect/ai-and-bots/` | 301 | Direct successor: bots and voice AI page (Nov 2026 SEO check) |
| `/aivoiceagent/` | `/amazon-connect/ai-and-bots/` | 301 | Direct successor: bots and voice AI page (Nov 2026 SEO check) |
| `/amazon-connect-helps-e-commerce-company-toimprove-their-customer-service-experience/` | `/solutions/banking-and-regulated-voice/` | 301 | Anonymous; retire |
| `/amazon-connect-integration-with-salesforce-and-zoho-crm/` | `/products/other-crms/` | 301 | Anonymous; retire |
| `/amazon-connect-setup-and-back-office-integrations-foraustralian-customer-to-improve-customer-service/` | `/solutions/banking-and-regulated-voice/` | 301 | Anonymous 2024 case study; retire |
| `/amazon-connect-zendesk-and-salesforce-integration-for/` | `/products/other-crms/` | 301 | Matches the sibling Salesforce and Zoho page |
| `/amazon-connect/` | — | live | Now the Amazon Connect overview page (positioning change, Oct 2026); no redirect |
| `/amazon-connect-automation/` | `/solutions/amazon-connect-services/` | 301 | Found in Search Console (Oct 2026); custom-build capability |
| `/7slots-casino-en-guvenilir-casino-oyunlari/` | — | 410 | Injected casino spam page (Search Console, Oct 2026); gone |
| `/tag/ai/` | `/resources/guides/` | 301 | WordPress tag archive (GA4, Oct 2026) |
| `/tag/chatgpt/` | `/resources/guides/` | 301 | WordPress tag archive (GA4, Oct 2026) |
| `/tag/openai/` | `/resources/guides/` | 301 | WordPress tag archive (GA4, Oct 2026) |
| `/tag/hubspot/` | `/resources/guides/` | 301 | WordPress tag archive (GA4, Oct 2026) |
| `/tag/zendesk/` | `/resources/guides/` | 301 | WordPress tag archive (GA4, Oct 2026) |
| `/interac-casino-best-online-casinos-with-interac-banking-in-canada/` | — | 410 | Injected casino spam page (GA4, Oct 2026); gone |
| `/olimp-kazino-2026-kazahstan-stavki-na-sport-i-olimp-casino/` | — | 410 | Injected casino spam page (GA4, Oct 2026); gone |
| `/betify-casino-en-ligne-jouez-sur-betify-avec-1000-eu/` | — | 410 | Injected or junk page found live in the old-site crawl (Nov 2026 SEO check); gone |
| `/buitenlandse-online-casino-s-voor-spelers-uit-nederland-complete-ranking-en-vergelijking-van-populaire-casino-s/` | — | 410 | Injected or junk page found live in the old-site crawl (Nov 2026 SEO check); gone |
| `/jouer-au-plinko-en-ligne-jeu-de-casino/` | — | 410 | Injected or junk page found live in the old-site crawl (Nov 2026 SEO check); gone |
| `/pinko-kazino-oficialnyy-sayt-pinco-casino-vhod-na-zerkalo/` | — | 410 | Injected or junk page found live in the old-site crawl (Nov 2026 SEO check); gone |
| `/vavada-casino-online-einzahlungen-und-auszahlungen-im-online-casino/` | — | 410 | Injected or junk page found live in the old-site crawl (Nov 2026 SEO check); gone |
| `/coronavirus-disease-2019/` | — | 410 | Injected or junk page found live in the old-site crawl (Nov 2026 SEO check); gone |
| `/cw-check-https-test-com/` | — | 410 | Injected or junk page found live in the old-site crawl (Nov 2026 SEO check); gone |
| `/australian-energy-renewable-appliance-company-amazon-connect-with-hubspot-cti-connector/` | `/products/hubspot/` | 301 | Legit topic but page is spam-flooded. Clean before redirect; check backlinks |
| `/autocall-for-e-commerce/` | `/products/campaign-manager/` | 301 | Outbound campaigns now have a product page |
| `/automate-amazon-connect-aws-mcp-automator/` | `/solutions/amazon-connect-services/` | 301 | Custom-build capability. Revisit as a guide when AI-agent tooling matures |
| `/aws-sms-outbound-calling-campaign/` | `/products/campaign-manager/` | 301 | Outbound campaigns now have a product page |
| `/become-a-partner/` | `/partners/` | 301 | Rewrite with real terms |
| `/blog/` | `/resources/guides/` | 301 | Replace with guides |
| `/career/` | `/company/careers/` | 301 | Keep; 38 words today, needs real roles |
| `/case-studies/` | `/solutions/banking-and-regulated-voice/` | 301 | Rebuild in new template |
| `/case-studies/amazonconnect-migration-project/` | `/solutions/banking-and-regulated-voice/` | 301 | Older case study; retire or rewrite |
| `/case-study-ms-dynamics/` | `/products/dynamics-365/` | 301 | Fold into Dynamics page; rewrite as case study if permitted |
| `/chatgpt-cc/` | `/amazon-connect/ai-and-bots/` | 301 | AI in the contact centre; spam-flooded, check backlinks, 410 if toxic |
| `/clutch/` | `/company/about/` | 301 | Reviews page; belongs with company proof |
| `/contact-us/` | `/company/contact/` | 301 | Rewrite; fix form |
| `/cookie-policy-eu/` | `/legal/cookies/` | 301 | Keep and fix consent tool |
| `/crm-amazon-connect/` | `/resources/guides/` | 301 | Topic will be covered by guide 1; once published, point this at it |
| `/devops/` | `/partners/` | 301 | Delivery capacity for partners |
| `/dynamically-selecting-caller-id/` | `/solutions/amazon-connect-services/` | 301 | Feature, not a product |
| `/enhancing-call-center-operations-with-amazon/` | `/solutions/banking-and-regulated-voice/` | 301 | Anonymous 2024 case study; retire |
| `/enhancing-contact-center-reporting-with-aws/` | `/solutions/amazon-connect-services/` | 301 | Anonymous; retire |
| `/enhancing-fraud-prevention-with-automated-robo-calls-for-a-leading-bank-in-pakistan/` | `/solutions/banking-and-regulated-voice/` | 301 | Keep. Best proof piece; rewrite in template |
| `/gohighlevel-cti-connector/` | `/products/other-crms/` | 301 | Merge |
| `/government-procurement/` | `/company/government/` | 301 | Footer only |
| `/hiredeveloper/` | `/partners/` | 301 | Delivery capacity for partners |
| `/hubspot-cti-connector/` | `/products/hubspot/` | 301 | Keep and rewrite. Highest-value product page |
| `/migration-to-amazon-connect/` | `/amazon-connect/migration/` | 301 | Now has its own page |
| `/mscrm-cti-connector-for-amazon-connect/` | `/products/dynamics-365/` | 301 | Keep and rewrite |
| `/multichat/` | `/solutions/amazon-connect-services/` | 301 | Retire from nav |
| `/octave-agent-desktop/` | `/solutions/amazon-connect-services/` | 301 | Retire from nav; one line in services |
| `/octave-vision/` | `/solutions/amazon-connect-services/` | 301 | Wallboard becomes an add-on line |
| `/privacy-policy/` | `/legal/privacy/` | 301 | Keep and review |
| `/queueselection-2/` | `/solutions/amazon-connect-services/` | 301 | Duplicate of /queueselection/ |
| `/queueselection/` | `/solutions/amazon-connect-services/` | 301 | Feature, not a product |
| `/quicksight/` | `/solutions/amazon-connect-services/` | 301 | Reporting build |
| `/robocall-for-banking/` | `/solutions/banking-and-regulated-voice/` | 301 | Merge |
| `/scm/` | `/solutions/amazon-connect-services/` | 301 | Retire from nav |
| `/suitecrm/` | `/products/other-crms/` | 301 | Merge; no live customer seen |
| `/voice-recording/` | `/products/call-intelligence/` | 301 | Recording and transcripts are covered by call intelligence |
| `/whatsapp/` | `/solutions/amazon-connect-services/` | 301 | Channel build; Plus plan covers WhatsApp |
| `/why-cloud-contact-center-is-important-for-businesses/` | `/amazon-connect/` | 301 | 14-word stub, but 19 clicks and 17,822 impressions in Search Console; topic fits the overview |
| `/why-kpis-is-important-for-business/` | — | 410 | 14-word stub |
| `/whycti/` | `/resources/guides/hubspot-cti-screen-pop-explained/` | 301 | CTI guide now exists. Spam-flooded: clean comments first |

**Also redirect or remove**

| Old pattern | New | Code |
|---|---|---|
| `/category/case-study/` | `/solutions/banking-and-regulated-voice/` | 301 |
| `/category/chatbots/`, `/category/cti/`, `/category/cloud-cc-technologies/`, `/category/wallboard/`, `/category/uncategorized/` | `/resources/guides/` | 301 |
| `/elementor-hf/about/`, `/elementor-hf/footer-2/` | none | 410 and `noindex` |
| `/feed/`, `/comments/feed/`, `/author/admin/` | none | 410 or disabled |
| Any other unmatched old URL | `/` or a custom 404 with search and links to Products, Pricing, Trial | 404 (not blanket 301 to home) |

## 6. Migration procedure

### Before launch
1. **Baseline (essential):** connect Search Console and export the last 16 months of pages and queries; export GA4 top landing pages and events; export backlinks (Ahrefs, Semrush or similar) for the top 50 URLs. **Adjust Section 5 where a URL turns out to have traffic or links.**
2. **Crawl the old site** (Screaming Frog or similar) and save the URL, title, H1 and status list.
3. **Clean the spam:** delete injected comments, close comments, submit removal requests in Search Console for any indexed spam URLs.
4. **Build the redirect file** from Section 5 and test every line against a staging copy.
5. **Prepare the new pages** with titles, metas, schema and canonicals from `content/`.
6. **Install tracking** (HubSpot script, GA4 events) on staging and test that a trial request creates a HubSpot deal.
7. **Have docs, changelog and status live** so the new nav does not link to empty pages.
8. **Freeze changes** to the old site 48 hours before launch.

### Launch day
1. Deploy new site and redirects together. Do not ship one without the other.
2. Test the top 30 old URLs by hand; crawl all 50; confirm one hop, correct code.
3. Submit the new XML sitemap in Search Console.
4. Confirm forms, tracking and marketplace links.
5. Keep the old site available (read-only) on a private URL for 30 days for comparison.

### After launch
| When | Check |
|---|---|
| Day 1–3 | 404 report, crawl errors, form deliveries, redirect chains |
| Week 1 | Indexing of new URLs; impressions and clicks compared to baseline |
| Weeks 2–4 | Ranking movement for the theme table; fix any 404 with traffic |
| Day 30 | Retire the private old-site copy; review anonymised, permission-cleared proof |
| Month 3 | Compare organic clicks, trial requests and lead sources to baseline |
| Ongoing | Keep the redirects **for at least 12 months** |

## 7. Content and link-building plan (small and realistic)

- **Six guides** at launch (`01-information-architecture.md` §5), each written for a question buyers actually ask. One new guide a month afterwards, driven by Search Console queries and support emails.
- **Marketplace and partner listings as backlinks:** make sure the AWS Marketplace, HubSpot Marketplace, Microsoft AppSource and APN listings link to the correct new pages.
- **Docs site** as a source of long-tail traffic (error messages, setup questions).
- **Reviews:** ask customers for reviews on the marketplaces (see proof plan).
- **No** paid links, directory blasts or comment-spam-style tactics.

## 8. Risks

| Risk | Mitigation |
|---|---|
| Traffic drop after removing 40 pages | Redirect one-to-one; keep the terms in new pages; monitor weekly; adjust from the baseline |
| Spam-flooded pages carried toxic backlinks | Backlink audit first; use 410 for those URLs if needed |
| Rename to "Amazon Connect Customer" shifts searches | Cover both terms; check Search Console monthly |
| Marketplace listing text drifts from the site | One owner keeps listing and page copy in sync |
| New site launches without measurement | Launch is blocked until tracking and baselines exist |
