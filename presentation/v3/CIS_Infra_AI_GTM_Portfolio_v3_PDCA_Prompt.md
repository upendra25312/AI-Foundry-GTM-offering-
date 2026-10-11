# Regenerate the CIS Infra Azure AI GTM Portfolio (Version 3.0) using PDCA

## 1. Role and objective

Act as an integrated review and build team:

- Azure solution architects (platform, networking, identity, AI services)
- CIS Infra offering leaders and presales leads
- FinOps specialists (Azure consumption, provisioned throughput, Microsoft licensing)
- Security architects (AI threat modelling, identity, data security)
- Responsible AI and regulatory advisers (EU, UK, Middle East)
- Microsoft partner and alliance specialists (co-sell, Marketplace, partner funding)
- Executive presentation designers and editors

Upgrade the Version 2.0 portfolio to Version 3.0. Work in **Plan, Do, Check, Act (PDCA) cycles**:

1. Apply the known recommendations listed in section 4.
2. Run a fresh, independent audit of the result.
3. Apply the new findings.
4. Repeat until the exit criteria in section 9 are met.

Deliver finished, editable files. Do not stop at a plan, an outline or sample slides.

## 2. Inputs

Inspect every input before relying on it. Ignore unrelated attachments.

| Input | Location | Use |
|---|---|---|
| Version 2.0 decks (5) | `CIS_Infra_AI_GTM_Portfolio_v2.0.zip`, folder `1_Presentations` | Baseline to improve |
| Version 2.0 architecture sources | `3_Architecture_Sources` | Editable diagrams to reuse |
| Version 2.0 registers | `4_Registers` (audit closure, source register, decision register) | Baseline evidence and open decisions |
| Azure icons | `5_Icons_SVG`, plus https://az-icons.com/ and https://learn.microsoft.com/en-us/azure/architecture/icons/ | Official icons only |
| GTM proposal V3 | https://github.com/upendra25312/AI-Foundry-GTM-offering-/ (root `.docx`) | Business context, RACI baseline, worked estimate, competitor benchmark |
| Reference architectures | https://github.com/upendra25312/AI-Foundry-GTM-offering-/tree/main/architectures | Source diagrams and Visio files |
| Branded template | Same repository, `Cognizant_Branded_Presales_Template.pptx` | Brand, palette and layouts |

If an input is missing, say so at the top of the work log, proceed with documented assumptions, and list the gap in the handover.

## 3. Business rules (unchanged from Version 2.0)

- These offerings originate in **Cognizant CIS Infra**. Security, DevOps, Data, AI and Data Engineering are separate towers.
- For every activity, make clear what CIS Infra sells, delivers and operates; what needs another tower; what the customer owns; who is accountable for the integrated outcome; and how cost and revenue are attributed.
- Do not imply CIS Infra owns model quality, application behaviour, data quality or security operations unless an agreed service includes them.
- Do not invent Cognizant-approved offerings, rates, staffing commitments, revenue policies, customer credentials or pipeline.
- Label every number as one of: **Verified** (with source and date), **Estimate** (with its basis), **Illustrative**, **Hypothetical** or **Synthetic**. Never present an estimate as approved terms.
- Mark custom diagrams "Proposed reference architecture". Never imply Microsoft endorsement.
- No em dashes or en dashes in slide text or notes.

## 4. Known recommendations to apply (PDCA cycle 1, "Do")

Treat each item as a tracked work item with an ID. Record its closure in the audit closure report.

### 4.1 Portfolio and commercial

| ID | Recommendation | Acceptance evidence |
|---|---|---|
| P1 | Build a **sixth, master portfolio deck** (10 to 12 executive slides plus appendix): the offering family, the entry offer, sequencing, combined economics, the Microsoft adjacency map, the decisions requested and a 30-day validation plan. | Deck 00 exists; every other deck links back to it |
| P2 | Replace "formula only" pricing with **labelled low, mid and high ranges** for effort (role days), elapsed duration and indicative fee band per package. Derive them from the V3 worked example (88 role days for a bounded extension) and state every assumption. Keep the formula and the missing approved input visible. | Every package has a range table marked "Estimate, not approved" |
| P3 | Add a **demand and "why now" case**: market drivers, buying triggers, target segments and a qualification scorecard. Use public sources only. Do not claim pipeline or customers that do not exist. Provide an empty account-shortlist template. | Sourced slide plus scorecard in each deck |
| P4 | Restore **competitive positioning** from the V3 benchmark (Accenture and Avanade, TCS, KPMG, EPAM, EY, PwC, Deloitte, Wipro). Add "why Cognizant CIS Infra" proof points, labelled as claims to validate. | Positioning slide in deck 00; battlecard in appendix |
| P5 | Add the **Microsoft partner motion**: co-sell, Azure Marketplace, partner designations and current Microsoft partner funding programmes. **Verify current programme names and eligibility on Microsoft sources before use.** | Verified sources in register |
| P6 | Add a **portfolio P&L view**: how the packages combine into a typical first-year deal, with services revenue separated from customer Azure and licence spend. Hypothetical only, clearly labelled. | Chart in deck 00 |

### 4.2 Microsoft 365 Copilot, Copilot Studio, Agent 365 and Azure API Center

Verify every fact below on current Microsoft sources before use and record it in the source register. Facts checked on 11 Oct 2026:

- **Agent 365:** GA on 1 May 2026. $15 per user per month standalone, or included in Microsoft 365 E7. Registry covers Microsoft, Copilot Studio, Foundry and partner agents; AWS and Google registry sync is in preview; lifecycle start, stop and delete announced as coming soon.
- **Entra agent identity protection and Conditional Access for agents:** now tied to Agent 365 licensing.
- **Azure API Center:** private registry for APIs and MCP servers, with sync from API Management and integration with Foundry tool catalogues.
- **Copilot Studio:** pay-as-you-go credits are billed through Azure.

| ID | Recommendation | Acceptance evidence |
|---|---|---|
| M1 | Add a **Microsoft 365 and Copilot adjacency map** to deck 00 and every portfolio slide. M365 Copilot is a handoff to the owning Cognizant practice, not a CIS Infra offering. CIS Infra provides identity, network and Purview readiness inputs. If the owning practice is unknown, show "Owning practice: to confirm" and add it to the decision register. | Map slide; decision register entry |
| M2 | **Rebuild deck 02 (Agent Governance) on a "configure before build" principle.** First layer: Agent 365 plus the Foundry Control Plane. Custom build (registry, reconciliation, containment orchestration) only for documented gaps: unlicensed customers, uncovered runtimes, usage-reconciliation evidence, and cross-layer containment. Include a build-versus-buy comparison and a licence prerequisite check. | Revised architecture, coverage matrix and build-versus-buy slide |
| M3 | Treat **Copilot Studio agents as a covered runtime** in decks 02, 03, 04 and 05. Cover inventory, Entra controls, routing custom connectors through API Management, use of Foundry models and AI Search, Copilot credit consumption and operational ownership. Power Platform environment administration stays with the platform team. | Coverage matrix, RACI rows and cost lines updated |
| M4 | Add **Azure API Center** to deck 03 as the tool and MCP server registry, paired with API Management as the traffic control point. Show how an approved MCP allow-list is enforced. Add a tool-governance slide and an editable architecture. | Architecture plus GA or preview status verified |
| M5 | Add **Entra Agent ID and Conditional Access for agents** as a containment and access layer in the kill-switch architecture. Add Defender runtime blocking where applicable. Restate the limits. | Kill-switch K1 to K4 updated in decks 02 and 05 |
| M6 | Add **licence economics** to deck 04: Agent 365 per user, E7 bundle, Copilot credits (capacity pack, pay-as-you-go, pre-purchase) alongside Azure tokens and PTU. Present this as advisory input, not licence resale advice. | Cost-layer slide and worked example |

### 4.3 Security, regulation and responsible AI

| ID | Recommendation | Acceptance evidence |
|---|---|---|
| S1 | Add an **AI threat model** appendix in every deck, scoped to that offering: prompt injection, data exfiltration, tool misuse, model abuse, supply chain and the MCP server trust boundary. Map each to a control and an owning tower. Reference OWASP Top 10 for LLM Applications (verify the current version). | Threat-to-control table |
| S2 | Add **Defender for Cloud AI threat protection, Purview data security for AI and Microsoft Sentinel** positioning, with the Security tower as owner. CIS Infra provides telemetry plumbing only. Verify current product names and status. | Security architecture slide |
| S3 | Add a **regulatory and responsible-AI slide** for the EU, UK and Middle East: EU AI Act obligations and application dates, UK guidance, UAE and Saudi data protection, and ISO/IEC 42001. **Verify dates and status; state uncertainty explicitly.** Cognizant gives no legal advice. | Sourced slide with "not legal advice" note |

### 4.4 Deck-specific fixes

| ID | Deck | Recommendation |
|---|---|---|
| D01a | 01 | Name the Microsoft AI Landing Zones accelerator and Azure Verified Modules as reuse assets. Quantify the reuse saving as an estimate. |
| D01b | 01 | Add data platform paths (Fabric or OneLake, Storage, AI Search) and a disaster-recovery options slide (single region, warm standby, active-active) with cost and RTO drivers. |
| D01c | 01 | Add effort and duration ranges for assess, extend, establish and transition. |
| D03a | 03 | Add a gateway choice slide: API Management (GA tiers), the AI Gateway tier (preview), the Foundry built-in AI gateway (preview) and third-party gateways. Use decision criteria, not a recommendation. |
| D03b | 03 | Add latency overhead considerations and a test method (do not invent figures), semantic caching economics and a multi-tenant chargeback model. |
| D04a | 04 | Replace gpt-4.1 in the worked example with a current GA model. Verify price, PTU parameters and retirement date. Keep the old example only if it explains model-lifecycle risk. |
| D04b | 04 | Redesign the break-even chart so an executive can read it in 10 seconds. One message, annotated, plus a plain-English sentence. |
| D04c | 04 | Add a FinOps operating model: FOCUS-format cost exports, showback and chargeback, unit economics per useful task, and a monthly review cadence. |
| D05a | 05 | Link proposed response targets to a staffing model and price range. Add ITSM integration (for example ServiceNow, verify connector options), AIOps options, and exit and transition. |
| D05b | 05 | Add Agent 365 and Copilot Studio operations to the service catalogue, with clear lane ownership. |
| K1 | 02, 05 | Add a **proof-of-concept plan** for the kill switch: scope, synthetic agents, runtimes, measured stop-time method and the evidence pack. Mark the design as unproven until tested. |

### 4.5 Readability and presentation quality

| ID | Recommendation |
|---|---|
| R1 | Redesign executive sections so they are **offering-specific, not templated**. No more than 3 of 10 executive slides may share a layout pattern within a deck, and at most 2 tables per executive section. Use one clear visual per message. |
| R2 | Executive body text 20 to 24 pt. Nothing below 18 pt in executive slides, and nothing below 12 pt anywhere. Simplify content rather than shrinking it. |
| R3 | Add a **glossary** (PTU, TPM, PAYG, APIM, RACI, MCP, A2A, RTO, RPO, FOCUS and every other acronym used) in deck 00 and each appendix. Expand each acronym on first use per deck. |
| R4 | Rewrite speaker notes as a **talk track**: what to say (3 to 5 sentences), the likely question, the answer, and then sources. Executives should be able to present without the author. |
| R5 | Give each complex diagram an **executive one-liner and a three-step story** ("request comes in, gateway decides, model answers"). Keep the technical version in the appendix. |
| R6 | Check consistency across decks: identical names for the same service, role and package; one portfolio map; and consistent hypothetical numbers or clearly separate scenarios. |

## 5. PDCA operating model

Run a minimum of **three cycles**. Cycle 1 applies section 4. Cycles 2 and 3 apply findings from fresh audits. Stop early only if the exit criteria are met after cycle 2.

### PLAN (each cycle)

1. Write the cycle objective and scope.
2. List the work items (IDs) with owner role, target slide or deck, and acceptance evidence.
3. Identify the facts that need verification, and verify them before building. Record the source URL, date checked, product, SKU or tier, region, GA or preview status and limitations.
4. Record assumptions and the open decisions they create.

### DO

1. Edit the decks, diagrams and registers. Reuse the Version 2.0 build sources where possible.
2. Use editable PowerPoint shapes, connectors and native tables and charts. Use only official Azure SVG icons, unmodified and labelled.
3. Keep the source-to-slide trace in speaker notes.

### CHECK: independent audit

Run the audit as if you had not built the decks. If sub-agents are available, use a separate reviewer that has not seen the build reasoning. Score every deck against the rubric in section 6. Produce a findings list with an ID, severity, deck, slide, issue, evidence and recommended fix.

The audit must cover at least:

- **Executive clarity:** can a senior leader state the problem, offer, price range, risk and decision after reading 10 slides?
- **Completeness:** all ten executive questions, the readiness checklist, RACI, attribution and cost layers.
- **Technical accuracy:** service names, GA or preview status, limits, regions and prices against current Microsoft sources.
- **Scope honesty:** tower boundaries, customer duties and no unsupported claims.
- **Microsoft adjacency:** Copilot, Copilot Studio, Agent 365, API Center and Entra Agent ID positioned correctly.
- **Security and regulatory coverage.**
- **Commercial usefulness:** ranges, deal shape, partner motion and qualification.
- **Visual quality:** render every slide and check clipping, overlap, font size, icon accuracy, connector meaning, contrast and layout repetition.
- **Cross-deck consistency.**
- **"Hard to explain" test:** for each executive slide, can its message be said in one sentence? If not, flag it.

### ACT

1. Classify findings as **fix now** (severity critical or high), **fix next cycle** (medium) or **log and accept** (low, with a reason).
2. Update the audit closure report: finding ID, cycle found, action, revised slides, status.
3. Update the decision register with anything that needs a human decision.
4. Start the next cycle's PLAN with the open findings.

## 6. Audit scoring rubric (1 to 5 per dimension, per deck)

| Dimension | 5 means |
|---|---|
| Executive storyline | Clear problem to decision flow; one message per slide; no repetition |
| Commercial clarity | Ranges, deal shape, cost layers and partner motion are clear and labelled |
| Technical accuracy | Every material claim verified and dated; GA and preview distinguished |
| Scope and ownership | Tower, customer and integrated-owner boundaries are unambiguous |
| Microsoft ecosystem fit | Copilot, Agent 365, API Center and Entra positioned correctly; build only where needed |
| Security and compliance | Threat model, controls, owners and regulatory notes present |
| Visual and editorial quality | Readable at presentation size; consistent; no clipping; editable |
| Presentability | Talk track, glossary and simple diagram stories let a non-author present it |

Record scores per cycle in a scorecard sheet so improvement is visible.

## 7. Verification rules

- Use authoritative Microsoft sources (Microsoft Learn, the Azure Retail Prices API, official Microsoft blogs and product pages). Use third-party sources only for licensing context, and label them.
- Distinguish published regional support, subscription quota, deployable capacity, temporary restrictions, resilience features and model processing geography.
- For selected-region comparisons, state that the list is not exhaustive and explain why those regions were chosen (US, EU, UK, Middle East).
- Never present a selected-region view as global availability.
- If a fact cannot be verified, say so on the slide and in the register, and do not build a recommendation on it.

## 8. Deliverables

Use versioned file names (`v3.0`).

1. Six editable PPTX decks: 00 Portfolio Overview (new), and 01 to 05 revised.
2. A PDF preview of each deck.
3. Editable architecture source files for every new or changed diagram.
4. Audit closure report (`.xlsx`): one sheet per PDCA cycle, plus the rubric scorecard.
5. Source register (`.xlsx`): Microsoft sources, verified values, architecture references, icon register.
6. Decision register (`.xlsx`) of unresolved business decisions, with owners and timing (now, after pilot, Finance approval, tower agreement).
7. A one-page **PDCA summary**: cycles run, findings per cycle by severity, score movement, remaining risks.
8. A ZIP bundle of all of the above, with a README.

## 9. Exit criteria

Stop only when all of the following are true:

- No open critical or high findings.
- Every rubric dimension scores at least 4 for every deck, and executive storyline and commercial clarity score 5 for deck 00.
- Every known recommendation in section 4 is closed or explicitly deferred, with a reason and owner.
- Every slide has been rendered and inspected after its last edit.
- Zero em or en dashes, and no placeholder text.
- File validation passes for every PPTX.

## 10. Handover statement

Open the handover with:

- What changed from Version 2.0, in five lines or fewer.
- Inputs that were missing and the assumptions used.
- Whether the files were opened in desktop PowerPoint. Do not claim this if only rendered previews were checked.
- Font substitutions (for example Arial for Gellix).
- The top open decisions leadership must take, and who owns each.

## 11. Execution instructions

- Proceed with the available information. Ask only when a missing input would materially change scope or create an unsupported commitment. Otherwise assume, label and log.
- Two items need human confirmation. If they are still unanswered, use the stated default and log it:
  - **Which Cognizant practice owns Microsoft 365 Copilot?** Default: "Owning practice to confirm".
  - **Will leadership accept labelled cost and effort ranges?** Default: yes, marked "Estimate, not approved".
- Finish all decks, run every PDCA cycle, review every slide and share the final files. Do not return only a plan or a partial sample.
