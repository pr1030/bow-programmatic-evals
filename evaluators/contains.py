def contains_eval(expected, actual):

    if isinstance(expected, str):
        expected = [expected]

    actual = str(actual).lower()

    return all(item.lower() in actual for item in expected)