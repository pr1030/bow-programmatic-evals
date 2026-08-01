def extract_boolean(rows):

    if not rows:
        return None

    row = rows[0]

    for value in row.values():

        if isinstance(value, bool):
            return value

    return None