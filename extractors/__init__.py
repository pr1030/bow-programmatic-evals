from extractors.numeric import extract_numeric
from extractors.string import extract_string
from extractors.boolean import extract_boolean
from extractors.contains import extract_contains


def get_extractor(name):

    extractors = {
        "numeric": extract_numeric,
        "string": extract_string,
        "boolean": extract_boolean,
        "contains": extract_contains,
    }

    return extractors[name]