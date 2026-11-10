# HubSpot analysis: what the business really is

> **INTERNAL. Not for publication.** This file names companies from private CRM records and email correspondence. It contains no credentials (customers pasted several into emails; they are referred to here only by type). Nothing here may go on the public site without permission (see the proof plan in Phase 2).

## How this was done

| Source | Volume | Method |
|---|---|---|
| Deals | 88 records (all of them) | Pulled in full, read by hand |
| Emails | 5,924 records in HubSpot; all 5,924 analysed (2,247 incoming, 3,677 outgoing) | Downloaded to local files, quoted history stripped, credentials redacted, grouped into 688 threads by normalised subject (there is no thread ID), then read thread by thread |
| Contacts / companies | about 1,436 contacts, several hundred companies | Aggregate queries |

Raw email text was kept outside the project folder.

**Limits on this data.**
- Roughly one in nine deal records is junk or test data ("Dummy Deal", "Demo Deal", "Call - +92…").
- Amounts are often blank.
- `closed_lost_reason` and `closed_won_reason` are not populated anywhere, so win/loss reasons come from email, not from the CRM.
- "Closed-Paid" is a legacy stage holding 27 old freelance jobs.
- 392 of the 2,247 "incoming" emails are from Octavebytes addresses (internal threads and CCs). They were excluded from customer counts.
- Conclusions are directional, not statistical.

---

## 1. What the deals say

**88 deals: 18 Closed won, 27 Closed-Paid (legacy), 16 Closed lost, 27 open, and the remainder junk.**

| Cluster | Deals | Notes |
|---|---|---|
| **"…CTI Connector" (HubSpot, MS Dynamics, GoHighLevel)** | **36 of 88** (14 of the 45 won or paid, 9 of the 16 lost) | The one product family that appears in every year from 2021 to 2026 |
| Upwork-era freelance work (Amazon Connect admin, AWS Lambda, Kinesis, Salesforce click-to-dial, DevOps) | about 25 | Created 2021–23, all small ($32–$1,350), sitting in the "Closed-Paid" stage (27 deals; two of them are recent payment records). This is where the company started. It is history, not the business |
| AI voice agent / robocall / voicebot / SMS configuration | about 6–8 | New in 2026, mostly through existing referral customers (a bank in Pakistan, a US e-commerce customer, a Saudi telecom integrator) |
| Amazon Connect implementation | about 6 | Snoonu chat (lost, $15k), Cyanergy (lost), Ruff Greens (won, $2k), Salesforce integration ($500) |
| Agent Desktop, wallboard, other | 3–4 | Rare |

**Deal source (self-reported field):** Website 28, Upwork 11 (all won or paid), Referral Client 11, Email Marketing 1, Social 1, unassigned 36. The "Website" value is set by hand. The tracking data disagrees: nearly every deal has `hs_analytics_source = OFFLINE` (see §3).

**Deal size.**
- A typical won deal is tiny (about $500–$1,500).
- The large ones are project-plus-licence bundles: $36,000, $9,823, $6,480, $5,400.
- The most recent wins are $100–$2,500 monthly subscriptions or small change requests.
- Biggest losses: $50,000 (Member Solutions), $15,000 (Snoonu, Amazon Connect chat), $7,100 and $6,000 (early MS CRM connector deals).
- **This is a low-ticket, high-touch business.** Each connector customer is worth roughly (agents × about $15–20 × 12) a year. For 3–20 agents that is $540–$4,800 a year.

**Customer geographies (won or active).** Australia (Sony, ITKnocks, Zeller, an energy initiative), United States (several), Mexico, the Netherlands, Pakistan (a bank), South Africa and Australia (a payments company), UK and Italy (POCs), Saudi Arabia and Qatar (AI and Amazon Connect prospects). CRM company records: US 200, UK 44, Australia 43, India 38, Germany 34, UAE 14.

**2026 pipeline (open).** Mostly HubSpot connector trials and POCs: a BPO, a marketing services firm, a fintech, a software firm, a printing company, and a Latin American delivery company. Also an MS Dynamics connector POC and two AI voice deals.

## 2. What emails say

### 2.1 The real product is the Amazon Connect ↔ CRM connector, sold per agent per month

Almost every commercially live thread in 2025–26 is about the HubSpot CTI Connector (POCs, licences, renewals, support), with the MS Dynamics 365 and GoHighLevel connectors behind it. Buyers are **companies that already run Amazon Connect and use HubSpot** (or Dynamics or GoHighLevel). They are not searching for a contact centre. They are searching for the missing link between two systems they already own.

### 2.2 Pricing exists, but only in email, and it is inconsistent

Extracted from 83 distinct outgoing price statements, 2022–2026 (customer names removed):

| Item | What was quoted |
|---|---|
| HubSpot connector, per agent per month | **$10 → $12 → $14 → $15 → $17 → $18 → $20 → $21 → $24** depending on year, agent count and who was asking. Most common in 2025–26: **$18** (quoted to at least 6 different buyers in 2026) and **$15–20** |
| Volume tiers (one 2026 MS Dynamics quote) | under 100 agents $20; 100–500 $18; 500–1,000 $15; 1,000+ $12 |
| GoHighLevel connector | $25–30 per agent per month (small teams) |
| One-time setup / professional services | $500 (trial setup), $1,000–$2,000 typical, up to $3,000–$5,000 for larger jobs |
| Extra channels (2024 quote, Amazon Connect chat/social) | $5 per agent per channel per month plus $1,500 one-time per channel |
| Agent Desktop | $15 per agent per month |
| Wallboard | $10 per supervisor per month |
| Custom work | $40–75 per hour, or about $2,500 per engineer per month (staff augmentation) |
| Free trial | 7 days |

Three things stand out.
1. **Buyers notice the drift.** One wrote "I thought the price was $18". Another pushed back hard on a 50% rise on an existing contract, noting the HubSpot integration was "nice to have" and that some features are native to Amazon Connect.
2. **Discounting is the default lever** (a "massive discount" to $15 for everyone who had run a POC; a pilot cut from $18 to $15 for a large delivery company in exchange for quarterly upfront billing).
3. **The competitor sets a higher public price.** See the competitor scan (Odea, $24–$35).

The website says "Flexible pricing" and "7 days free trial" but shows no numbers anywhere. The AWS Marketplace listing says "Custom pricing… request a private offer".

### 2.3 What leads ask

Keyword scan across 1,855 external incoming messages. "Threads" = distinct subjects (of the ~330 that had an outside reply) whose incoming messages mention the theme. The patterns are broad regexes, so counts are indicative, not exact.

| Theme | Threads mentioning it | Reading |
|---|---|---|
| Errors / not working / issues | about 100 (broad pattern; includes ordinary uses of "issue") | The largest theme by far. Post-sale friction dominates the inbox |
| Pricing, cost, quote, commercials | 75 | Asked early and often |
| Partner / reseller / referral / commission | 41 | Big second channel (see §4) |
| Trial / POC / pilot | 40 | Buyers want to try before they commit |
| AI / voicebot / transcription / Bedrock | 35 | Rising in 2026 |
| SIP trunk / carrier / DID / caller ID | 35 | Telephony plumbing is a recurring blocker |
| Invoice / payment | 35 | Manual billing |
| License / renewal | 32 | Licence keys are managed by hand |
| Case study / reference | 32 | Buyers ask for proof |
| Demo | 30 | |
| Security / compliance | 21 | |
| Competitor names (Aircall, Talkdesk, Five9, Genesys…) | 9 | Named competitors almost never come up. The competition is "do nothing", "native AWS", or "buy a different phone system" |

### 2.4 What wins deals

Read from the threads that closed or advanced. Items marked *(inferred)* are my reading of the pattern, not something a customer said.
- **A working trial or POC, usually deployed into the customer's own AWS account.** Every 2025–26 connector deal I traced (a payments company, a software firm, a printing company, a fintech, an insurance-services firm) began with a trial or POC. It is the standard route to a sale.
- **Fast access to an engineer.** Customers repeatedly asked for calls with the engineer and thanked them by name when issues were fixed *(inferred: the human onboarding is a selling point as well as a cost)*.
- **AWS staff vouching for OB.** Snoonu, a Kenya opportunity, a Dutch marketing company and a Middle East start-up all reached OB through Amazon contacts. In one, the Amazon SA said the customer's questions were all answered.
- **A low price** *(inferred: OB quotes $15–20 against $24–35 published by the main competitor, and buyers rarely haggled beyond the first discount)*.
- **Customisation on top of a standard product.** A software firm asked for real-time call transcription; an insurance-services customer was offered it; a payments customer received added chat, transcription and AI summary.
- **Marketplace links** sent after demos, so the buyer can purchase through AWS or HubSpot billing.

### 2.5 What loses deals, and what damages them

**Traced losses (thin: three cases).** A US restaurant-tech firm (2022) declined after a POC and gave no reason when OB asked. A fintech (2026) ran a 3-agent production POC, then wrote twice that it would "follow a different path". A technology group went quiet after a demo and the price quote: at least three follow-ups over five weeks with no answer. A US health-tech firm's deal was also closed lost in September 2026 with no reason recorded. **None of the traced losses cited price**, and none gave a reason at all.

**Friction that did not cause a loss but put customers at risk** (customers stayed, at least so far):
- **Price rises on existing customers.** Zeller: 50% proposed, halved after protest.
- **Reliability incidents tied to HubSpot changes:** the dial button stopped working; a blank record opened on call arrival; calls were logged against "Unknown User".
- **Licence expiry with no warning.** ISSI Corp's paid licences stopped working right before calls to C-level executives. The customer wrote "very concerning" and asked for automatic renewal.
- **Slow enterprise procurement.** Rappi: MSA sent 6 April, still in review on 11 May while the pilot was already live for 20 agents and the invoice contact was still unresolved.
- **Long onboarding.** Foxit: 146 messages, May to September, still not in production.

The CRM does not capture loss reasons, so none of this is countable. With so few traceable losses I would **not** claim "price is not the issue"; I would say the data does not show price as the stated reason, and that **onboarding friction, slow follow-up and renewal admin are the recurring complaints**.

### 2.6 How the sale really works today (a 5-step manual process)

1. Form or email arrives ("New message from octavebytes website" is the subject of the notification).
2. Account manager replies and books a call (a Google Calendar link).
3. Demo → 7-day trial. Customer sends AWS Connect instance details (instance ID, region, recording bucket) and the HubSpot URL by email.
4. A deployment guide goes as an **email attachment**; an engineer deploys the connector into the customer's AWS account.
5. Licence key issued by email. Monthly renewal by email. Invoice by email.

There is no self-serve path, no online documentation, no status page, no changelog, no licence portal.

## 3. Website → HubSpot: the site is invisible to the CRM

- About **1,436 contacts**, of which **1,428 have Original Source = "Offline Sources"**. Only 8 are attributed to organic search, referral or direct traffic.
- The live site uses **Contact Form 7**, which sends an email notification. The raw HTML I checked (home, contact, partner, HubSpot connector, AI voice agent) has **no HubSpot forms and no HubSpot tracking script**. It does have Google Analytics 4 (`G-PQXZPMEVBF`).
- The contact form's email subject is a template that shipped without being filled in. At least one 58-message customer thread is titled `octavebytes "[your-subject]"`.
- Consequence: **the CRM cannot say which page, keyword or campaign produced any deal.** The "Website" deal source is a guess. Any claim about what the site achieves would need GA4 and Search Console data, which I do not have.

## 4. Segments and buying routes

| Route | Evidence | What the buyer needs |
|---|---|---|
| **A. Direct: existing Amazon Connect + HubSpot/Dynamics/GHL customer** | The bulk of 2025–26 connector deals | A price, a trial, docs, and proof that it will not break when HubSpot changes |
| **B. AWS-referred** | About 100 incoming messages from amazon.* addresses (amazon.com 57, .ae 17, .es 15, .de 15). Partner Development Managers and Solutions Architects in Spain, UAE, Germany, US, Malaysia pass customer opportunities (Kenya, a Dutch marketing company, a Qatari delivery app, a Middle East chat start-up). Also "ACE" (APN Customer Engagement) opportunity registrations and validated leads | A **cost calculator or estimate**, a statement of work, AWS funding options, a demo, references, evidence of AWS credentials. They ask for these things by name |
| **C. Partner / subcontract** | Several threads: staff augmentation for a Saudi telecom integrator, collaboration talks with US and Asian AWS partners, an NDA with a Singapore AWS partner, a UK IT reseller. The bank robocall project ran alongside two systems integrators | Rate card ($45–75/hour, about $2,500/engineer/month), team credentials, NDA, a way to see what OB can do |
| **D. Marketplace** | AWS Marketplace listing (FTR certified, private-offer pricing) and HubSpot Marketplace listing. Buyers are sent the links after demos. I can't see from the data how many purchases came only through them | Public price, "Buy" or "Try" |
| **E. Cold outbound** | About 600 outbound emails in threads titled "collaboration for AWS / Amazon Connect / MS Dynamics" to other AWS partners; roughly 55 replies. Much lower yield than routes A–D | n/a. This is outreach, not inbound demand |

**Segments by what they buy.**
1. **Amazon Connect contact centres on HubSpot** (SMB to mid-market, 3–50 agents; a few in the hundreds). Highest volume.
2. **Amazon Connect contact centres on Dynamics 365 / GoHighLevel / Salesforce.** Lower volume, higher deal value (won: Sony Australia, ITKnocks; open: a UK pub group's POC).
3. **Banks and fintechs in South Asia and the Gulf buying AI voice, robocall and campaign tooling.** New, mostly relationship-led.
4. **AWS partners and resellers** buying capacity, white label or referral.

## 5. Proof material that exists, and the constraints on it

- One Amazon Connect SA wrote that a customer meeting went well and his involvement "was not even needed" (Snoonu). **Amazon employee, private email: not usable as a quote.**
- The bank robocall project was declared deployed across "all five use cases" on 27 April 2026 after a 113-message thread. The public case study is anonymous; the bank's identity and metrics need written approval.
- A permission-to-share-as-reference request went out in February 2025 ("Request for permission to share your contact as a reference"); the outcome is not obvious from the data.
- Customers with big brand names (for example Sony Australia, Foxit, Rappi, Zeller, Harte Hanks, TDCX) are all **commercial relationships whose logos need explicit permission**.

## 6. Things that surprised me

1. **The company is a connector vendor with a project past, not an Amazon Connect consultancy.** Growth is in the product line; the site still leads with consulting language.
2. **Prices exist, they are consistent enough to publish, and they are lower than the main competitor's.** The site hides them.
3. **"7 days free trial" is really "a call, then an engineer, then a deployment in your AWS account".** The trial is not self-serve, so it can't be a website button yet.
4. **Buyers' loudest complaint is not price; it is reliability and renewal admin.**
5. **The CRM has almost no digital attribution.** The site is running blind.
6. **AWS staff email more than most customers do** (about 100 incoming messages from amazon.* addresses, versus 169 from the largest single customer). The AWS channel is a first-class audience the site does not address.
7. **Cold outreach to other partners is a large share of email volume for a small yield.**
8. **One account manager's recorded 2025 sales were about $42,000 against a $55,000 target for 2026** (CEO email, February 2026). This is one person's number, not company revenue, but it says the direct-sales business is small. That argues for a narrow, sharply focused site, not a 50-page catalogue.
