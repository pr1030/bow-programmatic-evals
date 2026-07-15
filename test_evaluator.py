import unittest

from evaluator import numeric_eval


class TestNumericEvaluator(unittest.TestCase):

    def test_correct_average_rating(self):
        expected = 8.74
        response = "The average movie rating is 8.74."

        self.assertTrue(numeric_eval(expected, response))

    def test_wrong_average_rating(self):
        expected = 8.74
        response = "The average movie rating is 8.65."

        self.assertFalse(numeric_eval(expected, response))


if __name__ == "__main__":
    unittest.main()