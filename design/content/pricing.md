# Pricing  ·  `/pricing/`

> **Page job:** answer the most-asked question (75 threads asked it), in the open, and move the reader to the trial.
> **Every number here is a proposal.** `[CONFIRM: owner approval]`. See `../00-decision-and-strategy.md` §6 for the evidence behind the prices.

**Title tag:** Pricing: Amazon Connect for HubSpot & Dynamics 365 | Octavebytes
**Meta description:** $15 or $20 per agent per month, plus a $500 guided setup. What is included, what you pay AWS, and how to buy through AWS Marketplace.

---

# Pricing

Pay per agent, per month. You pay Octavebytes for the connector and AWS for Amazon Connect. No surprises.

## The connector

| | **Core** | **Plus** |
|---|---|---|
| **Price** | **$15** per agent per month | **$20** per agent per month |
| Softphone in HubSpot or Dynamics 365 | ✓ | ✓ |
| Screen-pop (contact, company, deal, ticket) | ✓ | ✓ |
| Click-to-dial | ✓ | ✓ |
| Automatic call logging and recordings | ✓ | ✓ |
| Pause/resume recording | ✓ | ✓ |
| Wrap-up codes | ✓ | ✓ |
| SMS | ✓ | ✓ |
| Single sign-on | ✓ | ✓ |
| WhatsApp and social channels | | ✓ |
| Transcripts, sentiment and AI summaries | | ✓ |
| Support | Included `[CONFIRM: hours]` | Included `[CONFIRM: hours]` |

**Guided setup: $500, fixed, up to 20 agents.** An engineer deploys the connector into your AWS account, configures screen-pop and matching rules, and stays with you until agents are taking calls. Larger teams and extra channels are quoted before we start.

**50 or more agents?** Volume pricing. [Talk to us]

**[Start a 7-day trial]**  ·  **[Buy on AWS Marketplace]**

## Try it first

Your **7-day trial** runs on our hosted environment, so you can test with real agents before anything is deployed in your AWS account. `[CONFIRM: free; a 2026 trial was invoiced as setup. Decide and state one rule]`

## What you pay AWS

The connector runs in your AWS account, so AWS bills you directly for:

- **Amazon Connect**: usage-based, per minute of voice and per message. [AWS pricing →] [AWS Pricing Calculator →]
- **Phone numbers and carrier charges**
- **Contact Lens** (only if you want transcripts and sentiment)
- **The connector's hosting resources**: a small instance. In one 2026 deployment sized for about 20 agents, we estimated **about $45–$67 per month**. `[CONFIRM: current figures and sizing guidance]`

Not sure what your total will be? Our guide **[What does Amazon Connect plus HubSpot cost?]** walks through it, and we will build the estimate with you.

## Custom work

| | |
|---|---|
| Extra fields, queue logic, integrations | Fixed estimate, or **$60 per hour** `[CONFIRM: 2026 hourly rate quoted as $60, discounted to $50]` |
| Real-time transcription, custom chat behaviour | Scoped and quoted |

## Other products

| | |
|---|---|
| Outbound campaigns and voice AI | Quoted per project. [Banking and regulated voice →] |
| Wallboard for Amazon Connect (Octave Vision) | `[CONFIRM: currently sold? $10 per supervisor per month quoted in 2025]` |

## Buying options

- **AWS Marketplace.** Counts toward your AWS commitment and uses AWS billing. `[CONFIRM: public price or private offer. See decision memo §7]`
- **HubSpot Marketplace.**
- **Direct invoice.** Monthly, or quarterly in advance.

## Questions

**Is there a contract?**
`[CONFIRM: terms. Suggested public wording: "Month to month. Cancel with 30 days' notice." Publish only what OB will honour.]`

**What if we grow or shrink?**
You are billed for the agents you license each month. Change the number with 30 days' notice. `[CONFIRM]`

**Will the price change?**
We give 60 days' written notice of any price change. Existing customers keep their current price during that notice period. `[CONFIRM: OB should commit to this. Two 2026 price discussions, including a 50% proposed increase, caused friction]`

**How do renewals work?**
`[CONFIRM once automated: "Renews monthly. We email you 14 days and 3 days before any change, so your agents never lose access unexpectedly."]`

**Do you offer discounts?**
For 50+ agents, and for annual or quarterly prepayment. `[CONFIRM: rates]`

**Do you compare yourselves to other connectors?**
Yes, in our guide **[Amazon Connect and HubSpot: your integration options compared]**. It covers what to ask any vendor. It does not quote competitors' prices.

---

### Final call to action
**[Start a 7-day trial]**  ·  **[Get a cost estimate for your team]** (`/start-trial/?intent=estimate`)

*Schema:* `Offer` for each plan (priceCurrency USD, unitText "per agent per month"), `FAQPage`.
