# Learning plan and reusable asset backlog

Use this plan to produce a concrete presales artifact at each stage. Links to vendor-neutral course catalogs are search/catalog links, not endorsements or claims that a course is current or included in a subscription. Check course content and account access before use.

## Learning plan

| Stage | Learn / practice | Output for GTM |
|---|---|---|
| 1. Azure foundations | Microsoft Learn: [Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/), [Azure landing zones](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/), [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/) | Customer ALZ discovery map and decision log |
| 2. AI platform concepts | Microsoft Learn: [Azure AI Foundry documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/); GitHub: [Azure AI Landing Zones](https://github.com/Azure/AI-Landing-Zones) | Service/region verification checklist and AI foundation architecture review |
| 3. Hands-on labs | GitHub: [Microsoft AI for Beginners](https://github.com/microsoft/AI-For-Beginners), [Azure AI Landing Zones](https://github.com/Azure/AI-Landing-Zones), and [Azure samples](https://github.com/Azure-Samples) | One bounded, synthetic-data demo; document prerequisites, cost, risks, and acceptance first |
| 4. FinOps | Microsoft Learn: [FinOps on Azure](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/manage/azure-financial-management/); [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/) | Low/base/high consumption model with metering assumptions and source dates |
| 5. Structured external study | Udemy: [Azure AI Foundry course catalog search](https://www.udemy.com/courses/search/?q=Azure%20AI%20Foundry); LinkedIn Learning: [Azure AI course catalog search](https://www.linkedin.com/learning/search?keywords=Azure%20AI%20Foundry) | Shortlist only a current course; turn one lesson into a customer-safe architecture or discovery asset |
| 6. Short practical updates | YouTube: [Microsoft Azure AI Foundry search](https://www.youtube.com/results?search_query=Microsoft+Azure+AI+Foundry); favor Microsoft channels and verify documentation/version dates | A brief demo script and “what changed / what to revalidate” update |
| 7. Secure platform design | Microsoft Learn: [Azure Private Link](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview), [private endpoint DNS](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns), [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/overview) | Network/DNS test plan, monitoring ownership matrix, and security review prompts |

## Reusable asset backlog

Sequence is proposed; backlog items are not approved production modules or capabilities. Review Microsoft/customer IaC standards, licenses, security, versioning, and support before publishing reusable assets.

| Priority | Asset | Proposed acceptance criteria | Dependencies / owner to confirm |
|---|---|---|---|
| 1 | Terraform discovery/readiness workbook and architecture decision record | Captures ALZ, identity, networking/DNS, security, monitoring, resilience, cost, decisions, source dates, risks, and owners without customer secrets | CIS Infra; customer platform and security reviewers |
| 2 | Terraform module: diagnostic settings and monitoring integration | Configurable destination/retention; no sensitive payload logging by default; policy-compatible examples; automated plan/validation and documented ownership | CIS Infra/DevOps; Log Analytics/customer standards |
| 3 | Terraform module: private endpoint and DNS integration (service-specific) | Explicit service support and DNS inputs; no guessed zones; validates links/forwarding; documents non-private dependencies and test steps | CIS Infra/network/DNS; verify each service's current DNS guidance |
| 4 | Terraform module: workload identity and least-privilege role assignment pattern | Minimal roles, configurable principal, no credentials, documented approval boundaries and tests | Security/CIS Infra; service-specific role verification |
| 5 | Terraform module: budget/tag/cost alert pattern | Configurable budgets and recipients; deployment does not imply finance approval; test alert path; clear consumption owner | CIS Infra/FinOps; customer budget and ownership inputs |
| 6 | Bounded synthetic RAG demo (local first; Azure-connected variant separately gated) | Synthetic-only corpus; predictable bounded behavior; safe error handling; documented architecture, setup, costs, limitations, and acceptance; no secrets committed | AI tower/CIS Infra/Security; customer approval for any cloud version |
| 7 | Reusable managed-operations transition pack | Service boundary, runbooks, escalation, telemetry, RTO/RPO, cost review, and acceptance are configurable and contract-aligned | CIS Infra/service management/customer owner |
| 8 | Region/model/service verification worksheet | Captures official source, URL, review date, service/model/SKU/region/quota, and validation owner; does not hard-code availability as permanent | AI tower/platform/procurement |

Promote an asset from backlog only after peer review, security review where applicable, representative validation, and an owner/support lifecycle are defined.
