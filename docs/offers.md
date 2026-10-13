# Offer cards

These are proposed, configurable offer shapes for EMEA and US enterprise buyers—not approved Cognizant capabilities or fixed commitments. Confirm geography, legal entity, delivery model, scope, pricing, and service availability for each deal. CIS Infra is the proposed lead for the infrastructure/platform elements; domain tower ownership requires explicit agreement.

## 1. AI Platform Readiness Assessment

| Element | Proposed definition |
|---|---|
| Buyer | CIO/CTO, cloud platform owner, enterprise architect, AI program sponsor, or CISO delegate |
| Business problem | The customer needs an actionable view of whether its governance, Azure foundations, security, networking, operations, and cost controls can support its prioritized AI workloads. |
| Scope | Time-boxed discovery and evidence-based review of existing landing-zone fit; identity and access; network/private access and DNS; hybrid connectivity; policy/security controls; observability and resilience; FinOps and operating model; prioritized workload and platform gaps. |
| Prerequisites | Executive sponsor and nominated platform/security/data/AI contacts; agreed assessment boundaries and target use cases; read-only evidence or facilitated walkthroughs; data classification and residency constraints; permission to review relevant diagrams/configurations. No production access is assumed. |
| Deliverables | Current-state and gap summary; prioritized risk/decision register; target-state options and dependency map; high-level cost-input worksheet with unknowns flagged; phased roadmap; proposed RACI; playback and decision log. |
| Exclusions | Production changes/deployment; penetration testing or certification; legal/compliance opinion; model validation; data remediation; guaranteed savings or workload outcomes; detailed low-level design unless separately scoped. |
| Acceptance criteria | Sponsor receives the agreed assessment pack; each in-scope finding has evidence/source, impact, recommendation, priority, owner role, and dependency or is explicitly marked unverified; playback completed and customer comments/decisions recorded. |
| Expansion opportunities | Foundation extension; workload-specific architecture/design; security or data remediation by the accountable tower; bounded demonstration; managed operations readiness. |

## 2. Azure AI Platform Foundation Extension

For customers with an existing Azure landing zone (ALZ). This is an extension, not a replacement for the ALZ; preserve customer ownership and existing platform guardrails.

| Element | Proposed definition |
|---|---|
| Buyer | Azure platform/landing-zone owner, cloud center of excellence, AI platform sponsor, enterprise architect, or security lead |
| Business problem | Existing cloud foundations need validated, repeatable platform capabilities and controls for an agreed set of Azure AI workloads. |
| Scope | Validate the existing ALZ and extension points; design and, if explicitly contracted, implement agreed subscription/resource organization, identity/RBAC, private connectivity/DNS, policy/security integration, monitoring, resilience, cost controls, and infrastructure-as-code handover for a bounded workload pattern. |
| Prerequisites | Accepted current-state ALZ design and platform owner; customer-selected region(s), subscription(s), network/DNS and identity owners; documented workload/data classification and requirements; security architecture approval; quotas/capacity and model/service availability verified; environment access and change windows; approved IaC standards and pipelines. |
| Deliverables | Validated solution design and decisions; responsibility/dependency matrix; agreed configuration/IaC artifacts if in scope; deployment and test evidence; operational runbook, cost assumptions, risks, and handover. |
| Exclusions | Greenfield enterprise landing zone; AI application/model/data product delivery; security exception approval; tenant-wide policy changes; 24x7 support; production availability or performance guarantee; cloud credits or licensing unless separately contracted. |
| Acceptance criteria | Agreed scope deployed or design-only outputs delivered as contracted; tests pass for specified identity, network/DNS, policy, telemetry, and recovery checks; no unresolved critical blockers within the acceptance boundary; artifacts and ownership accepted by designated platform owner. |
| Expansion opportunities | Additional workload patterns/regions; data/AI tower implementation; controlled demonstration; landing-zone remediation; managed platform operations. |

## 3. Managed AI Platform Operations

Operate only explicitly identified platform components under an approved service description, service hours, support model, and customer authorization.

| Element | Proposed definition |
|---|---|
| Buyer | CIO/CTO, cloud operations/service owner, AI platform owner, procurement, and service-management lead |
| Business problem | Platform teams need a repeatable support and continual-improvement model for agreed AI platform foundations and operational controls. |
| Scope | Transition-in; agreed monitoring and alert response; access/configuration and change processes; incident/problem/request coordination; capacity, quota, reliability, security-posture and cost review; runbook maintenance; service reporting and continual improvement. Define component inventory, boundaries, severity, hours, response targets, and escalation path in the contract. |
| Prerequisites | Stable accepted platform and architecture; named customer service owner and tower contacts; operational access through approved controls; telemetry, CMDB/service inventory, runbooks, support agreements, change/incident processes, and escalation contacts; signed service description and commercial approval. |
| Deliverables | Transition checklist and acceptance; service runbooks; agreed dashboards/reports; incident/change records; recurring service and cost review; improvement backlog and periodic service review. |
| Exclusions | Unspecified AI application/model/data operations; model quality/safety decisions; tenant-wide SOC or security operations; Azure/Microsoft support fees; unlimited changes; uncontracted SLA, coverage, or outcome guarantees. |
| Acceptance criteria | Transition entry/exit gates met; named components and access approved; agreed runbooks and escalation tests completed; reporting cadence and metrics baseline accepted; open risks and deferred work assigned. Operational targets are only those in the executed agreement. |
| Expansion opportunities | Additional platform services or regions; workload-specific SRE; security operations; data/AI operations by agreement with those towers; automation and FinOps improvements. |

## Qualification gates (all offers)

Do not qualify an offer as committed delivery until a sponsor, measurable business outcome, workload boundary, existing-platform owner, customer dependencies, decision process, data/residency constraints, security path, commercial path, and acceptance authority are identified. If ownership or prerequisites are unknown, record them as open decisions and scope a discovery step rather than assuming them.
