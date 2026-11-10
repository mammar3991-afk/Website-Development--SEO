# Start a trial (and contact)  ·  `/start-trial/` and `/company/contact/`

> **Page job:** turn a ready buyer into a HubSpot deal in under two minutes. This is also the "contact / demo" page for the whole site.

## `/start-trial/`

**Title tag:** Start a 7-Day Trial | Octavebytes
**Meta description:** Tell us your CRM and Amazon Connect setup and we will open a 7-day trial for you. Two minutes.

# Start your 7-day trial

Tell us about your setup. An engineer will reply with the next steps. `[CONFIRM: reply-time commitment]`

### Form
*(Every field maps to a HubSpot property; see the conversion plan.)*

| Field | Type | Options / notes |
|---|---|---|
| Your name | text | required |
| Work email | email | required; block free-mail domains only for the "Book a call" route, not the trial |
| Company | text | required |
| Which CRM do you use? | select | HubSpot · Microsoft Dynamics 365 · GoHighLevel · Other |
| Are you running Amazon Connect? | select | Yes, in production · Yes, testing · Not yet, we are choosing a system |
| AWS region of your Amazon Connect instance | select | (list) · I don't know |
| How many agents? | select | 1–5 · 6–20 · 21–50 · 51+ |
| Which channels matter? | multi-check | Voice · SMS · WhatsApp · Chat · Transcripts and AI summaries |
| Anything else we should know? | textarea | optional |
| Consent | checkbox | "I agree to be contacted about this request. Privacy policy." (no pre-ticked SMS consent; the old form bundled text-message consent) |

**Button:** Start my trial

**Under the button:** *No card needed. We will not add you to a mailing list.* `[CONFIRM: no card needed; consent wording]`

### What happens next (shown beside the form)
1. **You get an email within one business day** `[CONFIRM]` with the requirements checklist.
2. **We open your trial** on our hosted environment.
3. **Your agents test for 7 days.** An engineer is on the thread.
4. **You decide.** If you go ahead, we deploy into your AWS account.

### Alternative routes (beside the form)
- **Book a 30-minute call** (calendar link) `[CONFIRM]`
- **Buy on AWS Marketplace** / **Buy on HubSpot Marketplace**
- **Not running Amazon Connect yet?** [We can set it up →]

### Thank-you page
"Thanks, {first name}. We have your request. Here is what to have ready: (1) your Amazon Connect instance alias and ID, (2) the AWS region, (3) the S3 bucket where call recordings are stored, (4) a HubSpot Super Admin (or Dynamics 365 admin) who can approve the connection. **[Read the requirements →]**"

---

## `/company/contact/`

**Title tag:** Contact Octavebytes: Sales, Support and Offices
**Meta description:** Talk to sales, get support, or find our offices in the USA, UK and Pakistan.

# Contact us

| I want to… | Go here |
|---|---|
| **Start a trial or get a quote** | [Start a trial](/start-trial/) |
| **Get help as a customer** | support@octavebytes.com · [Docs](https://docs.octavebytes.com) · [Status](https://status.octavebytes.com) |
| **Talk about a bank, telecom or regulated-sector project** | [Contact form, "Regulated voice"] |
| **Partner with us** | [Partner enquiry](/partners/) |
| **AWS account team** | [For AWS teams](/partners/aws/) |
| **Careers** | [Careers](/company/careers/) |

**Sales:** sales@octavebytes.com  ·  +1 855 681 4627 `[CONFIRM: live number]`
**Support:** support@octavebytes.com  ·  hours `[CONFIRM: what is staffed]`

### Offices
`[CONFIRM: each office is real and staffed; the current site lists three addresses with inconsistent numbers]`
- **USA:** 10808 Capri Dr, McKinney, TX 75072
- **UK:** 128 City Road, London EC1V 2NX
- **Pakistan:** Office 2, Fourth Floor, 36 Civic Centre, Garden Town, Lahore · +92 326 0376366

*Use one address block, in one component, on every page. No page should have its own phone number.*

### General contact form
Name · Work email · Company · Topic (Sales · Support · Regulated-sector project · Partnership · Other) · Message · Consent.
*Email subject line is generated from the Topic field, never from an unfilled template tag. The old form sent messages titled `[your-subject]`.*
