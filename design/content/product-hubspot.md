# Amazon Connect for HubSpot  ·  `/products/hubspot/`

> **Page job:** convince a HubSpot admin or contact-centre lead that this connector fits their setup, and move them to the trial.
> Replaces `/hubspot-cti-connector/` (301). Feature statements come from the current site and the AWS Marketplace listing.

**Title tag:** Amazon Connect HubSpot Integration | Octavebytes
**Meta description:** Embed the Amazon Connect softphone in HubSpot. Screen-pop, click-to-dial, automatic call logging and recordings. From $15 per agent per month. Try it for 7 days.

---

# Amazon Connect for HubSpot

Answer calls in HubSpot. Every call is logged on the contact, company, deal or ticket. It works with the Amazon Connect instance you already run.

**[Start a 7-day trial]**  **[See pricing]**  **[View on HubSpot Marketplace]**

AWS FTR-certified · Listed on AWS Marketplace and HubSpot Marketplace

---

## What agents can do without leaving HubSpot

**Take inbound calls.** The Amazon Connect Contact Control Panel runs inside HubSpot. Answer, hold, resume, transfer, mute and conference from the same window.

**Know who is calling.** On arrival, the matching contact, company, deal or ticket opens. Two records share a number? The agent chooses. No match? They create the record without leaving the call.

**Call out with one click.** Click any phone number in HubSpot to dial.

**Log every call automatically.** Each call becomes a HubSpot activity linked to the right record, with direction, duration and the recording.

**Control recordings.** Agents can pause and resume recording during sensitive moments, and listen back from the call activity.

**Close the loop with wrap-up codes.** Outcomes are captured the same way on every call, so reports stay comparable.

**Text and message from the record.** Click-to-send SMS and WhatsApp. *(Plus plan)*

**Read the conversation later.** Transcripts, sentiment and AI summaries are written to the record. *(Plus plan; see [Call intelligence](/products/call-intelligence/))*

---

## Set it up your way

Different teams want different behaviour, so the connector is configurable:

- **Contact-based, company-based or deal-based** flows: choose which HubSpot object opens on arrival and which one the activity attaches to.
- **Matching rules** for multi-match and no-match numbers.
- **Single sign-on** with Google Workspace. `[CONFIRM: other identity providers; one 2026 customer requested SSO configuration]`
- **Custom queue logic and fields** on request. [Custom builds →]

---

## How it deploys

The connector runs **in your AWS account**, so your recordings and Amazon Connect data stay where they already are.

**You provide:**
- Your Amazon Connect **instance alias, instance ID and region**
- The **S3 bucket** where Amazon Connect stores call recordings
- A **HubSpot Super Admin** to approve the connection (they do not need to give us access)
- Someone on your side with rights to run a **CloudFormation template** in your AWS account

**We provide:**
- A CloudFormation template (recommended), or a manual step-by-step guide with a remote session
- A trial on our hosted environment first, so you can test with real agents before touching production
- Engineers on the thread until your agents are taking calls

Deployment guide, requirements and FAQ: **[Read the docs →]**  `[LINK: docs.octavebytes.com. Publish before launch]`

---

## What it costs

| | Core | Plus |
|---|---|---|
| Per agent per month | **$15** | **$20** |
| Softphone, screen-pop, click-to-dial | ✓ | ✓ |
| Call logging and recordings, wrap-up codes | ✓ | ✓ |
| SMS | ✓ | ✓ |
| WhatsApp and social channels | | ✓ |
| Transcripts and AI summaries | | ✓ |

**$500** fixed guided setup for up to 20 agents. You pay AWS separately for Amazon Connect usage and the small resources the connector runs on. [Full pricing and FAQ →]

---

## Common questions

**Do you support HubSpot Sales Hub, Service Hub and Marketing Hub?**
`[CONFIRM: which hubs and editions have been tested; state them exactly]`

**Does it work with HubSpot's own calling and Breeze AI?**
It writes calls and transcripts to HubSpot records, and can place transcripts in Breeze AI fields. `[CONFIRM: current status. A 2026 deployment requested this; state only what is live]`

**Can our agents use it in the browser?**
Yes; the softphone runs in the browser tab. `[CONFIRM: Chrome extension status. One customer was told it was under Google review in May 2026]`

**What if my number of agents changes?**
Pay per agent per month. Add or remove agents with 30 days' notice. `[CONFIRM: terms]`

**How do licences renew?**
`[CONFIRM: once automated renewal exists, write: "Renews automatically each month. We email you 14 days and 3 days before any change."]` Until then, do not promise it.

---

### Final call to action
**Try it with your agents for 7 days.**
**[Start a 7-day trial]**  ·  Prefer AWS billing? **[Buy on AWS Marketplace]**

---

*Schema:* `SoftwareApplication` (name, applicationCategory "BusinessApplication", offers with the two prices) + `FAQPage`. Add breadcrumb markup.
