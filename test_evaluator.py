import unittest

from evaluator import numeric_eval


class TestNumericEvaluator(unittest.TestCase):

    def test_correct_value(self):
        self.assertTrue(
            numeric_eval(
                8.74,
                "The average movie rating is 8.74."
            )
        )

    def test_incorrect_value(self):
        self.assertFalse(
            numeric_eval(
                8.74,
                "The average movie rating is 8.65."
            )
        )

    def test_no_number(self):
        self.assertFalse(
            numeric_eval(
                8.74,
                "No rating available."
            )
        )


if __name__ == "__main__":
    unittest.main()