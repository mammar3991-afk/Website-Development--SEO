# Conversion plan

**Goal:** turn ready buyers into HubSpot deals with less back-and-forth, and make the funnel measurable for the first time.

## 1. What visitors should do

| Priority | Action | Audience | Where |
|---|---|---|---|
| **1** | **Start a 7-day trial** | 1 (Amazon Connect + CRM teams) | Header button on every page; end of every product page; `/start-trial/` |
| 2 | **See pricing → get a cost estimate** | 1, 2 | `/pricing/`, `/start-trial/?intent=estimate` |
| 3 | **Buy on AWS Marketplace / HubSpot Marketplace** | 1 | Product and pricing pages |
| 4 | **Send an opportunity** (AWS teams) | 2 | `/partners/aws/` |
| 5 | **Talk to us about a regulated-sector project** | 4 | Banking page |
| 6 | **Partner enquiry** | 5 | `/partners/` |
| 7 | **Contact support** | 3 | Contact page, docs |

The old site had one call to action, "Request a Demo", on every page, for every audience.

## 2. What a self-serve buyer needs

A buyer who wants to evaluate before talking to anyone needs seven things. Today, none is on the site.

| Need | Delivered by | Status |
|---|---|---|
| A price | `/pricing/` | Copy written; needs owner approval |
| Whether it works with my setup | Product page + requirements list | Copy written |
| What I must provide to try it | Requirements list (instance ID, region, recording bucket, admin) | Copy written; taken from real onboarding emails |
| How deployment works | Docs + diagram | **Docs need building** |
| Proof it is safe and reliable | Security page, status page, changelog | **Need building** |
| A way to try it without a sales call | Trial form → hosted trial | Form copy written; **hosted-trial process must be defined** |
| A way to buy without a sales call | AWS/HubSpot Marketplace, later direct checkout | Listings exist; **public-price listing recommended** |

**Reality check.** The trial is not instant, because an engineer deploys it. The honest promise is "**a trial opened for you within one business day**" `[CONFIRM]`, not "instant".

**Three stages toward true self-serve** (product work outside the website):
1. **Launch:** form-triggered hosted trial, requirements checklist, marketplace links. *(Website work only.)*
2. **Next:** scripted trial provisioning, automated licence keys and renewal, a customer portal. *(Removes the manual key emails that caused a lapse.)*
3. **Later:** AWS Marketplace SaaS/metered listing with public price and free trial (the route ProUCX uses). *(Confirm listing type in the AWS console first.)*

## 3. How leads reach HubSpot

### Today
Contact Form 7 emails a notification; no HubSpot form or tracking script; the CRM shows almost every contact as "Offline".

### Design
**All forms post to HubSpot** (embedded HubSpot forms, or a custom form using the HubSpot Forms API) and **the HubSpot tracking script is installed** with consent. Then:

| Form | Properties captured | Workflow |
|---|---|---|
| **Trial** | name, email, company, `crm_used`, `connect_status`, `aws_region`, `agent_band`, `channels`, message, hidden: `source_page`, UTM fields, referrer | Creates contact + company + **deal** in **New Lead**; owner assigned round-robin; instant email to sales; auto-reply with requirements checklist and calendar link |
| **Estimate** | as above + telephony notes | Same, tagged `intent = estimate` |
| **AWS opportunity** | customer name, CRM, agents, timeline, AWS contact (optional), ACE ID (optional) | Deal with `lead_route = AWS-referred`; notify partner lead |
| **Regulated-sector** | organisation, sector, country, use case, systems to integrate, timeline | Deal with `lead_route = Direct`, product = Voice/Outbound; notify the owner |
| **Partner** | company, AWS tier, type (refer/resell/capacity), message | Company + contact; task for the partner lead |
| **Contact / support** | topic, message | Support goes to the helpdesk address; sales topics create a lead |

**New HubSpot properties** (deal): `lead_route` (Direct / AWS-referred / Partner / Marketplace / Outbound), `product_interest`, `agent_band`, `connect_status`, `trial_start_date`, `first_live_call_date`, `closed_lost_reason` (**make required when a deal is closed lost**).
**Deal name convention (keep the existing pattern):** `{Company} – {Product}`.
**Pipeline mapping (existing stages):** form submitted → *New Lead*; trial opened → *Demo/POC scheduled*; pricing sent → *Contract & Commercials sent*; and so on. The legacy "Closed-Paid" stage is retired from the live pipeline.

### Response standard
`[CONFIRM: internal commitment]` First reply within one business day. If the requirements checklist has not come back after 3 days, offer a call. **Stop chasing after three follow-ups with a polite close-out that asks for the reason.** (One 2026 prospect received about seven chasers over six weeks.)

## 4. The trial flow, step by step

1. **Form submitted.** Confirmation page shows the checklist.
2. **Auto email (immediately):** the same checklist, the calendar link and the docs link.
3. **Day 1:** engineer replies, confirms the setup and opens the hosted trial.
4. **Day 3:** if instance details are still missing, offer a 30-minute call.
5. **Day 6:** "Your trial ends tomorrow. Want to extend or go live?"
6. **Day 8:** short feedback question and, if they want to continue, the price and setup quote.
7. **Production:** deployment via CloudFormation, with a named engineer.
8. **Day 30 after go-live:** check-in and a **permission request** (see proof plan).

## 5. Tracking and measurement

**Set up before launch (so the change can be measured):** HubSpot tracking, GA4 (existing property), Search Console, a 28-day baseline export of the old site.

**GA4 events**

| Event | When |
|---|---|
| `cta_click` (with `location`, `label`) | Any trial/pricing/marketplace button |
| `form_start`, `form_submit` (with `form_id`, `intent`) | Each form |
| `pricing_view` | Pricing page loaded |
| `docs_click` | Link to docs |
| `marketplace_click` (`aws` or `hubspot`) | Marketplace buttons |
| `estimate_request` | Estimate form submitted |
| `partner_enquiry`, `aws_opportunity` | Those forms |

**UTM policy:** every campaign and email link uses `utm_source`, `utm_medium`, `utm_campaign`. The AWS Marketplace and HubSpot Marketplace listing links carry their own `utm_source` so their clicks are countable.

**Dashboard (HubSpot):** trial requests by source and page · request → trial → paid rates · days to first live call · leads by `lead_route` · lost reasons.
**Weekly review for the first 8 weeks**, then monthly. **Set targets only after 60 days of baseline data.**

## 6. Friction to remove from today's site

| Today | New |
|---|---|
| One CTA ("Request a Demo") | Trial, pricing, marketplace; each with a clear purpose |
| "Your Name / Email / Phone / Message" | Short structured form that captures what the engineer needs |
| Pre-bundled SMS consent in the contact form | Consent is separate and unticked |
| Form emails titled `[your-subject]` | Subject built from the topic |
| Phone numbers that differ by page | One number, one address block |
| Live chat that produced "missed chat" emails | Only if staffed; otherwise a form |
| Broken cookie banner | Working banner with real category text |
| No price | Price card |
| Attachments emailed after the call | Public docs and checklist |

## 7. Later tests (only after baseline traffic exists)

- Hero button text: "Start a 7-day trial" versus "Try it with your agents".
- Price shown as monthly per agent versus annual total for a sample team.
- Requirements checklist above versus below the form.
- Whether a short screencast raises trial requests.
