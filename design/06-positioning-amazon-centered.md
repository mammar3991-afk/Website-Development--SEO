# Positioning change: Amazon Connect-centred (8 Oct 2026)

**This supersedes the "connector-first" strategy in `00-decision-and-strategy.md`** for positioning and navigation. The pricing, SEO, conversion and proof rules in the other design files still apply.

## Decision
The CEO and colleagues want Octavebytes presented as an **Amazon Connect partner** (migration, services, bots and AI, all centred on Connect), with **products that integrate with Amazon Connect** shown after the services: the HubSpot, Dynamics 365 and other CRM connectors, **Campaign Manager** and **AI Quality Management**.

Octavebytes should pitch itself this way even where it has no completed projects in an area yet. The site does this by presenting these as service offers and marking every capability claim for confirmation, never by implying past projects.

## What the evidence says (kept for honesty, not to override the decision)
- The CRM shows connector deals as nearly all current revenue and no completed Cisco/Genesys-to-Connect migration. So the migration page and the "platforms we migrate from" list carry flags.
- Verified and used as lead credentials: 45+ engagements, delivering since 2021, AWS FTR-certified connector, partner badges (badge use still to be confirmed).

## Information architecture changes
| Area | Before | Now |
|---|---|---|
| Nav item 1 | Products | **Amazon Connect**: Overview, Migration, Setup and custom builds, Bots and AI, Banking and regulated voice |
| Nav item 2 | Solutions | **Products**: HubSpot, Dynamics 365, Other CRMs, Campaign Manager, AI Quality Management, Call intelligence |
| New pages | | `/amazon-connect/`, `/amazon-connect/migration/`, `/amazon-connect/ai-and-bots/`, `/products/campaign-manager/`, `/products/ai-quality-management/` |
| Homepage | CRM softphone pitch and trial | Amazon Connect partner pitch: what we do, products, why Octavebytes, proof, FAQ |
| Primary call to action | 7-day trial | "Talk to an Amazon Connect engineer" on the homepage. The trial stays on product pages and in the header |
| Services page | Setup, migration and builds | Setup and custom builds only; migration moved to its own page |
| Redirects | `/amazon-connect/` and `/migration-to-amazon-connect/` to the services page | `/amazon-connect/` is live; `/migration-to-amazon-connect/` goes to the new migration page |

## Open items for the owner
- **Campaign Manager and AI Quality Management:** status, name, features, pricing, screenshots, regions and languages. The pages are placeholders with flags until supplied. Also decide how AI QM differs from AWS's own automated evaluations in Amazon Connect.
- **Migration:** which platforms were really migrated, how many projects, what can be shown.
- **Bots and AI:** which features are live (Lex, Bedrock, Q in Connect), which languages, and the voice-AI product name.
- **Managed support:** is there a support-plan offer?
- **Header button:** keep "Start a 7-day trial" (suits the connectors) or change it to "Talk to an engineer".
- Colour option A to D is still to be chosen.
