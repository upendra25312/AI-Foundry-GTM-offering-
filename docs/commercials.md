# Sizing and commercial templates

Do not present these fields as Cognizant-approved rates or Microsoft quotes. Fill them using approved internal tools, current Azure pricing, customer entitlements, and commercial review. Keep delivery fees, Azure consumption, licensing, and managed operations distinct. All amounts are USD; document exchange-rate, tax, discount, and quote-date treatment separately.

## 1. Delivery estimate (services fees)

Estimate role effort independently; use actual approved delivery rates and commercial assumptions.

| Work package / role | Unit | Quantity | Effort per unit | Total effort | Approved rate (USD) | Fee (USD) | Source / approver |
|---|---:|---:|---:|---:|---:|---:|---|
| Discovery and assessment | day | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Architecture and security coordination | day | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Platform/network/IaC implementation | day | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Validation and handover | day | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Project/service transition management | day | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| **Delivery fee total** |  |  |  | **Σ effort** |  | **Σ fees** |  |

Formula per line: `total effort = quantity × effort per unit`; `fee = total effort × approved role rate`. Add contingency only with an explicit basis and approval. Do not blend internal rates with Azure consumption.

## 2. Azure consumption estimate (customer usage)

For each service, collect a usage driver and current public or contract price. Verify currency, region, model/deployment type, SKU, tier, meter, discounts, and billing period in the official pricing tool at quote time. Model low/base/high scenarios; expose uncertainty rather than imply precision.

| Service/meter (confirm name) | Region/SKU/model | Driver and quantity | Unit price (USD) | Period | Estimated cost | Price source/date | Assumption / owner |
|---|---|---:|---:|---|---:|---|---|
| AI model inference | [ ] | requests/tokens by input/output [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Search/index | [ ] | tier/replicas/partitions or equivalent [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Storage/data transfer | [ ] | capacity/transactions/egress [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Network/private connectivity | [ ] | gateways/endpoints/data processed [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Monitoring/log retention | [ ] | ingestion/retention [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Other required services | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| **Azure consumption subtotal** |  |  |  |  | **Σ lines** |  |  |

Include environment uptime, scale/replica count, token or transaction profile, indexing, retention, egress, backup, and DR assumptions. Record whether estimates include taxes, support, reservations/commitments, discounts, and free grants. Grants are not assumed. Prices and regional/model availability change; revalidate before proposal and deployment.

## 3. Licensing and third-party costs

| Product/license | Quantity/user or unit | Term | List/contract price (USD) | Discount/entitlement evidence | Total | Owner/source/date |
|---|---:|---|---:|---|---:|---|
| [Customer/Microsoft/third-party license] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| **Licensing subtotal** |  |  |  |  | **Σ lines** |  |

Confirm tenant entitlements, SKU requirements, licensing metric, eligibility, and contract terms with procurement/licensing owners. Do not assume Azure service consumption includes product, Microsoft 365, or third-party licensing.

## 4. Managed operations (recurring)

| Service component / coverage | Unit (month, component, event) | Quantity | Approved recurring rate (USD) | Monthly amount | Annual amount | SLA/service-description reference |
|---|---|---:|---:|---:|---:|---|
| Transition-in (one-time) | [ ] | [ ] | [ ] | [ ] | N/A | [ ] |
| Platform monitoring and response | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Service review / FinOps | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Additional hours/on-call | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| **Managed operations subtotal** |  |  |  | **Σ monthly** | **Σ annual** |  |

State service hours, support boundaries, exclusions, response/restore targets, escalation, volume limits, indexation, and transition assumptions. No SLA exists unless included in an approved executed agreement.

## Commercial roll-up and approvals

| Category | USD | Basis / approval |
|---|---:|---|
| One-time delivery fees | [ ] | [ ] |
| Azure consumption (recurring estimate) | [ ] | Customer usage estimate—not service fees |
| Licensing/third-party costs | [ ] | [ ] |
| Managed operations recurring fees | [ ] | [ ] |
| Taxes, FX, discounts, contingencies | [ ] | [ ] |

**Proposed revenue allocation:** document any tower allocation separately as a proposal, including rationale and margin/ownership implications. It is not approved until the authorized Cognizant finance/commercial stakeholders approve it in writing. Do not infer allocation percentages from this toolkit.

**Required before quote:** approved role rate source; pricing-tool output/quote date; forecast and scenarios; license validation; service availability/quota check; assumptions and exclusions; internal finance/commercial approvals; customer acceptance of consumption owner and budget alerts.
