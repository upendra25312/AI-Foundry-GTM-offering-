# Local synthetic RAG demonstration

## Status and boundaries

This is a bounded, local-only illustration for presales conversations: retrieve relevant snippets from a tiny synthetic corpus and return them as evidence for a question. It uses deterministic keyword overlap, not an LLM or Azure service. It does **not** demonstrate Azure AI Foundry, Azure AI Search, production security, model quality, customer data handling, or a production-ready RAG architecture.

The demo architecture and constraints were documented in `docs/architecture.md` before implementation.

## Architecture

```text
Question -> normalize and score terms -> rank fixed synthetic documents
         -> return bounded snippets with synthetic source IDs
```

There is no network access, persistence, telemetry, credential use, or cloud resource. The corpus is an inline fictional organization policy excerpt and contains no real customer or employee data.

## Prerequisites and run

- Python 3.9 or newer (standard library only).
- From the repository root: `python demos/local-rag/app.py`
- Run focused tests: `python -m unittest discover -s demos/local-rag/tests -v`
- Example prompt: `How are service incidents escalated?`

## Cost, acceptance, and limitations

- **Expected cost:** USD $0 Azure consumption and $0 license cost because the program is local and makes no external calls. Local compute, if any, is the user's own environment. This is not an estimate for an Azure-connected workload.
- **Acceptance criteria:** (1) script runs without credentials or network access, (2) relevant query returns at most two synthetic source snippets, (3) unrelated query returns an explicit no-evidence response, and (4) tests validate both paths and the output bound.
- **Limitations:** lexical matching only; no embeddings, reranking, chunking pipeline, ACL trimming, LLM generation, content safety, monitoring, private networking, or resilience. Do not infer production readiness or quality from this demo.
- **Azure extension gate:** a separate scoped design must confirm customer data permission/classification, target services and region/model, identity and network/DNS architecture, security approvals, quotas, usage-based cost scenarios, and acceptance tests before any Azure-connected implementation.
