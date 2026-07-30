from evaluators.numeric import numeric_eval
from evaluators.string import string_eval
from evaluators.boolean import boolean_eval
from evaluators.contains import contains_eval


def get_evaluator(name: str):
    """
    Returns the evaluator function based on its name.
    """

    evaluators = {
        "numeric": numeric_eval,
        "string": string_eval,
        "boolean": boolean_eval,
        "contains": contains_eval,
    }

    if name not in evaluators:
        raise ValueError(f"Unknown evaluator: {name}")

    return evaluators[name]