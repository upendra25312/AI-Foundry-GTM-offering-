# Discovery and deal qualification

Use as a facilitated conversation, not a compliance questionnaire. Capture responses with a customer-approved classification; avoid recording secrets, personal data, or confidential artifacts in this repository.

## Discovery questionnaire

### Business outcome and workload

1. What business process or decision should AI improve, and what baseline and target measure will demonstrate value?
2. Who is the executive sponsor, product owner, end users, and acceptance authority?
3. What is the first workload (for example, internal knowledge retrieval, document processing, or an agent)? What is explicitly out of scope?
4. What is the expected user population, geography, concurrency, latency, availability, recovery, and growth profile?
5. Is the workload a prototype, pilot, or production service? What is the target decision/deployment date and procurement path?

### Existing Azure platform

6. Is an Azure landing zone in place? Who owns its architecture, subscriptions, network, identity, policy, and change process?
7. Which tenant, subscriptions, regions, environments, connectivity model, and deployment pipeline are approved?
8. What identity provider, managed identity, privileged-access, RBAC, and workload separation patterns are required?
9. What address spaces, DNS resolvers/zones, private endpoint, firewall, egress, proxy, and hybrid connectivity patterns exist?
10. Are there platform standards, policies, IaC modules, naming/tagging, monitoring, backup, or DR requirements to reuse?

### Data, security, and governance

11. What data sources, owners, formats, classifications, volumes, freshness, and quality constraints apply?
12. Does data include regulated, sensitive, personal, export-controlled, or customer-confidential content? Who determines permitted use?
13. What residency, sovereignty, retention, deletion, encryption/key, audit, threat-model, and regulatory requirements apply?
14. Which security approvals, threat assessments, identity reviews, network reviews, and exception processes are required?
15. What AI safety, content filtering, prompt-injection, grounding, human review, evaluation, and model risk controls are required, and which tower owns them?

### Operations and economics

16. Who owns platform service health, incident response, vulnerability management, change, capacity/quota, and cost accountability?
17. What hours, support boundaries, incident severity definitions, escalation, service targets, and reporting are required?
18. What is the expected usage profile: requests, tokens or processing units, data/index/storage volume, network egress, environment uptime, and retention? What is the source for each estimate?
19. Which Azure services, models, regions, and licenses are customer-approved? Have current price and availability been checked?
20. Which budgets, tags, allocation dimensions, chargeback/showback, and FinOps review cadence apply?

### Commercial and governance

21. Who approves scope, security, architecture, procurement, rates, licenses, Azure spend, and commercial terms?
22. What customer, Cognizant, Microsoft, and other supplier dependencies must be met, by whom, and by when?
23. What deliverables and objective acceptance evidence are required? How are changes and assumptions handled?
24. Which internal commercial/finance approvers must review proposed tower revenue allocation? Treat allocation as unapproved until they do.

## Deal qualification checklist

Record **Yes / No / Unknown**, an owner, evidence, and target date for every item. `Unknown` is not an implicit yes.

| Gate | Status | Evidence / owner / due date |
|---|---|---|
| Named sponsor, business owner, and measurable problem |  |  |
| Workload boundary, stage, users, and acceptance authority |  |  |
| Existing ALZ/platform owner and architecture evidence identified |  |  |
| Target regions, residency, data classification, and legal constraints reviewed |  |  |
| Security, identity, network/DNS, Data, Data Engineering, DevOps, and AI tower owners engaged |  |  |
| Availability, model/service capacity, quotas, and tenant eligibility verified |  |  |
| Usage assumptions and separate delivery/Azure/licensing/operations cost owners identified |  |  |
| Customer and internal approvals, procurement path, and decision date understood |  |  |
| Scope, exclusions, dependencies, acceptance criteria, and change process agreed |  |  |
| Delivery capacity and capability confirmed by accountable leads—not inferred |  |  |
| Risks, assumptions, unresolved decisions, and next actions have named owners |  |  |
| Any proposed revenue allocation clearly marked pending internal approval |  |  |

**Go** only when material gates are evidenced or explicitly converted to priced/scheduled discovery dependencies. **Hold/re-scope** when security/residency, platform ownership, capacity, acceptance, or commercial authority is unresolved.
