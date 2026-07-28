from evaluator import numeric_eval


def evaluate(expected, actual):
    return numeric_eval(expected, str(actual))