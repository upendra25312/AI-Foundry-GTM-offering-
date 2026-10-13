import argparse
import re


DOCUMENTS = (
    (
        "synthetic-platform-policy-01",
        "Urgent service incidents are escalated to the platform owner. "
        "The service owner records the incident and communicates status.",
    ),
    (
        "synthetic-platform-policy-02",
        "Platform changes require an approved change record and a scheduled "
        "maintenance window.",
    ),
    (
        "synthetic-platform-policy-03",
        "Synthetic business documents are reviewed by their data owner before "
        "they are added to a search index.",
    ),
)

STOP_WORDS = {
    "a",
    "an",
    "are",
    "do",
    "does",
    "for",
    "how",
    "i",
    "is",
    "it",
    "of",
    "on",
    "the",
    "to",
    "what",
    "when",
    "where",
    "who",
    "why",
}
MAX_RESULTS = 2


def _terms(text):
    return {
        term
        for term in re.findall(r"[a-z0-9]+", text.lower())
        if term not in STOP_WORDS
    }


def retrieve(question, limit=MAX_RESULTS):
    """Return up to `limit` matching synthetic documents, best match first."""
    if limit <= 0:
        return []
    limit = min(limit, MAX_RESULTS)

    question_terms = _terms(question)
    if not question_terms:
        return []

    ranked = []
    for source_id, content in DOCUMENTS:
        score = len(question_terms & _terms(content))
        if score:
            ranked.append((score, source_id, content))

    ranked.sort(key=lambda result: (-result[0], result[1]))
    return [(source_id, content) for _, source_id, content in ranked[:limit]]


def answer(question):
    matches = retrieve(question)
    if not matches:
        return "No evidence found in the synthetic demo corpus."

    snippets = "\n".join(f"- [{source_id}] {content}" for source_id, content in matches)
    return f"Synthetic evidence (keyword matching only):\n{snippets}"


def main():
    parser = argparse.ArgumentParser(
        description="Search a fixed synthetic corpus (no Azure or network calls)."
    )
    parser.add_argument("question", nargs="*", help="question to search for")
    args = parser.parse_args()
    question = " ".join(args.question) or input("Question: ")
    print(answer(question))


if __name__ == "__main__":
    main()
