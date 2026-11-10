# Competitor scan

> **Update, 21 Sep 2026 (later the same day):** a second pass found that the connector niche is **more crowded and cheaper than the first pass suggested**. See the addendum at the end. Where this file's earlier text says OB is "below" the competitor's price, read it as "below Odea only".

Fetched 21 September 2026. Each site's home or key product page was read once through a summariser. Treat every "proof" and "pricing" line as *what the page showed on that day*, not a full audit. Two attempted fetches failed (Aircall's HubSpot integration page returned 404; 4connect.io did not resolve) and Local Measure now redirects to Zendesk.

## Why this set

OB is really two things (see the HubSpot analysis): a **connector product** bought by existing Amazon Connect customers, and an **AWS-adjacent services shop** reached mostly through AWS and partners. Buyers arrive from those two directions, so the peer set has two groups plus one "alternative" that shows what the buyer could do instead.

| Group | Why included | Who |
|---|---|---|
| **1. Direct rival: same product, same buyer** | The other Amazon Connect ↔ HubSpot CTI connector vendor that turned up repeatedly in search, listed on AWS Marketplace alongside OB (other vendors may exist; I did not run an exhaustive search) | **Odea Integrations** |
| **2. Alternative the buyer could pick** | HubSpot users who don't already run Amazon Connect will buy a phone system that is native to HubSpot. Most OB leads never name a competitor, so this is the likeliest silent alternative | **Aircall** |
| **3. Amazon Connect service partners (same AWS programme, similar credentials)** | They compete for AWS-referred opportunities, and their sites show how the category earns trust | **contactSPACE** (outbound + product), **USAN** (large SDP), **Call Center Power** (services-only) and **NeuraFlash** (AI + own desktop product; now part of Accenture) |
| Noted but not analysed | Local Measure (agent desktop for Amazon Connect) now redirects to Zendesk, a reminder that desktop tools get absorbed by platform vendors | n/a |

**Not included, on purpose:** Genesys, NICE, Five9, Talkdesk, Twilio Flex. Named competitors barely appear in OB's emails (9 threads of about 330), and the buyer already chose Amazon Connect. **AI-voice-agent start-ups** (Vapi, Retell, ElevenLabs) are integration targets on OB's own AI page, not peers. **Native AWS/Salesforce CTI adapters** are a real alternative I could not analyse in the same way (no separate marketing site). I would treat them as the "do it yourself" option.

## Findings by competitor

### Odea Integrations: the one to watch (direct rival)
- **Positioning:** "Seamlessly connect your contact center with HubSpot CRM using Odea's powerful CTI Adaptor". Their site also sells services and a voice AI product, but the connector has a page of its own.
- **Pricing: transparent.** Startup **$24**, Standard **$28**, Professional **$35** per agent per month, each including the licence, implementation, go-live consultation hours and annual support of varying levels.
- **Proof:** AWS Select Tier Services Partner; "20+ years" claimed; **four named-vertical success stories** (university, patient-recruitment organisation, forklift company, media group); a Clutch profile with 3 reviews.
- **CTAs:** Book a Demo, Get a Quote, Get Started, Contact Us. No self-serve trial; buying is by consultation.
- **Navigation:** Services, Products (voice AI, CTI connectors, an omni-channel agent product), Industries (9), Resources.
- **What this means for OB:** OB's monthly rate ($15–20 quoted) is **roughly 25–50% below Odea's public monthly price** for a near-identical feature set, but a buyer cannot see that. It also is not a like-for-like comparison: Odea's price includes implementation, while OB's quotes often add a one-time setup fee ($500–$5,000). For a 10-agent team the first-year totals come out close (about $2,600–$3,200 for OB at $18 plus setup, against about $2,880 for Odea's entry tier). OB's advantage is clearest at higher agent counts and on the ongoing rate. Odea also wins by showing named-vertical stories and clear tiers.

### Aircall: what a HubSpot buyer might buy instead
- **Positioning:** "Customer communications, evolved with AI that handles customer interactions, end to end." Three product lanes: team-led, AI-assisted, AI-led.
- **Pricing:** none on the pages fetched (I did not read a separate pricing page).
- **Proof:** "23,000+ companies", five logos, one named quote; SOC 2 Type II, GDPR, HIPAA badges.
- **CTAs:** "Try for Free" and "Talk to Sales" side by side; **250+ integrations** highlighted with HubSpot near the front.
- **Content:** gated implementation guide; heavy "no technical skills needed" message.
- **What this means for OB:** an Aircall-style buyer expects **a free trial without a call**, badges (SOC 2), and setup measured in hours. OB's offer is different (bring your own Amazon Connect), so it should say so plainly instead of competing on Aircall's terms.

### contactSPACE: outbound dialling on Amazon Connect
- **Positioning:** "We'll help you build the perfect outbound-enabled contact center solution, on AWS." Sells a **named product line** (plug-ins and APIs) alongside services.
- **Pricing:** none shown.
- **Proof:** AWS Qualified Software Partner and Service Delivery Partner badges, **ISO 27001**, one named case study, offices in four regions.
- **Relevance:** the closest match to OB's robocall/campaign tooling. It leads with **one sharp use case** (outbound), not a catalogue.

### USAN: large Amazon Connect service delivery partner
- **Positioning:** "Solutions Purpose-Built for Your Business"; migration to Amazon Connect ("deploy up to 50% faster"), managed services, AI analytics.
- **Pricing:** none.
- **Proof:** **15 customer logos** (well-known consumer, financial and healthcare brands), four case studies, **quantified claims** ("25% decrease in agent onboarding time", "20% increase in agent productivity"), SOC 2, HIPAA, PCI DSS, Generative AI competency.
- **Content:** podcast, blog, four e-books, 15 FAQs, news.
- **What this means for OB:** the bar for enterprise trust in this category is logos, numbers and compliance badges. OB has none of the three on the page. It should not chase USAN's breadth; it should copy the *evidence style*.

### Call Center Power: services-only, evidence-heavy
- **Positioning:** "Improve CX and Reduce Your Contact Center Costs". Consulting, outsourcing, technology enablement, managed services (no own software).
- **Pricing:** none; CTAs are "Get a cost proposal" and "Start Your Evaluation".
- **Proof:** **30+ logos, 12 case studies with measurable outcomes, 7 director/VP testimonials**, 11 industry verticals.
- **Relevance:** shows that a small services firm's site is essentially a **proof library**.

### NeuraFlash: AI + Salesforce + Amazon, now inside Accenture
- **Positioning:** "Top Gen AI Partner for Salesforce & AWS"; own products including a desktop for Amazon Connect.
- **Proof:** "1000+ implementations", "4.9 CSAT", AI-impact percentages, big-brand logos.
- **Relevance:** upmarket, so not a direct rival. Useful as a picture of where the category is heading: AI-first messaging.

## Cross-cutting patterns

| Pattern | Evidence | Implication |
|---|---|---|
| **Pricing is almost never public** in this category. Odea is the exception among the sites I read. | Aircall, contactSPACE, USAN, Call Center Power, NeuraFlash show none; Odea shows three tiers | Publishing a price is a *differentiator*, not a norm. OB can be transparent (but see the addendum: it is not the cheapest) |
| **Proof = logos + numbers + badges.** | USAN, Call Center Power, NeuraFlash, Aircall all show named logos and numbers | OB has anonymous case studies only. Proof is its biggest gap |
| **Sharp use-case leads look more credible than a catalogue** *(my judgement, not tested)*. | contactSPACE (outbound), Odea (HubSpot connector page) | OB's 15-product menu reads as a generalist with no specialism |
| **Every site has a "talk to us" CTA. Only Aircall pairs it with a self-serve trial.** | All | A "try it" path would be unusual in OB's niche |
| **Content strategy:** e-books, podcast, and case-study libraries are the norm for larger firms. Small specialists lean on case studies and customer quotes. | USAN, Call Center Power | OB's realistic play is a small number of deep, technical pages (docs, how it works, security, costs), not a volume blog |
| **AI messaging is everywhere.** | Aircall, USAN, NeuraFlash | "AI voice agent" is a crowded claim. OB's credible edge is the connector, which is boring and true |

## Gaps in this scan

- I did not read pricing pages beyond Odea's, or any competitor's docs, changelog or status pages.
- No traffic, rankings, backlink or review data for any competitor; that needs Semrush/Ahrefs or similar.
- I did not scan HubSpot-marketplace competitors listing under the "calling" category; the HubSpot Marketplace listing pages weren't reachable without login.
- Ratings and sizes for competitors are their own claims.


## Addendum: second pass (market direction and the connector niche)

### More connector vendors, and a cheaper one
Searching AWS Marketplace and the wider web turned up **at least four vendors selling an Amazon Connect ↔ CRM connector**, not one:

| Vendor | HubSpot | Dynamics 365 | Price seen | Trial |
|---|---|---|---|---|
| **ProUCX** (Australian) | Yes | Yes (also Pipedrive, mobile softphone) | **$9 Standard / $15 Premium per active agent per month**, billed monthly in arrears, metered by active use, on AWS Marketplace | **14-day free trial** |
| **Odea Integrations** | Yes | Yes | $24 / $28 / $35 per agent per month (implementation included) | Demo or quote |
| **Cornerstone CX** | Yes ("HubSpot Hub for Amazon Connect") | Yes | Not seen | Not seen |
| **Maaz SmartConnect** and others | n/a | Yes (also on Microsoft's marketplace) | Not seen | Not seen |
| **Octavebytes** | Yes | Yes | About $15–20 quoted; listing says "private offer"; site shows nothing | 7 days, by call |

ProUCX's own site has no case studies or testimonials and its main CTA is "Book a demo". But its **AWS Marketplace listing is a metered SaaS product with public prices and a free trial**, which is easier to buy. OB's listing is categorised under "Professional services" with a "Request private offer" button. *(I read that off the listing's breadcrumb and buttons; confirm in the AWS seller console.)*

**What this changes.** My first-pass idea, "publish a lower price than the rival and win on price", is **wrong**. OB's $15–20 sits in the middle of this niche, above the cheapest ($9) and below the most expensive ($35). The plain softphone-in-CRM is heading toward commodity pricing. OB's edge has to be what it *adds* to the softphone.

### Where OB genuinely differs (from listings and emails)
- Voice **plus SMS, WhatsApp and social channels** in one connector (ProUCX's Standard tier lists voice only; check Premium).
- **Transcription and AI summaries written back to the CRM record**, and, for two customers, custom features (real-time transcription, chat, Breeze AI transcript placement).
- **A human engineer deploys it into the customer's AWS account** (CloudFormation), with SSO and custom queue logic.
- **AWS FTR-certified** (per the Marketplace listing).
- **GoHighLevel and SuiteCRM connectors**, which none of the vendors above appear to sell.
- **Outbound campaign and AI voice tooling** with delivered banking work (bilingual Urdu/English).

### Market direction (sources fetched 21 Sep 2026)
- **AWS is repositioning Amazon Connect as an agentic-AI suite.** On 28–29 April 2026 the original product was renamed **"Amazon Connect Customer"**, alongside new Decisions, Talent and Health products. AWS announced 29 agentic-AI features at re:Invent 2025, and on 23 April 2026 acquired the conversational-AI vendor NLX. Named customers include Capital One, Hilton, State Farm, Air Canada and United Airlines. ([No Jitter](https://www.nojitter.com/contact-centers/amazon-connect-becomes-connect-customer-), [SiliconANGLE](https://siliconangle.com/2026/04/28/amazon-connects-second-act-contact-center-agentic-ai-suite/))
- **HubSpot ships its own calling and AI (Breeze).** A large customer deployment asked OB to write transcripts into HubSpot's native Breeze AI fields. The value is moving from "a softphone in the CRM" to "what happens to the conversation afterward".
- **AWS Marketplace is the procurement path for AWS-centric buyers**, and it now supports private offers, channel-partner private offers and, from 1 June 2026, requires new SaaS products to support Concurrent Agreements. ([AWS docs and guides](https://aws.amazon.com/marketplace/features/cpprivateoffers))
- **Implication:** the Amazon Connect base keeps growing, so demand for CRM connectors grows with it. But the connector alone will be squeezed on price by ProUCX-style products, and AWS's own native AI agents make a generic "AI voice agent" a crowded claim.

### Naming risk for SEO
"Amazon Connect" is now "Amazon Connect Customer" in AWS's own language. Buyers, and OB's own emails, still say "Amazon Connect", and most searches will for some time. The site should use **"Amazon Connect"** as the primary term and mention **"Amazon Connect Customer"** on key pages. Confirm with Search Console once it is available.
