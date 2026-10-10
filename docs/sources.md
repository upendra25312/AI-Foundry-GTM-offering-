# Source register

Official Microsoft guidance used to shape this toolkit. Links and claims are starting points, not customer-specific approval. **Review date: 2026-10-10** (initial authoring review). Microsoft pages and availability/pricing change; re-open the sources at proposal and design time and update the review date. No regional feature availability is asserted here.

| Topic | Official source | Use / validation note |
|---|---|---|
| Cloud Adoption Framework | [Cloud Adoption Framework for Azure](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/) | Adoption, governance, management and readiness context |
| Azure landing zones | [Azure landing zone documentation](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/) and [design areas](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-areas) | Reuse and extend existing platform guardrails; verify customer-specific design |
| Well-Architected Framework | [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/) | Reliability, security, cost optimization, operational excellence and performance-efficiency review lenses |
| FinOps | [Azure financial management](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/manage/azure-financial-management/) and [FinOps Framework: architecting for cloud](https://learn.microsoft.com/en-us/cloud-computing/finops/framework/optimize/architecting) | Cost governance and financial-management practices; confirm currently applicable guidance |
| Azure AI Foundry | [Azure AI Foundry documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/) | Current product terminology and service-specific implementation documentation; check for renamed features |
| Azure AI landing zones | [Azure AI Landing Zones (Microsoft GitHub)](https://github.com/Azure/AI-Landing-Zones) | Reference implementation material; inspect release/version and suitability before adoption |
| Private Link | [What is Azure Private Link?](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview) | Private connectivity concepts; service-specific support still must be checked |
| Private endpoint DNS | [Azure Private Endpoint DNS configuration](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns) | DNS configuration patterns; verify exact private DNS zone for each service |
| Azure Monitor | [Azure Monitor overview](https://learn.microsoft.com/en-us/azure/azure-monitor/overview) | Observability capabilities; validate retention, ingestion, access, and charges |
| Regional service availability | [Azure products by region](https://azure.microsoft.com/en-us/explore/global-infrastructure/products-by-region/) and [Azure service availability by region type/category](https://learn.microsoft.com/en-us/azure/reliability/availability-service-by-category) | High-level service availability only; verify individual model, feature, SKU, quota, and deployment availability for the target tenant and date |
| Azure pricing | [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/) | Build current scenario estimates; final charges depend on meter, region, terms, usage, and contract |

## Review protocol

For each opportunity, record the date checked, target region(s), service/model/SKU, quota and capacity result, private networking and DNS support, licensing/entitlement, price-source date, and the person who verified each item. If an official page does not establish a customer-specific fact, record it as **unverified** and obtain the relevant Microsoft/customer/internal confirmation. Do not rely on cached region tables or this initial reference list as a deployment approval.
