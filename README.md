# Azure AI presales and GTM toolkit

Reusable working material for enterprise Azure AI opportunities in EMEA and the US, prepared for a Cognizant CIS Infra presales architect. It is a proposal toolkit, not an approved Cognizant offering, rate card, policy, or customer reference. Tailor each artifact with the customer and obtain the approvals listed before making commitments.

## Source inputs and limits

The repository supplied for this work contained only this README. No proposal, Excel workbook, customer architecture, internal rate card, approved capability catalog, revenue allocation policy, or customer reference was present. Consequently, no customer-specific facts, approved rates, licenses, service availability, or delivery commitments are assumed. All example content is synthetic; all variable commercial inputs are left configurable.

## Repository map

| Path | Use |
|---|---|
| `docs/offers.md` | Three offer cards, qualification gates, and expansion paths |
| `docs/discovery.md` | Customer discovery questionnaire and deal qualification checklist |
| `docs/architecture.md` | Reusable architecture patterns and bounded demo design |
| `docs/commercials.md` | Configurable effort, Azure consumption, licensing, and operations model |
| `docs/delivery.md` | Dependencies, proposed RACI, risks, assumptions, and handover |
| `docs/enablement-backlog.md` | Role-focused learning plan and reusable asset backlog |
| `docs/sources.md` | Official guidance and source review dates |
| `demos/local-rag/` | Bounded, offline synthetic-data RAG demonstration (no Azure deployment) |

## Suggested workflow

1. Start with the discovery questionnaire and qualification checklist. Confirm customer objectives, data classification, regulatory/residency constraints, existing Azure landing-zone ownership, and decision makers.
2. Select one offer card and agree scope, exclusions, dependencies, success criteria, and roles. Use the architecture patterns as options to validate—not as a customer design or guarantee.
3. Complete the configurable commercial model with current, customer-approved delivery rates, Azure pricing inputs, licensing, tax/currency treatment, and internal approvals. Recheck Azure services and regional/model availability for the target region and deployment date.
4. Agree the proposed RACI with the customer and internal tower leads. Resolve risks, assumptions, security approvals, and change control before a statement of work or production deployment.
5. Use the local demo only to illustrate a synthetic retrieval flow. It does not call Azure, prove production readiness, or estimate a cloud bill. Follow its README for prerequisites, run steps, and acceptance criteria.
6. Record decisions, owners, source review date, and changes in the customer-specific delivery pack; do not put customer confidential data or credentials in this repository.

## Boundaries

- CIS Infra is proposed to lead infrastructure/platform foundations and their operational handover. Security, DevOps, Data, Data Engineering, and AI tower responsibilities must be confirmed for each opportunity; see [the proposed RACI](docs/delivery.md).
- Revenue allocation is a proposal for internal commercial review, not an approved split.
- Microsoft references are starting points. Service names, product packaging, regional/model availability, quota, pricing, and licensing can change; validate against official sources and customer tenant constraints before presenting or deploying.
- The included demo is local and intentionally bounded. No Azure resources are created and no credentials are required.

## Validation

This is a documentation-first repository with no existing build, lint, or test configuration. The demo uses Python's standard library and includes a focused `unittest` test. Run it from the repository root:

```bash
python -m unittest discover -s demos/local-rag/tests -v
python demos/local-rag/app.py
```

Review external source URLs and their dates in [docs/sources.md](docs/sources.md) before reuse.
