# Prompt: CIS Infra Azure AI GTM portfolio v4.0 (leadership-ready revision)

## 1. Role

Act as a combined review and build team:

- Azure solution architects (Foundry, API Management, API Center, Agent 365, Entra)
- CIS Infra offering leaders and delivery leads
- Presales solution architects and bid managers
- Account and client partners
- Security architects and a CISO delegate
- Microsoft alliance managers
- FinOps and commercial finance specialists
- Senior directors who approve new offerings
- Executive presentation designers
- Reviewers who apply three well-known consulting lenses:
  - **Strategy and storyline** (McKinsey-style): answer first, action titles, MECE, sizing the prize.
  - **Operating model, commercial risk and responsible AI** (PwC-style).
  - **Assurance and audit-readiness** (KPMG-style).

These are **review lenses only**. Do not claim the opinion of any real firm. PwC and KPMG are named in the competitor battlecard, so nothing in this work is shared with them.

Prepared by: **Upendra Kumar**. Every file's properties (Author, Last modified by) must say **Upendra Kumar**. No file, slide, note or register may mention the tool used to prepare it.

## 2. Inputs

- The v3.0 bundle `CIS_Infra_AI_GTM_Portfolio_v3.0.zip`:
  - Decks 00 to 05 (PPTX).
  - Architecture source packs.
  - Audit closure report, source register and decision register (XLSX).
  - Talk tracks (MD) and the PDCA summary (PDF).
- The build sources for v3.0 (python-pptx scripts, `common.py`, `lib.py`, `finops_model.py`, `registers3.py`).
- The GTM proposal V3 (`CIS_Infra_Azure_AI_Platform_GTM_Proposal_V3.docx`) in `github.com/upendra25312/AI-Foundry-GTM-offering`, including:
  - The eight-firm competitor benchmark.
  - The Cognizant source list C1 to C9 (Agent Foundry, Neuro AI, Microsoft Business Group and others).
- The Cognizant branded presales template in the same repository.

## 3. Non-negotiable constraints

1. **Keep all five offerings and the master deck.** Leadership decides which offerings to validate. Do not narrow the portfolio. Deck 00 must present the five as options, then give a clearly labelled author recommendation that leadership may accept or reject.
2. **Do not invent Cognizant facts.** This covers rates, margins, staffing, revenue targets, customer names, references, pipeline, certifications or approvals.
   - Where a number is needed and not supplied, use a clearly labelled **"Input required: <owner>"** field. Do not use a made-up figure.
   - The only exception is the existing illustrative rate of $1,000 per role day. Keep it, labelled as illustrative, until Finance supplies a blended rate.
3. **Verify every Microsoft fact** on Microsoft Learn, the Azure Retail Prices API or official Microsoft blogs, dated 11 Oct 2026 or later. Label third-party sources as third party. If a fact cannot be verified, say so on the slide and do not build a recommendation on it.
4. **No em dashes or en dashes** anywhere: slides, notes, tables, registers or file names.
5. **Labels on custom work:**
   - Custom designs carry "Proposed reference architecture".
   - Hypothetical, synthetic and illustrative figures carry those labels.
6. **Speaker notes on every slide**, in this order:
   - TALK TRACK (Say, Likely question, Answer)
   - DETAIL AND CAVEATS
   - Sources
   - Status
7. **Brand and type sizes:**
   - Use the Cognizant presales template, official Azure icons and editable diagrams.
   - Executive body text is 18 to 24 pt. Diagram labels are no smaller than 12 pt.
   - Appendix tables are no smaller than 12 pt. Split a table rather than shrink it.
8. Versioned file names use `v4.0`.

## 4. Recommendations to apply

Each item has an ID, a description and an acceptance test. Log every item in the audit closure report with its status and the slides it changed.

### 4.1 Leadership decision and storyline (L)

| ID | Recommendation | Acceptance test |
|---|---|---|
| L1 | Make the ask concrete. For each offering leadership selects, show the 90-day validation budget, the named sponsor and owner, the headcount, the stop rules and the success measures. Use "Input required" fields for amounts and names not supplied. | Deck 00 decision slide lists all five fields for every offering |
| L2 | Keep the five-option comparison (deck 00, slide 9). Add a labelled **author recommendation** box ("If we had to choose one or two, we would choose X because Y"). It must state that leadership decides. | Recommendation visible, labelled, with reasoning |
| L3 | Rewrite every executive slide title in all six decks as an **action title** that states the finding, not the topic. Maximum 60 characters. | No topic-only titles in any executive section |
| L4 | Make the storyline **answer first**: slide 2 of each deck states the answer and the ask before any context. | Reviewer can state the ask after slide 2 |
| L5 | Make the offerings **MECE**. Assign one owning offering for each shared capability: kill switch (02 builds, 05 operates), chargeback (03 builds the data, 04 designs the model), monthly reviews (05 runs, 04 supplies method). Add an ownership matrix to deck 00. | No capability claimed by two offerings without a stated split |
| L6 | Add a **horizons view** to deck 00. Show what earns revenue this year (likely 04, 03), what builds the platform (01, 05) and what is an emerging bet (02). | One slide, one visual |
| L7 | Add a **12-slide leadership pack** for live presentation, built from deck 00 plus one slide per offering. Keep the full decks as backup. | Pack exists; full decks referenced as backup |

### 4.2 Business case and economics (B)

| ID | Recommendation | Acceptance test |
|---|---|---|
| B1 | **Size the opportunity** per offering. Use target accounts × attach rate × average deal size, over one and three years. Every input is either sourced or an "Input required" field with an owner (account leadership, Finance). | Sizing table per offering in deck 00 appendix, formula visible |
| B2 | Add an **investment case**. Show what Cognizant must spend before the first sale: lab environment, accelerators, certifications, enablement, bench and presales time. Then show payback per offering. Amounts are "Input required" where not supplied. | Investment and payback table in deck 00 |
| B3 | Add **margin with delivery mix** (onshore, nearshore, offshore). Show the formula and leave rates as Finance inputs. Replace "no margin shown" with a margin structure. | Margin structure per offering |
| B4 | Add a **customer value metric** per offering, such as cost per useful AI task, time to production, audit findings closed or incidents contained. Show it on each offering's summary slide. | One value metric per offering, not only cost and control |
| B5 | State **revenue recognition** per offering: fixed-price milestones versus monthly managed service. Give a Finance owner for each. | Row in each deck's cost layers slide |
| B6 | Reframe the Microsoft story around **Azure consumption**. Governed platforms unblock production workloads, which grows consumption. Keep the honest FinOps message in deck 04, but add the consumption narrative to decks 00, 01, 03 and 05. | Consumption narrative present without contradicting deck 04 |

### 4.3 Delivery objections (DL)

| ID | Recommendation | Acceptance test |
|---|---|---|
| DL1 | Add a **skills and bench plan** per offering: roles, required skills (Agent 365, API Center, MCP, Entra agent controls, APIM, Foundry), certifications and ramp-up time. Use "Input required" for current bench numbers. | One slide per deck appendix |
| DL2 | Add a **fixed-price risk control** slide in decks 01, 02, 03: assessment before quote, change triggers, contingency approach and acceptance gates. | Present in three decks |
| DL3 | Tie the 24x7 package and P1 response target to a **funded roster and tooling prerequisite checklist** (deck 05). | Checklist on the package slide or adjacent appendix |
| DL4 | Mark every kill-switch claim as **unproven until the PoC passes**. Remove it from any committed scope until then. | No committed scope includes unproven containment |
| DL5 | Show the **estimate basis**. Say where each range came from (the V3 88-role-day example) and add a plan to recalibrate from pilot actuals. | E1 slides updated with recalibration plan |

### 4.4 Presales objections (PS)

| ID | Recommendation | Acceptance test |
|---|---|---|
| PS1 | Build a **customer-facing pitch** of 6 to 8 slides per offering. Remove internal content (tower attribution, internal rates, competitor names, open internal decisions). | Six customer pitches, each passing an "internal content" check |
| PS2 | List the **presales kit** per offering: demo environment, SOW template, estimator, RFP answer bank, objection handling, and case study once available. Show status for each (exists, to build, owner). | Kit table per deck |
| PS3 | Position the paid assessment against **Microsoft or partner-funded assessments**: when to use funding, when to charge, and how to combine them. | Slide in deck 04 and deck 00 partner motion |
| PS4 | Add **RFP-ready answers** for the top 10 technical questions per offering, in a register (XLSX). | Register delivered |

### 4.5 Account team objections (AC)

| ID | Recommendation | Acceptance test |
|---|---|---|
| AC1 | Add an **account play** per offering: where it fits in an existing account plan, typical deal sizes, and expansion path to larger deals. | Slide per offering |
| AC2 | Add a **cannibalisation check** for accounts where Cognizant already runs infrastructure or managed services. State how the new offering extends rather than competes with the existing contract. | Rule in deck 00 and deck 05 |
| AC3 | Finalise **joint-motion rules** with the M365 and D365 teams: deal lead, handoffs, revenue credit and one-team customer narrative. Keep the M365 versus D365 Copilot split as an open decision with an owner. | Deck 00 A3 updated; decision register entry |
| AC4 | Add a **business-led entry story** for each offering, aimed at buyers outside IT, such as the head of operations or the CFO. | One line per offering in the account play |

### 4.6 Security objections (SC)

| ID | Recommendation | Acceptance test |
|---|---|---|
| SC1 | Make **Security co-owner** of Agent 365 policies, Entra Conditional Access for agents, Purview and Defender configuration. CIS Infra implements under Security design. Update RACI and scope slides in decks 02, 03, 05. | RACI shows Security accountable for policy |
| SC2 | Add **kill-switch authority and liability**: who may stop, who may restart, what happens if a stop fails, and the contract position. | Slide in deck 02 and deck 05 |
| SC3 | Add a **data residency qualification gate** for the UK and Middle East. Verify current data zone, regional and global deployment options for the models in scope. State the gaps plainly. | Gate in Q1 and deck 01; verified on Microsoft Learn |
| SC4 | Add **prompt and telemetry data handling**: what is logged, redaction, retention and access for chargeback and observability data. | Slide in decks 03 and 05 |
| SC5 | Replace the generic threat list with an **offering-specific threat model**. Use the latest OWASP LLM Top 10 version (verify), the MCP trust boundary, supply chain and identity threats. | SEC1 in every deck revised |
| SC6 | Replace or flag third-party sources (SAMexpert, the Entra change tracker) with Microsoft sources where possible. | Source register shows Microsoft source or "unconfirmed" |

### 4.7 Microsoft alliance objections (MS)

| ID | Recommendation | Acceptance test |
|---|---|---|
| MS1 | Have the **alliance team co-author** the partner motion slide. Verify current programme names, Azure Accelerate eligibility, co-sell routes for services (not only IP co-sell), Marketplace options and relevant specialisations. | Slide shows verified facts and an alliance owner |
| MS2 | Add a **Microsoft sales motion alignment** slide: which Microsoft seller roles care about each offering, and the consumption outcome each one drives. | Slide in deck 00 |
| MS3 | Reword competitive language that positions against Microsoft (for example "Microsoft does this for free"). Frame offerings as **accelerating adoption of Microsoft products**. | No anti-Microsoft framing remains |
| MS4 | State the **packaged IP route** if co-sell for IP is wanted: what would become a Marketplace listing, and its certification requirement. | Decision register entry |

### 4.8 Senior director objections (SD)

| ID | Recommendation | Acceptance test |
|---|---|---|
| SD1 | Add **internal positioning** against Cognizant Agent Foundry, Neuro AI, the Microsoft Business Group and the AI Operations Assistant, using the V3 proposal C1 to C9 sources. Show who leads what and where CIS Infra adds infrastructure depth. | One slide in deck 00 with each owner named as "to confirm" |
| SD2 | Answer **"why us, why now, why CIS Infra"** in one slide, with proof points labelled as claims to validate. | Slide present |
| SD3 | Answer **"right to win"** against Accenture and Avanade and the other benchmark firms with specific, testable differentiators and the evidence needed to prove each. | Differentiator table with evidence column |
| SD4 | Add a **sign-off status** slide: who has reviewed (tower leads, Finance, Security, alliance, M365 and D365 leads), and their status. | Status table; no review claimed that has not happened |
| SD5 | Add an **offering governance** slide: P&L owner, stage gates (validate, pilot, launch), review cadence and stop rules. | Slide in deck 00 |

### 4.9 Operating model, risk and responsible AI (PwC-style lens) (PW)

| ID | Recommendation | Acceptance test |
|---|---|---|
| PW1 | Add a **contract risk** slide per offering: liability caps, service-level penalties, IP ownership of accelerators and infrastructure code, warranties and change control. | Slide per offering |
| PW2 | Map **EU AI Act roles** (provider, deployer) to each offering and the services that support each obligation. Use verified dates. State that this is not legal advice. | Table in SEC2 |
| PW3 | Add **sector regulation** checkpoints:<br>- EU: DORA and NIS2 for financial and critical sectors.<br>- UAE: personal data protection law.<br>- Saudi Arabia: PDPL and national cybersecurity authority cloud controls.<br>- UK: regulator guidance.<br>Verify each and mark anything unverified. | SEC2 regulatory table extended |
| PW4 | Add a **responsible AI controls** mapping (fairness, transparency, accountability, safety) showing which controls are platform-level (CIS Infra) and which are model or use-case level (AI tower, customer). | One table, owners clear |

### 4.10 Assurance and audit-readiness (KPMG-style lens) (KP)

| ID | Recommendation | Acceptance test |
|---|---|---|
| KP1 | Add an **audit-ready deliverable** to decks 02 and 05: a control matrix and evidence pack, so internal audit can test agent inventory, ownership and containment. | Named deliverable with contents |
| KP2 | Offer an **ISO/IEC 42001 readiness** add-on: scope, effort range and dependency on the customer's management system. | Add-on in deck 02 or 00 |
| KP3 | Add **model risk management** alignment for regulated banks (US SR 11-7 and equivalents). Verify references. | Row in SEC2 and Q1 |
| KP4 | Add a **customer third-party risk** answer set: data handling, access, subcontracting, certifications. Use "Input required" for Cognizant certifications not supplied. | Appendix slide or register |
| KP5 | Every material claim must trace to the source register with a date. Every number must trace to a formula or an "Input required" owner. | Traceability check passes |

### 4.11 Design and editorial (DE)

| ID | Recommendation | Acceptance test |
|---|---|---|
| DE1 | Apply the **Cognizant presales template** and Gellix where installed. If not available, keep Arial and log it. | Template applied or logged |
| DE2 | Raise every diagram label to **at least 12 pt** and every executive text to **at least 18 pt**. Simplify diagrams rather than shrink text. | Automated font-size check passes |
| DE3 | Reduce **hedging chips**: one status chip per slide, and move repeated caveats into notes and the appendix. | Max one chip per executive slide |
| DE4 | Reduce appendix sprawl. Merge or cut appendix slides that repeat content across decks, and keep shared slides (RACI, SEC2, glossary) consistent. | Total slide count reduced with a merge log |
| DE5 | Open and check every deck in **desktop PowerPoint** if available. If not, state that clearly in the handover. | Handover note |
| DE6 | Set file properties: Author and Last modified by = **Upendra Kumar** on every PPTX, XLSX and PDF. | Metadata check passes |

## 5. Method: PDCA, at least three cycles

1. **Plan:**
   - Map each recommendation in section 4 to the decks and slides it changes.
   - List the facts to verify and the inputs required from named owners.
2. **Do:**
   - Apply every item.
   - Rebuild decks from source, render every slide and inspect it.
3. **Check:**
   - Run a fresh audit as the full review team in section 1, as if you had not built the decks.
   - Write findings with ID, severity (critical, high, medium, low), deck, slide, issue, evidence, objection group (delivery, presales, account, security, alliance, senior director, strategy lens, operating-model lens, assurance lens) and fix.
   - Score each deck on the rubric in section 6.
4. **Act:** fix all critical, high and medium findings, and fix or accept low findings with a reason.
5. **Repeat** Check and Act until the exit criteria in section 8 are met.

Where a separate reviewer is available, use it for the Check step so the work is not graded by its builder. Otherwise, state plainly that the audit was a self-review.

## 6. Scoring rubric (1 to 5 per deck, per cycle)

| Dimension | 5 means |
|---|---|
| Executive storyline | Answer first, action titles, one message per slide, clear ask |
| Commercial clarity | Sizing, investment, margin structure, ranges and revenue recognition clear and labelled |
| Leadership decision readiness | Five options compared, author recommendation, concrete ask per option, stop rules |
| Technical accuracy | Every material claim verified and dated; GA and preview distinguished |
| Scope and ownership | Tower, Security, customer, M365 and D365 boundaries unambiguous; MECE offerings |
| Microsoft alignment | Consumption narrative, verified partner motion, no anti-Microsoft framing |
| Security, risk and compliance | Offering-specific threats, residency gate, contract risk, regulation, audit readiness |
| Delivery and presales readiness | Bench plan, presales kit, customer pitch, fixed-price controls |
| Visual and editorial quality | Template, font minimums, no clipping, editable, consistent |
| Presentability | Talk tracks, 12-slide leadership pack, glossary, simple diagram stories |

## 7. Deliverables (v4.0)

1. Six full decks, 00 to 05, editable PPTX with talk-track notes.
2. A 12-slide leadership pack (PPTX).
3. Six customer-facing pitches, one per offering plus a portfolio version (PPTX).
4. PDF previews of every deck and pack.
5. Architecture source packs for every new or changed diagram.
6. Registers (XLSX):
   - Audit closure report: one sheet per PDCA cycle, a findings sheet with objection group, and a rubric scorecard.
   - Source register.
   - Decision register: include every "Input required" item with owner and timing.
   - Inputs-required register.
   - RFP answer bank.
7. Stakeholder objection-handling guide (MD or DOCX). For each group (delivery, presales, account, security, alliance, senior directors), give the objection, the prepared answer and the slide that supports it.
8. One-page PDCA summary.
9. A ZIP bundle with a README.

## 8. Exit criteria

Stop only when all are true:

- No open critical or high findings.
- Every rubric dimension is at least 4 for every deck. Deck 00 scores 5 on storyline, commercial clarity and leadership decision readiness.
- Every section 4 item is closed or explicitly deferred with a reason and an owner.
- Every number is either sourced, calculated from a shown formula, labelled illustrative, or an "Input required" field with an owner.
- Every slide has been rendered and inspected after its last edit.
- Zero em or en dashes and no placeholder text other than labelled "Input required" fields.
- File validation passes for every PPTX.
- File properties show Upendra Kumar as Author and Last modified by.

## 9. Handover note must state

- Which inputs are still required, and from whom (Finance, account leadership, alliance team, tower leads, Security, M365 and D365 leads).
- Whether desktop PowerPoint was used.
- Which fonts were substituted.
- Which facts could not be verified.
- Whether the audit was independent or a self-review.
