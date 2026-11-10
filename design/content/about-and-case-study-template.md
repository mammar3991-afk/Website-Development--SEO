# About and case-study template

---

# 1. About  ·  `/company/about/`

> **Page job:** tell a cautious buyer who is behind the product, and why to trust them with production calls. Today's About page is a slogan collection; this one is about people, place and track record. **Names, photos and biographies require each person's permission.**

**Title tag:** About Octavebytes | Amazon Connect Specialists
**Meta description:** A small team of AWS engineers connecting Amazon Connect to the CRMs businesses already use. Offices in the USA, UK and Pakistan.

# About Octavebytes

We connect Amazon Connect to the CRM your team already uses.

## What we do
We build and support software that puts the Amazon Connect softphone inside HubSpot and Microsoft Dynamics 365, and we build outbound-call and voice-AI systems for banks and other regulated businesses. Our engineers deploy everything into your own AWS account and stay with you until it works.

## How we got here
`[PROOF NEEDED: founding year and story, in the owner's words. What the records show: the team began doing Amazon Connect, Salesforce and AWS project work for clients around 2021–22, then turned the most-requested piece, connecting Amazon Connect to a CRM, into a product. Confirm before publishing.]`

## What we believe
**We tell you what things cost.** Our prices are on the pricing page.
**We show our work.** Deployment steps, requirements and changes are documented in public.
**We stay with you after go-live.** Support is part of the subscription.
**We say no when it is not a fit.** If we cannot do something well, we will say so.
`[CONFIRM: each statement must describe how OB actually behaves; delete any it cannot stand behind]`

## Credentials
- AWS Select Tier Services Partner
- Amazon Connect Service Delivery Partner
- Amazon Connect Ready Partner
- AWS FTR-certified Amazon Connect connectors, on AWS Marketplace
- HubSpot Marketplace app; HubSpot Technology Partner `[CONFIRM: tier]`
- Microsoft AppSource listing (Dynamics 365 connector)
- US federal contractor registration (SAM.gov) [Government information →]
`[CONFIRM: every badge has current status and usage permission]`

## The team
`[PROOF NEEDED: 4–6 people with name, role, photo and one-line background, each with permission. Likely roles: CEO, co-founder for business development, solutions and engineering leads, account manager. Show the engineers customers actually talk to.]`
`[CONFIRM: team size and AWS certification count. The old site claims "AWS-certified solution architects" without numbers]`

## Where we are
| Office | |
|---|---|
| **USA** | McKinney, Texas |
| **UK** | London |
| **Pakistan** | Lahore (engineering and support) |
`[CONFIRM: which offices are staffed and what each does]`

## Work with us
**[Start a 7-day trial]**  ·  **[Talk to us]**  ·  **[Careers]**

---
---

# 2. Case-study template  ·  `/customers/[slug]/`

> **Purpose:** one repeatable format that produces evidence, not a brochure. It forces the fields buyers and AWS staff ask for, and it makes the permission status explicit.

## Permission block (internal; not published; stored in HubSpot on the case-study record)

| Field | Value |
|---|---|
| Customer legal name | |
| Customer contact who approved | |
| **What is approved** | ☐ Name  ☐ Logo  ☐ Industry and size only  ☐ Quote  ☐ Metrics  ☐ Photo |
| **Approval evidence** | email or signed form, stored and dated |
| Review date | 12 months from approval; re-confirm or take down |
| **Anonymous fallback** | ☐ Approved to publish as "a [industry] company in [region]" |

**No case study is published without at least "Industry and size only" ticked. A quote, a metric or a logo needs its own tick.**

## Page structure

**Title tag:** `[Customer or "A {industry} company"]: {outcome} with Amazon Connect and {CRM} | Octavebytes`

# {Headline that states the outcome}

**At a glance** (a fixed sidebar)
| | |
|---|---|
| Customer | Name/logo, or "Financial services, Pakistan" |
| Size | Agents, sites |
| CRM and Amazon Connect setup | |
| Product | Which Octavebytes product |
| Time to go live | trial start → first live call |
| Delivered | month and year |
| Result | one measured line `[PROOF NEEDED]` |

## The situation
Two to four sentences. What was the team doing before? What was breaking?

## What we built
Short, specific, in plain language. Screenshot or diagram of the actual solution.

## How the project ran
Trial dates, deployment method (CloudFormation or manual), what the customer's team did, what went wrong and how it was fixed. **Include one real problem.** Buyers trust a case study that admits something.

## Results
Measured numbers **from the customer**, with their definition and date range. If no number is approved, say what changed qualitatively and do not invent a percentage.

## In the customer's words
Quote, name, role. Written approval attached.

## What they use now
Links to the product page, pricing and docs.

**[Start a 7-day trial]**

*Schema:* `Article` with `about` and, if named, `Organization`.

---

## Seed case study: the bank fraud-verification project (draft from public text)

**Status:** the existing public page is anonymous and already live; it can be republished in this template with no new claim. To name the bank or add numbers, follow the permission block.

**Headline:** Real-time fraud verification calls for a leading bank in Pakistan
**At a glance:** Financial services · Pakistan · Amazon Connect · Octavebytes Campaign Management and robo-call system · Delivered 2026 (deployment confirmed complete in April 2026)
**Situation:** As digital payments grew, the bank needed to verify suspicious card, e-commerce, interbank, instant-payment and bill-payment transactions without adding manual work for agents.
**What we built:** An outbound robo-call system connected to the bank's fraud risk system. It triggers an automated, personalised call in Urdu or English, asks the customer to press 1 to confirm or 2 to report fraud, retries when the call is not answered, and returns the result to the fraud system in real time.
**How the project ran:** `[PROOF NEEDED: bank's permission to describe: integration with a fraud system and a gateway; the bank supplied a virtual machine; we deployed and tested five use cases]`
**Results:** `[PROOF NEEDED: measured results such as calls per day, verification rate, time to block. None are on the current page]`
**Quote:** `[PROOF NEEDED]`
