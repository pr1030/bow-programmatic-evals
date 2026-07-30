import re


def extract_number(text):
    """
    Extract the first integer or decimal number from a string.
    """

    match = re.search(r"\d+(\.\d+)?", str(text))

    if match:
        return float(match.group())

    return None


def numeric_eval(expected, actual):
    """
    Compare numeric values.
    Returns True if they match, otherwise False.
    """

    actual_number = extract_number(actual)

    if actual_number is None:
        return False

    return actual_number == float(expected)