# Phase 4: comparison against the existing Next.js build

> **Read-only exercise.** I read `/Users/hhh/Documents/Projects/ob-website` (37 page files, 38 sitemap URLs, committed once on 8 Jul 2026) and changed nothing there. This file is the only thing written. Customer names that appear in that repo's own data files are **not repeated here**, because they are marked "pending sign-off" in that repo and are not live on any public page — the same confidentiality rule I've applied throughout applies to this report too. I refer to them by industry instead.

## Plain-language summary

**Both builds are serious, evidence-aware work, and they agree on more than I expected going in — which is the most useful signal in this whole exercise.** Independently, with no shared context, we both:
- Cut the same five dead single-feature pages from the old site (wallboard, voice recording, both queue-selection duplicates, dynamic caller ID, QuickSight as a standalone page).
- Built a page for AWS account teams, separate from a page for reseller/delivery partners — because the emails show those are different audiences with different needs.
- Landed on **$18 per agent per month as the real, defensible HubSpot connector price** (my research found it as the most-quoted figure in 2025–26 emails; the Next.js build put it straight on the page).
- Kept the AWS FTR certification, which the *current live site never mentions*, as a headline trust signal.
- Treated the case studies as evidence that needs the customer's written sign-off before anything goes live, not as marketing copy to write freely.

**Where we genuinely differ, it's one big decision, not a hundred small ones: what Octavebytes is *for*.** The Next.js build is written as a **migration consultancy** — "modernize your contact center, leave Cisco or Genesys, zero disruption" — aimed at mid-market enterprises who don't yet have Amazon Connect. My build is written as a **connector product** — "Amazon Connect, inside your CRM" — aimed at smaller teams who already have Amazon Connect and need it wired into HubSpot or Dynamics. I went back to my own deal and email data specifically to check this, rather than take either version on faith: **the deal data supports my reading, not the migration-consultancy reading.** I found no pattern of "displace Cisco/Genesys" deals in the CRM; I found 36 of 88 deals and nearly all 2025–26 revenue tied to the CRM connector, sold mostly at 3–20 agents. "Mid-market enterprise" is a real stretch for a business whose typical deal is a few thousand dollars a year. That doesn't mean the Next.js build is badly made — it's the more ambitious, better-produced version of the story the *old* site already told about itself, and it inherits that story's evidence problem along with its ambition.

**On execution, the two builds are strong in different places.** The Next.js build has a fuller catalogue (38 URLs to my 25), a real blog with four well-written, specific posts that do the job I left as placeholders on my docs/security pages, and a bigger design swing (navy + AWS orange, versus my four options that all stay close to the existing blue). Mine has a centralized, transparent pricing page with a working cost estimator (the Next.js build has no `/pricing` route at all), and a stricter internal discipline about not asserting anything I couldn't check (130 open flags, all visible, versus a few strong claims in the Next.js build — a "no call content ever leaves your AWS account" security promise, an "$18… listed with public per-seat pricing" claim about the AWS Marketplace listing that contradicts what that listing actually says today, and "used on every migration engagement… without a single configuration error" for an internal tool — that read as asserted rather than sourced).

**My recommendation: merge, and lead with the Next.js build's execution wrapped around my positioning and pricing.** Full ranked recommendation is in §6.

---

## 1. What each site is trying to be known for

| | Next.js build | My build |
|---|---|---|
| **One-line positioning** | "Modernize Your Contact Center. Zero Disruption to Your CRM." — a migration consultancy for teams leaving Cisco, Genesys or custom telephony | "Amazon Connect, inside your CRM." — a connector product for teams that already run Amazon Connect |
| **Assumed starting point of the buyer** | Does *not* have Amazon Connect yet; is deciding whether to move off legacy telephony | *Has* Amazon Connect; needs it wired into HubSpot or Dynamics 365 |
| **Named customer segment** | "Mid-market enterprise" (used repeatedly: hero, About, AWS co-sell headline, careers) | Not segment-named; audience is defined by task ("teams running Amazon Connect") |
| **Secondary story** | AI-native modernization (Celesta, Contact Center AI, Bedrock, Amazon Q) sits alongside migration as a second pillar | AI (call intelligence) is explicitly a *feature of the connector*, not a separate pillar; banking/regulated voice is a distinct, named second lane |

**Which claim does the evidence support better?**

- **The deal data supports the connector story, not the migration story.** Of 88 deals, 36 mention a CTI connector, and the HubSpot analysis found the *entire* commercially live email volume in 2025–26 is trials, licences, renewals and support for the connector. I looked specifically for a "leaving Cisco/Genesys for Amazon Connect" deal pattern to check the Next.js positioning fairly, and didn't find one — the closest matches in the emails are a customer already on Cisco asking about voice-recording integration (not a migration), and the old site's own "Migration to Amazon Connect" service page, which had no deals attached to it either.
- **"Mid-market enterprise" overstates the median deal.** A handful of deals do reach real scale (one hospitality customer's connector deal was described in the Next.js case-study data as 40+ seats; a few historical project deals ran $6,500–$36,000), so the language isn't fabricated — but the typical connector deal is 3–20 agents at roughly $18/agent/month, which is a small or lower-mid-market account, not an enterprise one. The Next.js build's positioning describes the top of the funnel as if it were the median.
- **The "45+ completed engagements" and "delivering since 2021" stats (Next.js `awsProofPoints`/`TrustStats`) check out.** 18 closed-won plus 27 legacy "Closed-Paid" deals is exactly 45, and the earliest deal record in the CRM is from June 2021. These are the two strongest, most literally-verifiable facts on either site, and they're both on the Next.js build. I don't have equivalent aggregate stats on my own homepage yet — mine are marked `[DATA NEEDED]` rather than filled in. **This is a point in the Next.js build's favor**, not a wash.
- **My positioning is the one built to match where the revenue actually is now, at the cost of sounding smaller.** That's a real trade-off, not a free win: "Amazon Connect, inside your CRM" is a narrower, less impressive-sounding pitch than "modernize your contact center," and it says nothing to a prospect who hasn't chosen Amazon Connect yet. My services page (`/solutions/amazon-connect-services/`) covers migration as one offering among several, not the headline.

**Verdict:** the Next.js build's positioning is the more ambitious claim and the weaker-evidenced one. Mine is the better-evidenced claim and the more modest one. Neither is dishonest; they're optimizing for different things (a bigger story vs. a defensible one).

## 2. Information architecture: agreement and divergence

### Where the two structures independently agree

| Decision | Next.js build | My build |
|---|---|---|
| Cut the wallboard (Octave Vision) as a standalone page | Not in the sitemap | Folded into Amazon Connect services |
| Cut Voice Recording as a standalone page | Not in the sitemap | Folded into the HubSpot connector's feature list |
| Cut both Queue Selection duplicates | Not in the sitemap | Folded into Amazon Connect services |
| Cut Dynamic Caller ID as a standalone page | Not in the sitemap | Folded into Amazon Connect services |
| Cut QuickSight as a standalone page | Not in the sitemap | Folded into Amazon Connect services |
| Give AWS account teams their own page, separate from partners | `/partners/aws-co-sell` (noindexed) | `/partners/aws/` |
| Give resellers/integrators their own separate page | `/partners/become-a-partner` | `/partners/` |
| Move Government Procurement out of the main nav | Kept as a page but not top-level; reached via the Company dropdown | Footer-only |
| Treat AWS FTR certification as the headline technical credential | Yes — its own `/aws` page and a `TrustStats` banner | Yes — hero trust strip and product pages |
| Split GoHighLevel from HubSpot in messaging (different buyer, smaller teams) | Own page, own (undisclosed) pricing | Merged into "Other CRMs," priced "on request" |
| Treat case studies as evidence needing written customer sign-off, not copy to write freely | Explicit amber banner: "none of the named customers has signed off... get written permission before this page goes live" | Explicit proof-plan gate: nothing publishes without a permission tier |

That's ten independent agreements from two people working from the same underlying CRM with no shared brief beyond "look at the evidence." That's a stronger signal than either of us reasoning alone — in particular, the wallboard/voice-recording/queue-selection/caller-ID/QuickSight cut is a good sign that the *old* site's page count really was inflated with dead weight, since we didn't compare notes and cut the same five pages.

### Where the structures diverge, and which is stronger

| Divergence | Next.js build | My build | Which is stronger, and why |
|---|---|---|---|
| **Overall catalogue size** | 38 URLs; keeps Agent Desktop, full Omnichannel section (+ MultiChat, WhatsApp sub-pages), Automation, AI Chatbot, Contact Center AI, Managed Services, and SuiteCRM each as their own page | 25 built (plan: ~28); these are folded into one or two pages each | **Mine**, on the evidence: Phase 1 found Agent Desktop in exactly one open $300 deal, wallboard only as a 2025 cross-sell, and no live SuiteCRM customer anywhere in the data. Phase 1 flagged the *old* site's "15 products, no clear lead" as a core weakness; a 38-URL catalogue organized into cleaner buckets is a better-organized version of the same problem, not a fix for it. |
| **A dedicated, centralized pricing page** | None — pricing is inline on product pages only, and only the HubSpot page discloses a number (GoHighLevel and Dynamics both say "contact us") | `/pricing/` with a live cost estimator, disclosed AWS-cost breakdown, and one price card reused everywhere | **Mine.** Pricing was the single most-asked question in the emails (75 threads). Making a buyer hunt product-by-product, and getting "contact us" on two of three CRMs, reproduces the exact opacity Phase 1 flagged on the old site. |
| **Trial length consistency** | 7 days (HubSpot) vs. 2 weeks (GoHighLevel) vs. "available on request" (Dynamics) — three different answers to the same question, unexplained | One rule (7 days) applied everywhere, flagged `[CONFIRM]` pending the owner | **Mine**, on consistency; but neither of us has actually confirmed a single trial policy with the owner, so this is a soft win. |
| **Docs / security / changelog as separate pages** | None exist. Instead, four blog posts do real work here: *AWS Marketplace private offers, explained*; *What AWS FTR certification actually checks*; *HubSpot CTI screen pop, explained*; *Leaving Cisco for Amazon Connect: a phased approach* | `/resources/docs/`, `/resources/security/`, `/resources/changelog/` exist as pages but are mostly `[CONFIRM]`/`[DATA NEEDED]` shells | **The Next.js build**, honestly. Its blog posts are finished, specific, and answer real objections from the emails (screen-pop matching behaviour, private-offer mechanics, FTR scope) in readable prose. My equivalent pages are correctly *scaffolded* to the right questions but contain no answers yet. If I had to ship today, theirs is more useful to a visitor; mine is more honest about what isn't known yet. |
| **Indexing of the AWS-facing page** | Explicitly noindexed (`robots: { index: false, follow: false }`) | Indexed and linked from primary nav | **The Next.js build's call is better reasoned.** A page meant to be forwarded by email to a named AWS contact doesn't need to rank in search, and keeping it out of the index avoids a stray public page that reads oddly to a general visitor. I should adopt this. |
| **Design departure from the current brand** | New palette entirely (`navy #0a192f` + `AWS orange #ff9900`), while keeping the exact existing blue-cloud logo file unmodified | Four options, all either keeping the existing blue exactly (A) or staying close enough that the existing logo still fits (B); C and D require a new logo | **Neither is simply "more correct."** The Next.js build's navy-and-orange doesn't actually match its own logo's blue, which is the kind of inconsistency my design direction was written to avoid (`03-design-direction.md` says keep the accent tied to the logo). But AWS orange is a legible, deliberate way to say "AWS partner" at a glance, which mine doesn't do visually at all. This is a genuine matter of taste, not evidence — I'll say so plainly rather than declare a winner. |
| **Lead capture mechanism** | A single universal `/demo` form for every interest (celesta, CTI, partnership, government, careers...), submitted via `mailto:`, exactly like the current live site's Contact Form 7 | Six purpose-specific forms (trial, contact, partner, AWS opportunity...), built to POST to HubSpot's Forms API with UTM/source tracking, gated behind consent (not yet wired to a live HubSpot form as of this Phase 3 build) | **Mine, on architecture; theirs matches what's shippable today.** Phase 1's single biggest structural finding was that the current site's email-only forms are *why* ~99% of HubSpot contacts show "Offline" as their source — there's no way to attribute a lead to a campaign or page. The Next.js build's `mailto:` submission reproduces that exact problem instead of fixing it. My version is architected to fix it, but it isn't live yet either — no HubSpot form GUIDs are configured. Neither implementation is done; only one of the two designs actually closes the gap once it is. |
| **Industries as a first-class nav item** | Yes — `/industries` plus four vertical pages (financial services, retail/e-commerce, healthcare, BPO/outsourcers) | No — regulated-sector work has one page (`/solutions/banking-and-regulated-voice/`); no industries section | **The Next.js build**, partially. The financial-services and BPO/outsourcer pages track real patterns in the data (compliance-heavy buyers; a meaningful share of pipeline arriving through partner/subcontract routes). The **healthcare page is the weak one**: its headline is "legacy telephony migration for clinical and patient-facing teams," and I found no clinical or healthcare-sector deal or thread anywhere in the CRM. That page reads as a template filled in by analogy to "what a contact-center vendor's industries page usually says," not something the deal data supports. |

## 3. Content and proof

### Case studies

Both builds independently identified the **same underlying situation**: the CRM has three or so relationships worth writing up, none has given permission yet, and the current live site's anonymous case studies ("Global Consumer Corporation," "a Leading Bank in Pakistan") are weak because they carry no name and no number.

- The **Next.js build went further and actually drafted three named case studies** from deal records (financial services, retail/logistics, hospitality), each with specific claimed outcomes (a security-review pass, a seat count, a "since [month/year]" production date). It gates them behind an explicit on-page notice that none has signed off yet.
- **My build stopped one step earlier**: a proof plan (`design/02-proof-plan.md`) that ranks the same kind of candidates, names the specific frictions to resolve first (a licence lapse, a price dispute, an unresolved bug) before asking, and a case-study *template* rather than filled-in drafts.
- **One real difference in judgment, not just thoroughness:** the Next.js financial-services case study reads as a clean, entirely positive account — proof-of-concept, migration, security sign-off, "live in production... billed per agent seat" — with no mention of any of the support friction visible in that account's own email thread (a UI bug after a HubSpot update, a renewal question). My proof plan explicitly flags that exact account as "resolve and document the fix first" before using it as a reference, precisely *because* of that friction. Writing the case study before resolving what the emails show isn't dishonest — the outcomes listed are all real, drawn from the deal record — but it's incomplete in a way that could read as evasive if the customer or a prospect who talked to that customer noticed the gap.
- The Next.js build's **industries page for financial services independently restates a version of the same case study's ISO 27001 result as a general capability claim** ("Our HubSpot CTI Connector has passed customer-run vendor security reviews"), without the same "pending sign-off" caveat that sits on the case-studies page. That's an internal inconsistency worth fixing regardless of which build ships: the same unconfirmed fact is treated cautiously in one place and asserted as settled in another.

### Pricing transparency

| | Next.js build | My build |
|---|---|---|
| HubSpot connector | **$18/agent/month, disclosed on the page** | $15 (Core) / $20 (Plus), disclosed, `[OWNER DECISION]` pending |
| Dynamics 365 connector | "Contact us for per-agent pricing" | Same $15/$20 card, `[CONFIRM]` whether Dynamics should differ |
| GoHighLevel connector | "Contact us for per-agent pricing" | Same $15/$20 card, `[OWNER DECISION]` on GHL-specific pricing |
| Setup fee | Not disclosed anywhere I found | $500 fixed, disclosed |
| A page a buyer can compare plans on without contacting sales | No `/pricing` route exists | `/pricing/` exists, with a working estimator |

**On the actual number:** the Next.js build's **$18 flat rate is the single most literally evidenced price in either build** — it's the exact figure quoted most often in 2025–26 emails, with no invented tiering. My **Core/Plus $15/$20 split is a bundle I proposed**, anchored on real evidence (a $5 uplift one customer actually accepted for added features, and the range of quotes from $15–24), but it is a genuine invention on my part, clearly marked as a proposal awaiting the owner's decision — not something either dataset states directly. I should be honest that the Next.js number needs less interpretation to defend than mine does.

**On transparency as a strategy:** disclosing a price for one product and not the other two, on a site that otherwise emphasizes "transparent, per-seat pricing" as a section heading, undercuts its own claim. Either commit to disclosing all three or none.

### Credentials

Both builds correctly surface AWS FTR certification, which the *current* live site never mentions despite it being the strongest available technical credential (Phase 1's single clearest "missing" finding). Both cite the same three AWS partner tiers. The Next.js build adds a fourth and fifth badge ("Amazon Connect Ready" as distinct from "Amazon Connect Delivery," and "Top AWS Consultants," a third-party recognition) that I did not verify and have not carried onto my own site — I'd treat "Top AWS Consultants" the same way I treated every other badge claim: confirm it's current and get AWS's/the third party's brand permission before publishing it, not assume it from a data file.

### A specific, checkable factual problem in the Next.js build

The `/aws` page states: *"The HubSpot CTI Connector is listed with public per-seat pricing and a 7-day free trial"* on AWS Marketplace. When I fetched that same AWS Marketplace listing directly during Phase 1 research, its pricing section read: *"Custom pricing options... Pricing is based on your specific requirements and eligibility. To get a custom quote for your needs, request a private offer."* That is a private-offer listing, not a public-price listing. This may have changed since either of us looked, but as of the evidence I gathered, the Next.js build's claim about its own AWS Marketplace listing appears to be wrong, and it's a claim on a page whose entire purpose is "every credential below is a third-party check... here's what to confirm it." I'd verify this in the AWS Seller Console before publishing either version of the site.

### Other claims worth checking before either site ships

| Claim | Where | Why it needs a check |
|---|---|---|
| "No call, chat, or message content is sent to any Octavebytes-operated system"; "Credentials and secrets live in AWS Secrets Manager, inside your account" | Next.js blog post, *What AWS FTR certification actually checks* | Specific, strong, checkable security claims. I flagged the identical question `[CONFIRM]` on my own security page because I found nothing in the CRM or email data that verifies exactly what data does or doesn't reach Octavebytes systems. If these statements are true, they're a genuine asset and should move onto a real security page (not just a blog post) with the same confidence. If they're aspirational, they're a real liability risk for any customer relying on them for their own compliance sign-off. |
| "Used on every OctaveBytes migration engagement" / "without a single configuration error" (MCP Automator) | Next.js `platform/mcp-automator` page | Absolute claims with no supporting record in the deal or email data I reviewed. This is the same *kind* of unsupported superlative Phase 1 flagged on the current live site ("increase efficiency by up to 300%"); it shows the pattern can survive a rebuild even when the rebuild is otherwise more disciplined. |
| Healthcare as a named industry vertical | Next.js `/industries/healthcare` | No healthcare-sector deal, contact, or email thread found anywhere in the CRM data reviewed across both phases. |
| `contact@octavebytes.com` as a live inbox | Next.js `CONTACT_EMAIL`, used on the Contact and AWS-co-sell pages | The live site and every email signature I reviewed use only `sales@` and `support@`. I can't confirm `contact@` is a monitored inbox. |
| "Mid-market enterprise" as the customer description | Next.js hero, About, careers, AWS co-sell headline | Addressed in §1 — supported at the top of the funnel, not representative of the median deal. |

## 4. Where the two independently agreeing is the strongest evidence in this whole report

Repeating this because it matters more than any single disagreement: **neither of us saw the other's work before building.** That two independent readings of the same CRM data landed on the same five pages to cut, the same two-audience split for AWS teams versus resale partners, the same $18 HubSpot figure, the same "FTR is the missing credential" finding, and the same "case studies need permission before they're customer-named" governance rule, is a much stronger signal that these particular conclusions are *right* than either build reaching them alone would be. If I were advising the owner on what to treat as settled without further debate, it's this list.

## 5. What each has that the other doesn't (quick reference)

**Next.js build has, and mine lacks:**
- A working, deployed-feeling catalogue of 38 pages with consistent visual design and working navigation, right now.
- Four finished, specific, well-written blog posts that function as the docs/security content mine only scaffolds.
- Verified-feeling aggregate stats on the homepage (45+, 2021, 5 regions) — mine has none yet.
- Industry vertical pages, two of which (financial services, BPO/outsourcers) track real patterns in the data.
- A distinct, noindexed AWS co-sell page, separated from the general partner page more cleanly than mine.
- Three fully drafted (if unapproved) case studies, further along than my template.

**My build has, and the Next.js build lacks:**
- A centralized, transparent pricing page with a working cost estimator; the Next.js build has no pricing page at all.
- Consistent pricing disclosure logic (even though the number itself is a proposal) rather than one product priced and two not.
- A redirect map with a self-testing build step that verifies every rule fires exactly once and none captures a live page. (**Correction, added after this report was first written:** I initially stated the Next.js build had no legacy-URL redirects at all. That was wrong — `next.config.ts` has 109 redirect rules, covering essentially the same legacy URL set, including some more precise than mine, e.g. redirecting a retired single-feature page straight to the right `#anchor` on its new hub page rather than just the hub page's top. Its coverage looks comprehensive on inspection, though I have not run the same automated one-rule-per-URL self-test against it that I run against mine.)
- A lead-capture architecture designed to close the exact CRM-attribution gap Phase 1 identified, rather than reproducing it with `mailto:`.
- A visible, self-enforced discipline about unverified claims (130 flagged items, a build step that refuses to ship while any remain) versus a smaller number of confidently-stated claims that didn't all check out.
- A narrower catalogue that matches the "small firm, be narrow" implication of Phase 1's revenue evidence.

## 6. Recommendation, ranked by impact

**Overall: merge. Use the Next.js build as the production codebase and visual system; replace its positioning, pricing structure, and lead-capture plumbing with the versions built in this project.** Neither build should ship as-is.

1. **(Highest impact) Rewrite the homepage, About page, and AWS co-sell headline around the connector, not migration.** Keep "Modernize your contact center" language, if the owner likes it, as a sub-theme for the services/migration page — but the site's *main* promise should be "Amazon Connect, inside your CRM," because that's where the deal evidence is. This is a content and IA change, not a rebuild; it does not require touching the Next.js codebase's structure.
2. **(High impact) Build a real `/pricing` page inside the Next.js app**, using either the $18 flat figure (less invented, more literally evidenced) or my Core/Plus $15/$20 split (more product-market logic, needs the owner's sign-off) — but pick one and disclose it for all three CRM connectors, not just HubSpot. Reuse my cost-estimator logic; it's a small, self-contained component.
3. **(High impact) Fix lead capture before launch, regardless of which frontend ships.** Replace every `mailto:` form submission with a real HubSpot Forms API integration, with UTM and source-page fields carried through as hidden fields. This is the single concrete fix for the attribution problem Phase 1 identified in the *current* site, and it is not yet fixed in either candidate.
4. **(Medium impact) Cut the catalogue.** Fold Agent Desktop, Omnichannel/MultiChat/WhatsApp, Automation, AI Chatbot, and SuiteCRM down to sections of one or two pages, the way both builds already agreed to do for wallboard, voice recording, queue selection, caller ID and QuickSight. Keep them reachable, just not each as a headline page.
5. **(Medium impact) Resolve the specific factual risks before launch:** verify the AWS Marketplace listing's actual pricing model (public vs. private offer) before repeating either claim; verify the two absolute security claims in the FTR blog post with whoever built the connector, or soften them; verify or drop "used on every migration engagement... without a single configuration error"; verify `contact@octavebytes.com` is a real, monitored inbox or remove it; either get real evidence for a healthcare vertical or drop that page.
6. **(Medium impact) Keep the Next.js build's four blog posts and its "Why AWS" credential page almost as-is** — port the wording style and structure into my docs/security/changelog pages, once the specific technical facts they assert are confirmed by someone who can actually verify them (see item 5).
7. **(Lower impact, still worth doing) Reconcile trial length to one policy** (7 days is used in more places and matches the current live site) **and noindex any page meant to be forwarded by email rather than found in search** (adopt the Next.js build's choice for the AWS-facing page).
8. **(Lower impact, a taste call, not evidence) Pick a colour direction deliberately, not by accident.** If the owner likes the navy-and-AWS-orange system already built and mostly working in the Next.js codebase, keep it, but fix the mismatch between that palette and the still-blue logo (either recolour the logo to match, or bring the accent back toward the logo's blue, which is what Options A and B in the Phase 3 prototype already do). If the owner prefers the four Phase 3 options, review those against this same navy/orange system side by side before deciding.

**What I would not do:** discard either codebase outright. The Next.js build is materially further along as a shippable product (working navigation, finished prose, a real design system, industry pages with real substance in two of four cases). My build's contributions are concentrated in exactly the places Phase 1 found the current site weakest — price transparency, lead attribution, and claim discipline — and those are the parts worth carrying over, not the whole site.
