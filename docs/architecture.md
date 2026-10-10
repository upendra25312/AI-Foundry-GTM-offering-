# Reference architecture patterns

These are design prompts and options, not a deployment specification. Validate service and model availability, quota, SKU/features, private connectivity support, and commercial terms for the exact region, tenant, and date. Align the customer design to the Azure Cloud Adoption Framework (CAF), Azure Well-Architected Framework (WAF), and FinOps guidance in [sources.md](sources.md).

## Bounded pattern: private enterprise RAG foundation

```text
Enterprise users
      |
Customer identity / conditional access (customer-owned)
      |
Private corporate access -- ExpressRoute/VPN (where needed)
      |
Hub/spoke or customer-approved network + firewall/DNS
      |
Workload subnet / private endpoints (where supported and approved)
      +---- application or AI workload identity
      +---- Microsoft Foundry project/model endpoint (formerly Azure AI Foundry; region/model validated)
      +---- Azure AI Search index (synthetic or customer-approved content)
      +---- approved storage / Key Vault integration as required
      |
Azure Monitor / Log Analytics --> agreed operations and security teams
Azure Policy / Cost Management / budgets / tags --> governance and FinOps
```

The diagram is logical: resource placement, service names, private endpoint support, DNS zones, identity integration, and traffic paths depend on the chosen services and customer architecture. Do not infer that private endpoints alone make an environment secure or that every feature is available in every region.

## Design areas and decisions to validate

| Area | Reference questions / baseline | Evidence before design approval |
|---|---|---|
| Landing zone and ownership | Extend the customer's ALZ; align subscription, management group, policy, tags, environment, and network patterns. Escalate material gaps rather than silently creating parallel foundations. | ALZ diagrams, policy/IaC standards, subscription/network owners, change approval |
| Identity | Prefer customer-approved Microsoft Entra ID integration and least-privilege role assignments; use managed identities for supported workload-to-service access; separate human admin from workload identity; define privileged access and access reviews. | Identity flow, role matrix, service support verification, approval by identity/security owner |
| Private networking | Assess private endpoints for supported services, subnet/IP allocation, egress and firewall rules, route control, ingress, and whether customer-managed or service-managed networking is suitable. Public network access should follow customer policy. | Service-specific network docs, approved topology, firewall and route matrix, deployment validation |
| DNS | Decide private DNS zone ownership, links, forwarding, resolver placement, split-horizon behavior, and on-premises resolution. Validate endpoint FQDN resolution from workload and hybrid clients. | DNS ownership, conditional-forwarder design, zone links, test evidence from each network path |
| Hybrid connectivity | Reuse customer-approved ExpressRoute, VPN, Virtual WAN, or other patterns; validate routing, segmentation, bandwidth, failover, and responsibility boundaries. | Network diagrams, routes, connectivity tests, customer network sign-off |
| Security and governance | Integrate customer policy, Defender/SIEM/SOC processes where licensed and approved, encryption/key requirements, logging, threat model, data classification, content safety, and model governance. Security decisions remain with accountable security stakeholders. | Control mapping, threat model, policy results, exception approvals, data/AI owner decisions |
| Monitoring and operations | Identify platform/workload signals, diagnostic settings, metrics/logs, alerts, action groups, retention, access, incident routing, and service-health ownership. Avoid logging prompts or sensitive data unless explicitly approved. | Monitoring plan, retention/access approvals, alert test, service owner and runbooks |
| Resilience | Set workload-specific RTO/RPO, backup/rebuild approach, zone/region strategy, dependency failure modes, quota/capacity plan, and recovery test. Confirm regional features and model availability. | Approved objectives, dependency analysis, service-region checks, restore/failover evidence |
| Cost management | Apply customer tags/budgets, owner and environment allocation, forecast by metered driver, alert/action ownership, and regular review. Separate Azure consumption from delivery and licenses. | Usage model, current pricing source/date, budget owner, cost guardrails, variance process |
| AI workload | Define retrieval/data ingestion, document access filters, evaluation, content safety, human escalation, model selection, quota and responsible AI approval. AI tower and customer product owner confirm workload controls. | Workload design, approved models/data, quality and safety acceptance tests |

## Architecture decision record template

For each decision capture: ID/date; question; context; options; decision; owner/approver; assumptions; consequences; security/privacy/cost/reliability impact; validation evidence; source URL and review date; revisit trigger. Mark unresolved choices **OPEN** and do not present a preferred option as an approved customer decision.

## Bounded demo design (documented before implementation)

The repository demo in [`../demos/local-rag/README.md`](../demos/local-rag/README.md) is a local-only illustration of a retrieval-augmented question-answering flow using synthetic documents, deterministic keyword scoring, and extractive snippets. It does not call Microsoft Foundry (formerly Azure AI Foundry), Azure AI Search, or any external service and does not demonstrate production security, model quality, or service availability. Its purpose is to explain a workload boundary and stimulate platform discovery; an Azure-connected version requires a separate design, customer approvals, current regional/cost checks, and security review.
