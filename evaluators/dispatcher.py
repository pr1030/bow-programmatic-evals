from evaluators.numeric import evaluate as numeric
from evaluators.string import evaluate as string
from evaluators.contains import evaluate as contains
from evaluators.boolean import evaluate as boolean


def evaluate(evaluator, expected, actual):

    evaluators = {
        "numeric": numeric,
        "string": string,
        "contains": contains,
        "boolean": boolean,
    }

    if evaluator not in evaluators:
        raise ValueError(f"Unknown evaluator: {evaluator}")

    return evaluators[evaluator](expected, actual)