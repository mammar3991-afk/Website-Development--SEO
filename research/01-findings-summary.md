# Phase 1 findings: summary

> **INTERNAL.** Contains names from private CRM and email records. Not for publication. Detail: [live site audit](02-live-site-audit.md) · [HubSpot analysis](03-hubspot-analysis.md) · [competitor scan](04-competitor-scan.md) · [URL inventory](data/url-inventory.csv).

## The short version

**Octavebytes is a small software vendor whose real product is one connector: it links Amazon Connect (Amazon's cloud call-centre system) to a company's CRM, mainly HubSpot, and it charges per agent per month.** The current site presents it as a broad Amazon Connect consultancy with about 30 products and no prices, no named customers and no way to start without a call.

## What the evidence says the business is

1. **The connector is the business.** 36 of 88 deals are "CTI Connector" deals. Nearly every commercially live email thread in 2025–26 is a HubSpot connector trial, licence, renewal or support issue. The freelance AWS work of 2021–23 (about 25 small deals) is where the company began, not what it is.
2. **Buyers already own both systems.** They run Amazon Connect and use HubSpot (or Dynamics 365 or GoHighLevel). They want the missing link.
3. **It is a low-ticket, high-touch business.** Typical connector customers have 3–20 agents at roughly $15–20 per agent per month, plus a $500–$5,000 setup fee. Each sale is a small recurring amount that takes a lot of human effort.
4. **There are four ways in.** Direct (existing Amazon Connect customers), **AWS-referred** (Amazon staff pass opportunities; about 100 incoming messages), **partner/subcontract**, and **Marketplace** (AWS Marketplace and HubSpot Marketplace listings). Cold outbound to other partners is a large part of email volume but produces few replies.
5. **A newer stream is AI voice, robocall and banking campaigns**, mainly via relationships in Pakistan and the Gulf.

## What surprised me, and what contradicts the current site

| # | Finding | Site says | Evidence says |
|---|---|---|---|
| 1 | **Prices exist** | "Flexible pricing", no numbers | About 83 quoted prices: usually **$15–20 per agent per month**, with drift from $10 to $30. Competitors publish **$9–$15 (ProUCX) and $24–$35 (Odea)**, so $15–20 is mid-market, not cheapest |
| 2 | **The "free trial" is not self-serve** | "7 days free trial" | A call, then an engineer deploys into the customer's AWS account, using details emailed to OB. One customer's rollout is at 146 messages and four months and is not in production |
| 3 | **The site is invisible to the CRM** | n/a | About 1,436 contacts, 1,428 "Offline". Forms are Contact Form 7 emails. No HubSpot tracking or forms in the pages I checked. One live form sends emails titled `[your-subject]` |
| 4 | **Three posts are buried in spam** | n/a | **11,543** injected comments (escort, casino and similar), 3–5 MB per page |
| 5 | **The strongest credential is missing** | "Select Tier", "Service Delivery", "Ready" | The AWS Marketplace listing says **"AWS FTR Certified"**. The site never mentions it |
| 6 | **Proof is anonymous** | Case studies without customers or numbers | Buyers ask for references in about 32 threads; competitors show logos, numbers and badges |
| 7 | **The homepage does not lead with the money product** | Agent Desktop, Amazon Connect, DevOps | HubSpot connector is the revenue line; Agent Desktop and Octave Vision appear in almost no recent deals |
| 8 | **AWS staff are a top audience with no page** | "Become a Partner" (no terms) | AWS SAs and partner managers ask for **cost estimates, SoWs and funding routes**, and refer customers |
| 9 | **The biggest post-sale pain is renewal and reliability** | "24/7 Octave Standard Support included" | Licence keys expire by hand (one customer's licences stopped mid-use); a HubSpot change broke the dial button once; no docs, status page or changelog |
| 10 | **Contact facts disagree across pages** | n/a | Three phone formats or numbers, UK address present or blank, "Europe, Middle East and Asia" vs "USA and Asia" |
| 11 | **Government-procurement page is a top-level nav item** | SAM.gov IDs published | No government deal in the CRM |
| 12 | **The connector niche is crowded and price-compressed** | n/a | At least four vendors sell Amazon Connect ↔ CRM connectors; the cheapest lists **$9–15 with a 14-day free trial** on AWS Marketplace. Named contact-centre giants (Five9, Talkdesk, Genesys) barely appear in email |

## Confidence and gaps

- **High:** what the site says and lacks; the product mix; the price ranges; the manual sales and onboarding process; AWS-referral behaviour.
- **Medium:** segment sizes and geographies (CRM is messy; one in nine deals is junk, amounts often blank, no loss reasons recorded). Loss analysis rests on three or four cases.
- **Not available to me, and needed:** Google Search Console (what people actually search and land on), GA4 (behaviour and conversion), backlink data (what to protect in a migration), Core Web Vitals, HubSpot Marketplace and AWS Marketplace sales data, and total company revenue. I have one account manager's 2025 sales figure (about $42k) and no company total.
- **Competitor scan:** six sites read once each through a summariser; no pricing pages beyond Odea's; no traffic or ranking data.

## What this implies for Phase 2 (superseded by the decision memo in `../design/00-decision-and-strategy.md`, which also corrects the competitor picture)

- Make the **Amazon Connect ↔ CRM connector** the centre of the site and the homepage's single job: get an existing Amazon Connect customer to a working trial.
- **Publish prices**, and make the Marketplace listings visible (but not as a race to the bottom: see the decision memo).
- Build **proof in a permission-first way**, starting with the customers who are already in production.
- Give **AWS staff** and **partners** each their own short, factual page.
- Cut the catalogue to what the evidence supports; redirect the rest.
- Fix the site's hygiene (spam, H1s, forms → HubSpot) before or with the redesign.

Phase 2 followed after review of this summary; see `../design/`.
