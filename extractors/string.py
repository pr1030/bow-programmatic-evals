def extract_string(rows):
    """
    Returns the first string value found.
    """

    if not rows:
        return None

    row = rows[0]

    for value in row.values():

        if isinstance(value, str):
            return value

    return str(next(iter(row.values())))