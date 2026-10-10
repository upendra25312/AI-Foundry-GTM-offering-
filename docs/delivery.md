# Delivery dependencies, RACI, risks, and handover

The RACI below is a starting proposal only. Confirm named accountable owners, customer roles, and approval authority for each opportunity. It does not assert Cognizant tower capabilities, contract obligations, security approval, or revenue share.

## Proposed role boundaries

- **CIS Infra (proposed lead):** platform foundation and infrastructure scope—landing-zone extension coordination, Azure resource/network integration, IaC where contracted, platform observability, resilience and cost-control integration, and infrastructure handover.
- **Security:** customer control interpretation, identity/security architecture approval, threat/risk review, exceptions, audit and security-operation integration.
- **DevOps:** source control and pipeline standards, release/change automation, environment promotion and IaC pipeline operation.
- **Data:** data ownership, classification, governance, source access and information lifecycle decisions.
- **Data Engineering:** ingestion, transformation, data quality, indexing/refresh, data pipeline operation.
- **AI tower:** AI workload/model/application architecture, model selection and evaluation, grounding/safety integration, AI workload operation where agreed.
- **Customer/platform owner:** tenant/subscription/network/DNS/identity access and approval, existing ALZ decisions, business acceptance, licensing/procurement, service ownership, and Azure spend.

These role boundaries need joint sign-off. CIS Infra does not assume ownership of AI/model outcomes, customer data, security approvals, or uncontracted operations.

## Proposed RACI

`R` Responsible (does work); `A` Accountable (one final owner per activity); `C` Consulted; `I` Informed. Customer may add/replace roles. Agree a single A per row before delivery.

| Activity | CIS Infra | Security | DevOps | Data | Data Engineering | AI tower | Customer/platform owner |
|---|---|---|---|---|---|---|---|
| Business outcomes, workload priority, acceptance | C | I | I | C | C | C | A/R |
| Existing ALZ/platform fit and extension design | R | C | C | I | I | C | A |
| Identity, access, security controls and exceptions | R (platform implementation) | A | C | C | I | C | C |
| Network, hybrid connectivity, DNS design | R | C | C | I | I | C | A |
| Platform IaC/pipeline standards and deployment | R | C | A/R | I | C | C | C |
| Data classification, source permissions, retention | C | C | I | A/R | R | C | C |
| Data ingestion, transformation, indexing | C | C | C | A | R | C | I |
| AI/model/app design, evaluation, safety behavior | C | C | C | C | C | R | A |
| Platform monitoring, backup and recovery design | R | C | C | I | C | C | A |
| Workload operations and incident ownership | R (only agreed platform scope) | C | C | C | C | R (AI scope) | A |
| Azure spend ownership, tagging, budgets, FinOps review | R (platform controls) | I | C | C | C | C | A |
| Handover and service acceptance | R | C | C | C | C | C | A |

## Dependencies and entry criteria

| Dependency | Accountable provider | Needed by / evidence |
|---|---|---|
| Sponsor, business owner, workload boundary, acceptance criteria | Customer | Before estimate/design |
| Existing ALZ diagrams, policy, network and subscription standards | Customer/platform owner | Before foundation design |
| Tenant/subscription, approved environments, access path, change window | Customer/platform owner | Before implementation |
| Identity, network, DNS, firewall and hybrid connectivity decisions | Customer/platform owner with Security | Before private-path testing |
| Data owners, classification, access and approved synthetic/customer test data | Data/customer | Before ingestion or demo adaptation |
| AI service/model choice, target region, quotas/capacity, availability check | AI tower/customer with platform owner | Before design freeze and quote |
| Security, privacy, compliance, threat-model and exception approvals | Security/customer | Before production release |
| Pipeline, source control, IaC and release policy | DevOps/customer | Before deployment |
| Current Azure prices, license entitlements and approved delivery rates | Customer procurement + internal commercial | Before proposal/quote |
| Service owner, telemetry, support boundary, runbooks and escalation | Customer/service owner and delivery roles | Before managed operations transition |

## Risks and assumptions register

Use owner, due date, status, evidence, mitigation, and decision in the working project register.

| Risk / assumption | Impact | Mitigation / owner |
|---|---|---|
| Target AI model, feature, SKU, quota, or service unavailable in selected region | Redesign, delay, residency impact | Verify current service/model availability and quota early; maintain approved alternatives; owner: AI/platform lead |
| Existing ALZ differs from assumed pattern or lacks controls | Scope growth or unsafe parallel design | Assess evidence first; record gap and change request; owner: CIS Infra + customer platform owner |
| Private DNS/firewall/hybrid route incomplete | Workload cannot resolve/reach private endpoints | Validate end-to-end DNS and routes from each client network; owner: network/DNS owner |
| Data permissions/classification or quality are unresolved | Unauthorized data exposure or unusable results | Data-owner approval; synthetic data until cleared; owner: Data/Security |
| AI output quality or safety requirements unmeasured | Unacceptable user/business risk | Agree representative evaluation and human escalation with AI/product owners; owner: AI tower/customer |
| Unverified usage, token profile, retention, egress or SKU price | Cost overrun / inaccurate quote | Explicit low/base/high assumptions, budgets/alerts, price date and owner; owner: customer FinOps/platform |
| Tower/capability ownership is ambiguous | Gaps, duplicated delivery, unapproved commitment | Confirm named accountable leads and scope boundary before proposal; owner: opportunity lead |
| No approved commercial rates, licensing or revenue allocation | Invalid economics/contract | Internal finance/procurement approval; label allocation as proposal; owner: commercial lead |
| Customer requirements for RTO/RPO/support conflict with architecture | Unmet service expectations | Set measurable targets, validate dependencies and recovery evidence, contract only approved targets |

**Assumptions to confirm rather than silently accept:** customer owns the tenant, subscriptions, data rights, business acceptance, and Azure consumption unless contract says otherwise; necessary approvals and access arrive on schedule; chosen service/model is available and has sufficient quota; approved delivery and licensing terms exist; customer permits required monitoring and retention. If false, revise scope, schedule, design, and estimate.

## Handover checklist

- [ ] Customer owner accepts in-scope deliverables and records exclusions/deferred work.
- [ ] As-built architecture, decisions, dependencies, source links, versioned IaC/configuration, and deployment evidence are transferred.
- [ ] Identity/RBAC, secret/key ownership, access reviews, and credential rotation path are documented; no secrets are in handover files.
- [ ] Network routes, firewall rules, private endpoints, DNS zones/forwarders, and end-to-end connectivity tests are documented with owners.
- [ ] Monitoring, alert thresholds, diagnostic settings, log access/retention, incident routing, and sensitive-data logging constraints are agreed.
- [ ] Backup/rebuild, resilience targets, capacity/quota, and recovery test results are documented; open gaps are assigned.
- [ ] Cost model, current price source/date, budgets/tags, forecast, alert/action owners, and consumption responsibility are transferred.
- [ ] Runbooks, support boundary, service hours, escalation, known errors, and operational acceptance are agreed for the contracted components only.
- [ ] Security, privacy, data, AI/model, and customer approvals/evidence are recorded by their accountable owners.
- [ ] Open risks, assumptions, change requests, follow-on backlog, named owners, and review dates are accepted.
- [ ] Proposed revenue allocation has separate written internal approval before it is represented as final.
