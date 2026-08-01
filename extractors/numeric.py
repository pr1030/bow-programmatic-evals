def extract_numeric(rows):
    """
    Returns the first numeric value found in the first row.
    """

    if not rows:
        return None

    row = rows[0]

    for value in row.values():

        if isinstance(value, (int, float)):
            return value

        try:
            return float(value)
        except:
            pass

    return None