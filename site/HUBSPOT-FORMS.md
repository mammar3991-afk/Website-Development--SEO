# HubSpot form spec (portal 9426463)

Build these in HubSpot > Marketing > Forms > Create form > Embedded form (Regular). Name each form exactly as below. Then send me the six form GUIDs (Share > Embed code shows `formId`).

Every form needs these **hidden fields** (leave blank; the site fills them): `intent`, `source_page`, `referrer`, `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`.
Every form needs **visible** `firstname`, `lastname`, `email` (required), `company`. Turn on the GDPR/consent checkbox (the site sends it as `legalConsentOptions`).
Set each form's lifecycle stage to Lead and follow-up to the same workflow the existing Request a Demo form uses (create the deal, notify sales).

| Form name | Extra visible fields |
|---|---|
| `OB Website - Trial` | `crm_used`, `connect_status`, `aws_region`, `agent_band`, `channels`, `plan_interest`, `message` |
| `OB Website - Estimate` | same as Trial (the site sets hidden `intent=estimate`) |
| `OB Website - AWS opportunity` | `agent_count`, `timeline`, `ace_id`, `message` |
| `OB Website - Regulated sector` | `topic`, `message` (hidden `intent=regulated`) |
| `OB Website - Partner` | `partner_type`, `aws_partner_tier`, `company_website`, `message` |
| `OB Website - Contact` | `topic`, `message` |

Properties were created in the CRM on 14 Oct 2026 under the Contact information group. `message` already existed in HubSpot, so it was reused.

Then put the GUIDs into `site.json` > `hubspot.formGuids`. Portal ID is `9426463` (matches `site.json`). The 21 properties were created in this account on 14 Oct 2026.
