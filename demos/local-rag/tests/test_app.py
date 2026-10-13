import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import MAX_RESULTS, answer, retrieve


class LocalRagTests(unittest.TestCase):
    def test_relevant_question_returns_bounded_synthetic_evidence(self):
        results = retrieve("How are service incidents escalated?")

        self.assertGreater(len(results), 0)
        self.assertLessEqual(len(results), MAX_RESULTS)
        self.assertTrue(all(source_id.startswith("synthetic-") for source_id, _ in results))
        self.assertIn("escalated", results[0][1])

    def test_unrelated_question_returns_no_evidence(self):
        self.assertEqual(
            answer("What is the weather on Mars?"),
            "No evidence found in the synthetic demo corpus.",
        )

    def test_question_without_searchable_terms_returns_no_results(self):
        self.assertEqual(retrieve("How is it?"), [])

    def test_result_limit_is_bounded(self):
        self.assertEqual(len(retrieve("platform service data change", limit=100)), MAX_RESULTS)
        self.assertEqual(retrieve("platform", limit=0), [])


if __name__ == "__main__":
    unittest.main()
