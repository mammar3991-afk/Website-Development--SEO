# Decision and strategy

> **INTERNAL.** Built on the Phase 1 research in `../research/`. Marks which statements are evidence and which are my judgement. The decisions the owner must make are collected at the end.

## 1. The decision

**Make Octavebytes the specialist for one thing: making Amazon Connect work inside the CRM a team already uses, and turning every call into CRM data with AI on top. Lead with the HubSpot connector, follow with Dynamics 365, and use the delivered banking work as a second, clearly separate lane. Cut everything else from the front of the site.**

The site's tagline becomes **"Amazon Connect, inside your CRM."**

The homepage has **one job: get a team that runs Amazon Connect and uses HubSpot or Dynamics 365 to start a trial.** Every other page serves that job or serves one of the four other audiences below.

## 2. Why this and not the alternatives

| Option | For | Against (evidence) | Verdict |
|---|---|---|---|
| **A. Stay a broad Amazon Connect consultancy** (today's site) | It is how the company started; AWS partner status supports it | No proof (all case studies anonymous); competes with USAN, Call Center Power and NeuraFlash, which show 15–30 named logos and quantified results; the freelance/project deals are small and shrinking; 15 products with no clear lead | **Reject** |
| **B. Be the cheapest connector** | Pricing is currently hidden, so publishing looks like a win | The first-pass idea assumed Odea was the only rival. **ProUCX lists $9 / $15 per agent with a 14-day trial on AWS Marketplace.** OB's $15–20 is mid-market. A race to $9 kills a business whose customers average 3–20 agents | **Reject** |
| **C. Specialist: connector + call-intelligence + AI/outbound for regulated sectors** | Connector deals appear every year (36 of 88 deals); 2026's wins and upsells are transcription, summaries, custom chat and voice AI; AWS is moving Connect toward agentic AI, so value is shifting from "softphone in the CRM" to "what happens to the conversation"; OB has already delivered banking voice/outbound | Requires OB to deliver on reliability, onboarding speed and proof, not just messaging | **Choose** |
| **D. Become a pure AI voice-agent company** | Market energy is there; a Saudi RFP, a bank project, and a US customer exist | AWS now sells its own AI agents (and bought NLX); "AI voice agent" is the most crowded claim in the category; the evidence shows about 6–8 deals and one delivered project, not a product-market fit | **Reject as the headline; keep as lane 2** |

## 3. The evidence behind the choice

*Evidence:*
1. **The connector is what keeps selling.** 36 of 88 deals mention it; almost every live 2025–26 thread is about it. (`03-hubspot-analysis.md` §1, §2.1)
2. **Trials convert to work.** Every connector deal traced in 2025–26 began with a trial or POC, and customers keep asking for extras on top: transcription, chat, Breeze AI transcripts, real-time transcription. (`03` §2.4)
3. **Buyers and AWS staff both ask for the same missing things:** a price, a clear trial path, proof, a cost estimate. (`03` §2.3, §4)
4. **The connector niche is crowded and price-compressed.** At least four vendors; ProUCX at $9–15 with a free trial; Odea at $24–35. (`04` addendum)
5. **AWS is moving upstream.** Amazon Connect became "Amazon Connect Customer" in April 2026, with 29 agentic-AI features announced at re:Invent 2025 and NLX acquired. (`04` addendum)
6. **OB's customers pay for engineer-led, in-your-account deployment** and get unhappy when renewals, licences and HubSpot changes are handled loosely. Trust is earned by operations, not slogans. (`03` §2.5, §2.6)
7. **The direct-sales business is small** (one account manager's 2025 sales about $42k). A small firm wins by being narrow and credible. (`03` §6)

*Inference (my judgement, not proven by the data):*
- The plain softphone connector will face continued price pressure, and HubSpot and AWS will keep adding native features. **OB should therefore price for a bundle, not a bare connector**, and prepare a second revenue line (AI/outbound for regulated sectors) that leans on skills competitors' listings do not show (Urdu/Arabic voice, bank integrations).
- Publishing prices helps more with AWS-referred and technical buyers (who cannot proceed without a cost estimate) than it hurts, because competitors' listings already expose their prices.

## 4. Audiences, ranked

Ranked by growth value to OB, with the evidence for the rank.

| # | Audience | Who exactly | What they need from the site | Evidence |
|---|---|---|---|---|
| **1** | **Amazon Connect + CRM teams** | Contact-centre or RevOps lead, HubSpot/Dynamics admin, AWS architect. 3–50 agents typical | Does it work with my CRM? What does it cost? What do I need? How fast is a trial? Will it break when HubSpot changes? | Bulk of 2025–26 deals; 75 pricing threads, 40 trial/POC threads |
| **2** | **AWS account teams and partner managers** | Amazon SAs, PDMs, ACE co-sell contacts | A one-page fact sheet: credentials, price basis, cost-estimate inputs, SoW template, how to register an opportunity | About 100 incoming Amazon messages; Snoonu, Kenya, TradeTracker, Middle East chat opportunities |
| **3** | **Existing customers** | Admins and agents at customers | Docs, status, renewals, contact for support, roadmap | Largest email theme is errors and issues; renewal admin; upsell fuel |
| **4** | **Regulated-sector buyers for AI voice and outbound** | Banks, fintechs, telecoms, retailers in Pakistan, the Gulf, South Asia and Africa | Evidence of delivery, language support, deployment options (on-prem/VM, in-region), integration list, security | One bank deployment across five use cases; Saudi RFP; Snoonu |
| **5** | **Partners and integrators** | Other AWS partners, integrators needing delivery capacity or a white-label connector | Terms, rate card basis, what OB delivers, how to start | About 41 partner threads; staff-augmentation engagement; cold outreach yields few replies, so a page beats emails |
| 6 | Candidates and procurement officers | | Careers list; company registration details | Low volume; footer only |

## 5. Positioning

**One sentence.** Octavebytes connects Amazon Connect to HubSpot, Microsoft Dynamics 365 and other CRMs, so every call, chat and text lands on the customer record, with transcripts and AI summaries, and deploys it into your own AWS account.

**Why believe us** (only claims the evidence supports):
1. It is in production with paying customers *(evidence: emails; permission needed to name any)*.
2. Engineers deploy it in your AWS account and stay on the thread *(emails)*.
3. AWS FTR certified; AWS Select Tier Services, Amazon Connect Service Delivery and Amazon Connect Ready partner *(Marketplace listing, existing site, emails)*.
4. Transparent price *(to be published; owner decision below)*.
5. Live on the AWS Marketplace and HubSpot Marketplace *(existing site, listing)*.

**What Octavebytes should be known for.** In two years, when someone using Amazon Connect asks "how do I get this into HubSpot (or Dynamics)?", the answer should be *Octavebytes*. Secondary reputation: **AI voice and outbound campaigns for banks and other regulated sectors in South Asia and the Gulf.**

**What the site should not try to be:** a general Amazon Connect consultancy, an agent-desktop vendor, a wallboard shop, a general dev-outsourcing agency, or an "AI company" in the abstract.

## 6. Commercial model to put on the site (proposal: owner decision)

Anchored on what OB actually quotes (modal $18; $15 discounts; $20 for small teams; a 2026 Dynamics quote with volume tiers), what competitors publish ($9–15 ProUCX; $24–35 Odea) and the add-ons customers actually request.

| Plan | Price | Includes | Anchor |
|---|---|---|---|
| **Core** | **$15** per agent per month | Softphone in the CRM, screen-pop (contact, company, deal, ticket), click-to-dial, automatic call logging and recordings, wrap-up codes, SMS, SSO | ProUCX Premium $15; OB's 2026 quotes $15–18 |
| **Plus** | **$20** per agent per month | Everything in Core, plus WhatsApp/social/chat channels, call transcription and AI summaries written to the CRM record | The 2026 feature bundle that one customer accepted at a $5 uplift; Odea's $24–35 |
| **Guided setup** | **$500** fixed, up to 20 agents, deployed with CloudFormation into your AWS account | Engineer-led | OB's actual $500 setup quote (2026) against $1,000–$5,000 for custom work |
| **Custom work** | From **$60/hour** or a fixed estimate | Extra fields, queue logic, custom integrations | Hourly quotes $40–75 |
| **Volume** | 50+ agents: talk to us | | Route101 tier quote (12–20) |

*Also disclose:* the connector runs in the customer's AWS account, so the customer pays AWS for its own hosting (OB quoted about $45–67 a month for a mid-size instance in one deployment) plus Amazon Connect usage. **Flag: confirm current hosting figures before publishing.**

## 7. Moves outside the website that the site depends on (I recommend; the owner decides)

These are not web design, but the site cannot deliver its promises without them.

1. **Make licence renewal automatic** (or move billing onto AWS Marketplace / HubSpot Marketplace), and send expiry warnings 14 and 3 days before. A customer's licence lapsed mid-use; another asked for auto-renew. *(Evidence: ISSI thread.)*
2. **Publish documentation** (deployment guide, requirements, FAQ) online instead of as email attachments, and a **status/changelog page** with a stated policy for handling HubSpot and AWS API changes. *(Evidence: dial-button and blank-record incidents.)*
3. **Change the AWS Marketplace listing to a public-price SaaS or metered product with a free trial** if AWS rules allow; today it is a professional-services listing with a "request private offer" button. Since 1 June 2026, new SaaS listings must support Concurrent Agreements. **I could not verify the listing's technical type; check in the seller console.**
4. **Connect the site to HubSpot** (HubSpot forms, tracking script, deal creation from the trial form) so the funnel can be measured. Nothing in Phase 1 can attribute a lead to a page today.
5. **Set up Google Search Console, GA4 goals and a HubSpot dashboard** *before launch* so migration effects can be measured.
6. **Record closed-lost reasons** in HubSpot on every lost deal.
7. **Reduce cold outbound "collaboration" email** (about 600 emails, roughly 55 replies) in favour of the partner and AWS pages plus targeted ACE co-sell.

## 8. Risks

| Risk | Likelihood / impact | Mitigation |
|---|---|---|
| A cheaper competitor makes the connector a commodity | High / High | Price for the bundle; lead with transcription and AI; add custom work and vertical AI as the moat |
| AWS or HubSpot ships a native integration | Medium / High | Position as the fastest route; keep AI/outbound lane alive; watch AWS announcements |
| Reliability incidents undermine the "trust" positioning | Medium / High | Docs, status page, change policy; keep support promise to what is actually staffed |
| Price transparency triggers pushback from existing customers on different rates | Medium / Medium | Grandfather existing customers for a period; never change price without notice |
| Proof cannot be obtained (customers decline) | Medium / High | Start permission requests now; use non-attributed "customer profile" format; use marketplace reviews |
| Contact-centre AI features overpromised | Medium / High | Publish only what runs in production today; label anything else "on request" |
| Claims on the current site that cannot be verified ("24/7 support", "300% efficiency") | High / Medium | Removed or marked `[CONFIRM]` in the new copy |

## 9. How to know it is working (no targets until a 60-day baseline exists)

| Measure | Why | Needs |
|---|---|---|
| Qualified trial requests per month | The homepage's job | HubSpot form + deal |
| Days from trial request to first live call | Onboarding friction is a recurring complaint | HubSpot deal properties |
| Trial → paid rate | The commercial outcome | HubSpot |
| Pricing-page → trial-form rate | Tests the price decision | GA4 |
| AWS-referred opportunities per quarter and share that ask for a cost estimate | Tests the AWS page | HubSpot source property |
| Marketplace private offers or subscriptions | Tests the marketplace route | AWS console |
| Support emails per active customer | Tests docs and status | Helpdesk/HubSpot |
| Organic clicks for "Amazon Connect HubSpot" family | SEO outcome | Search Console |

## 10. Decisions the owner needs to make

1. **Confirm the lane**: connector-first specialist, with AI/outbound for regulated sectors as lane 2. (Recommended.)
2. **Confirm the price card** in §6, or change it. Nothing in the copy goes live until this is decided.
3. **Confirm the trial terms**: 7 days, free, hosted by OB, then production in the customer's AWS account. (One 2026 trial was invoiced at $475 setup; the site says free.)
4. **Confirm what support OB can actually staff**, since the current site says "24/7". The copy says "Support included" with a `[CONFIRM]` on hours.
5. **Approve retiring products from the main nav** (§ IA): Agent Desktop, wallboard, MultiChat, Voice Recording, SCM, Queue Selection, QuickSight, Caller-ID, WhatsApp API, DevOps and Hiredeveloper, GoHighLevel and SuiteCRM as full pages.
6. **Decide the customers to ask for permission** (see proof plan) and who at OB asks.
7. **Confirm the office and phone facts** (US, UK, Pakistan; which numbers are live).
8. **Choose the domain for docs and status** (e.g. `docs.octavebytes.com`, `status.octavebytes.com`).
