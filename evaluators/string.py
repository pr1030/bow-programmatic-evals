def string_eval(expected, actual):
    """
    Compare two strings (case-insensitive).
    """

    return (
        str(expected).strip().lower()
        == str(actual).strip().lower()
    )