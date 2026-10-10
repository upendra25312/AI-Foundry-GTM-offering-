# CIS Infra Azure AI offering: PDCA action and release plan

Prepared for Upendra Kumar. Revision 2, 10 October 2026.

## Purpose and decision boundary

Rebuild the GTM and solutioning proposals around a bounded customer outcome, a selected architecture, a transparent USD example and evidence-based release decisions. This is a proposed working-day plan for the Cognizant team. Day 1 begins after the sponsor assigns owners and accepts the work. It is separate from the illustrative eight-week customer implementation schedule.

The revised decks contain a worked reference case and proposed targets. They do not establish an approved offering, Cognizant rates, an Azure quote, current tower capacity or completed implementation tests. Public capability descriptions do not establish internal asset availability.

## 1. PLAN: days 1–3

**Accountable:** Infra sponsor. **Responsible:** Upendra as proposed integrated solution owner, with tower leads.

1. Register every audit finding with priority, owner, due day, required evidence, reviewer and status. Keep one design and commercial baseline for both decks.
2. Confirm the primary offering: an extension to an existing landing zone for one funded, read-only AI workload. Assessment is the entry route when discovery remains unresolved. Operations is the recurring companion.
3. Establish the reference customer hypothesis: one document collection, two environments, 5,000 eligible users and 20,000 base monthly requests. Validate the source size, ACL metadata, adoption and business value with account teams.
4. Select a custom application RAG pattern. The app handles retrieval and authorization. Hosted agents, APIM, autonomous actions, OCR, extra sources, M365 rollout and regional DR are separate options.
5. Create an architecture decision register covering model version/API, deployment type, region, runtime, data services, private paths, identity, telemetry and recovery.
6. Confirm approved input owners for role costs, regional Azure prices, onshore/offshore mix, taxes, margin, risk reserve and attribution. Sample values remain clearly marked until replaced.
7. Agree evaluation, performance, revocation, recovery and service targets as proposals. Identify the customer approver for each.

**Outputs:** accepted scope, audit register, customer hypothesis, architecture decisions, commercial input register and acceptance draft.

**Exit gate:** sponsor accepts the boundary; every critical audit item has one accountable owner and a due day. Unresolved discovery stays in an assessment SOW.

## 2. DO: days 4–10

**Accountable:** integrated solution owner. **Responsible:** Infra, Security, DevOps, Data, Data Engineering and AI package owners.

1. Rebuild the GTM main story around the customer blocker, buyer, measurable outcome, primary offer, economics, differentiation hypothesis, delivery model and approval request.
2. Rebuild solutioning around one selected architecture. Produce native editable logical and network diagrams. Number request, retrieval, generation, ingestion and monitoring flows.
3. Specify the resource BOM by environment, service, SKU, quantity and candidate geography. Attach a dated price source and a cost owner to each billable item. Record shared hub allocation without double counting.
4. Implement the quote model: role days × approved costs; explicit reserve; agreed gross margin; optional assessment; Azure run costs; operations and licences as separate lines.
5. Demonstrate tower attribution with a reconciled worked example. Keep sales credit, delivery cost, shared internal charges and services revenue as separate views.
6. Allocate the 88 base days by week and tower. Keep the 13.2-day reserve unscheduled until a risk response needs it. Confirm resource availability and customer review/CAB windows.
7. Build a controlled reference demonstration. Use versioned Terraform and application releases; test private paths, restricted retrieval, citations, telemetry and rollback. Source sample code is a starting point, not production proof.
8. Implement permission enforcement: authenticate users, resolve group scope, deny unknown permissions, synchronize ACL metadata, filter before generation and protect citation downloads. Establish a feasible revocation path.
9. Create the operating schedule: one customer time zone, agreed holidays, service pool capacity, specialist OLAs, included allowance and overage rules.
10. Place detailed Microsoft reference images, costing, weekly staffing and RACI in appendices. Use simple, editable architecture views in the main proposal.

**Outputs:** revised PPTX drafts, implementation design pack, estimate, tower work packages, demo repository, test results and service schedule draft.

**Exit gate:** reviewers can trace every commercial number and every architecture component to a source, assumption or accepted decision. No unsupported approval, outcome or compliance claim remains.

## 3. CHECK: days 11–15

**Accountable:** integrated solution owner. **Independent reviewers:** Security lead, AI lead, Finance, service owner and account lead.

### Technical and security review

- Confirm model/version, API, deployment type, region and actual subscription quota. Validate private connectivity for the selected architecture rather than a different reference design.
- Verify public access denial, private DNS, build/operator paths, outbound dependencies and deployment/runtime identity separation.
- Run allowed-user, denied-user, revoked-access and forbidden-citation tests. Proposed pass condition: zero forbidden content in the agreed test population. Test results do not prove all future permission behaviour.
- Run injection and sensitive-data tests. Verify log redaction and access. Record exceptions and their risk owners.
- If an optional gateway is proposed, distinguish supported APIM AI policies from the separate preview AI Gateway tier. Record feature maturity, tier, region, networking and support limits.

### Workload and capacity review

- Proposed starting evaluation: 200 held-out questions, at least 85% business-approved answers, with valid citations and abstention cases. Customer approves the scoring rubric and thresholds.
- Proposed load test: 25 concurrent sessions, 20 RPM for 30 minutes, P95 complete answer at or below 15 seconds for agreed sizes. Include retrieval, query embeddings, model generation, throttling, retries and errors.
- Validate source ingestion and permission propagation. A proposed 15-minute revocation target depends on the source integration and requires proof.
- Demonstrate source restore, redeployment and index rebuild. Proposed RTO is one business day and source-copy RPO is 24 hours. A full-region outage is outside this baseline; do not infer DR from replicas.

### Commercial and operational review

- Recalculate role costs, reserve, services fee, token volumes, monthly totals, first-year cost and tower credits independently.
- Replace budget allowances with a dated Azure calculator/contract estimate. Include transactions, retention, snapshots, network transfer and peak scaling. Validate annual totals using displayed quoted amounts.
- Confirm the delivery mix and weekly allocations. Three monthly operations role days do not create dedicated 8×5 staffing. Confirm the shared service pool and specialist response agreements.
- Confirm that the benefit is a hypothesis. Measure task time, corrections and realization. Labor capacity value is not cash savings.

### Presentation and online review

- Inspect every slide at presentation size. Remove clipping, awkward wrapping, tiny reference labels and crowded footers.
- Confirm that main design diagrams, text and tables are editable. Retain original detailed Microsoft images in the appendix.
- Open the exported PPTX in PowerPoint Online. Check Gellix substitution, table expansion, arrows, notes, links and representative edits. Save, reopen and recheck.
- The assistant's local rendering and package checks do not count as PowerPoint Online verification.

**Outputs:** signed review checklist, calculation reconciliation, technical test evidence, residual risk register, online compatibility result and defect log.

**Exit gate:** no open critical technical/commercial blocker; all proposed acceptance conditions have an approver; all online layout defects are closed or explicitly accepted.

## 4. ACT: days 16–20

**Accountable:** leadership sponsor. **Responsible:** integrated solution owner and each finding owner.

1. Classify findings as release blockers, bounded pilot limitations or accepted residual risks. Every exception needs an accountable approver and expiry/review date.
2. Correct the design, resource estimate, support model and decks together. Rerun affected tests and calculations after changes.
3. Confirm approved internal assets and maintainers. Remove unverified capability claims from external copy.
4. Obtain Finance approval, tower delivery commitments, service acceptance and sponsor release decision.
5. Release a controlled offering version and evidence pack. Record the source repository commit, deck version, architecture decisions, estimate date and change history.
6. Choose one outcome: launch a bounded pilot, revise and repeat the cycle, or stop investment. Do not label a reference deck as a signed customer proposal.

**Outputs:** release decision, approved version, known limitations, evidence register and next PDCA backlog.

**Exit gate:** the sponsor names the permitted audience and use. Deal-specific commercial and customer approvals remain required for every quotation.

## Audit recommendation register

| ID | Priority | Recommendation and action | Accountable owner | Due | Evidence / gate | Revision 2 status |
|---|---|---|---|---|---|---|
| A01 | Critical | Add customer blocker, buyer and measurable value hypothesis | Account lead | Day 3 | Account feedback and baseline owner | Deck applied; account evidence pending |
| A02 | Critical | Establish one primary offer with entry and recurring companions | Infra sponsor | Day 3 | Accepted portfolio boundary | Deck applied; sponsor approval pending |
| A03 | Critical | Select one architecture and produce editable flow diagrams | Solution owner | Day 7 | Design decisions and peer review | Deck applied; tenant feasibility pending |
| A04 | Critical | Build a priced USD example and separate cost lines | Finance | Day 8 | Approved rates and dated Azure quote | Sample model applied; actual quote pending |
| A05 | Critical | Specify BOM by environment, SKU and quantity | Infra architect | Day 8 | Region, capacity and calculator evidence | Candidate BOM applied; validation pending |
| A06 | High | Pin model/API/deployment type and private network path | AI lead | Day 7 | Model lifecycle, quota and path tests | Candidate decisions applied; tests pending |
| A07 | High | Distinguish APIM capabilities from preview gateway tier | Infra architect | Day 7 | Tier/maturity decision record | Distinction applied; option unpriced |
| A08 | High | Separate agentic retrieval from autonomous actions | AI lead | Day 7 | Scope, threat model and action test pack | Baseline and optional scope separated |
| A09 | High | Specify ACL enforcement, revocation and citation authorization | Security lead | Day 10 | Persona and revoked-access tests | Proposed controls applied; proof pending |
| A10 | High | Add weekly resource loading and review gates | Delivery lead | Day 8 | Tower allocation and availability | Base loading applied; staffing pending |
| A11 | High | Set proposed measurable acceptance targets | Workload owner | Day 10 | Signed rubric and test thresholds | Targets applied; customer approval pending |
| A12 | High | Define recovery boundary and test method | Service owner | Day 10 | Restore and re-index evidence | Targets applied; recovery tests pending |
| A13 | High | Price operating coverage and resolver OLAs | Service owner | Day 10 | Pool capacity and service schedule | Sample allowance applied; coverage pending |
| A14 | High | Demonstrate reconciled tower revenue allocation | Finance | Day 8 | Ledger totals and attribution policy | Worked example applied; policy pending |
| A15 | High | Validate exact Cognizant assets and approved reuse | Practice owner | Day 10 | Owner, licence, maintenance and evidence | Unverified candidates clearly held back |
| A16 | Medium | Improve narrative and move dense references to appendix | Solution owner | Day 10 | Slide review at presentation size | Main story and appendices rebuilt |
| A17 | Medium | Add RACI legend and integrated ownership | Delivery lead | Day 8 | Accepted tower responsibilities | Legend and ownership applied |
| A18 | High | Verify PowerPoint Online usability and font fallback | Proposal owner | Day 15 | Open/edit/save/reopen result | Local checks only; online review pending |
| A19 | High | Define country-specific market and processing decisions | Account lead | Day 5 | Customer geography and commercial record | EU/US candidates applied; other countries separate |
| A20 | High | Set release authority and repeatable PDCA governance | Infra sponsor | Day 20 | Recorded launch/pilot/revise decision | Plan applied; release approval pending |

## Commercial calculation baseline in the revised decks

All inputs below are synthetic planning assumptions. They are not Cognizant policy or published Azure prices. Reserve and gross margin treatment require Finance approval.

| Tower | Base role days | Sample USD cost/day | Base cost | Sample services credit including reserve and margin |
|---|---:|---:|---:|---:|
| Infra | 40 | 500 | 20,000 | 32,857.14 |
| Security | 8 | 600 | 4,800 | 7,885.71 |
| DevOps | 12 | 500 | 6,000 | 9,857.14 |
| Data | 4 | 550 | 2,200 | 3,614.29 |
| Data Engineering | 12 | 500 | 6,000 | 9,857.14 |
| AI | 12 | 650 | 7,800 | 12,814.29 |
| Total | 88 | | 46,800 | 76,885.71 |

- Reserve cost = $46,800 × 15% = $7,020. Planning cost = $53,820.
- Implementation services fee = $53,820 / (1 − 30%) = $76,885.71, rounded to cents.
- Operations cost = 2 Infra days × $500 + 0.5 Security day × $600 + 0.5 AI day × $650 = $1,625/month. Sample fee = $1,625 / 0.70 = $2,321.43/month.
- Base model budget = 60M input tokens × $5/M + 15M output tokens × $15/M = $525/month. Other Azure budget = $1,975/month. Total base Azure budget = $2,500/month.
- First-year baseline = $76,885.71 + 12 × ($2,500 + $2,321.43) = $134,742.87.
- Optional assessment = 12 base days across Infra 6, Security 2, Data 1, AI 2, DevOps 1. Cost $6,550 + 15% reserve, divided by 0.70 = $10,760.71. It is excluded from first-year baseline and is not automatically credited.
- No automatic FX conversion, tax, licence, regional DR, APIM, OCR or unlimited resolver support is included.

## Ongoing PDCA after release

Monthly: review adoption, quality, incidents, source/permission freshness, cost per accepted answer and support allowance usage. Service owner opens actions with due dates and reviewers.

Quarterly: review offer demand, win/loss reasons, package margin, delivery variance, reuse assets and model/service lifecycle. Sponsor decides continuation and investment.

Event-triggered: repeat architecture, security, quality and cost checks after model/version changes, prompt changes, source/schema changes, permission changes, new tools, a new geography or changed support coverage. Change control updates the design, quote and SOW together.

## Evidence and sources

- Project source snapshot: https://github.com/upendra25312/AI-Foundry-GTM-offering-/tree/ad3af1ef8701abbcf05ee926c2f9e09ca8d346f4
- Source proposal: CIS_Infra_Azure_AI_Platform_GTM_Proposal_V3.docx; workbook: Microsoft_AI_Architect_Learning_Roadmap.xlsx; brand reference: Cognizant_Branded_Presales_Template.pptx.
- Custom application RAG reference: https://github.com/Azure-Samples/azure-search-openai-demo
- Private deployment guidance: https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/docs/deploy_private.md
- Access-control reference: https://github.com/Azure-Samples/azure-search-openai-demo/blob/main/docs/login_and_acl.md
- Model API: https://learn.microsoft.com/en-us/azure/foundry/openai/api-version-lifecycle
- Deployment processing boundaries: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types
- APIM AI capabilities: https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities
- Dedicated gateway preview: https://learn.microsoft.com/en-us/azure/api-management/ai-gateway-overview
- Foundry Agent Service setup options: https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/networking-options
- Microsoft 365 architecture: https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-architecture

Technical guidance reviewed 10 October 2026. Confirm current support and pricing at the deal design and quote date.
