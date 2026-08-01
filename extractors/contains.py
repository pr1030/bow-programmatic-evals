def extract_contains(rows):
    """
    Returns every value from every row.
    """

    values = []

    for row in rows:
        values.extend(row.values())

    return values