import re


def extract_number(text):
    """
    Extract the first decimal or integer number from a string.
    """
    match = re.search(r"\d+(\.\d+)?", text)

    if match:
        return float(match.group())

    return None


def numeric_eval(expected, response):
    """
    Compare the expected value with the value found in the response.
    Returns True if they match, otherwise False.
    """
    actual = extract_number(response)

    if actual is None:
        return False

    return actual == expected