import json

from evaluators.numeric import numeric_eval
from evaluators.string import string_eval


async def run_tests(session, report_id, test_cases):

    results = []

    for index, test in enumerate(test_cases, start=1):

        prompt = test["prompt"]
        expected = test["expected"]

        data_result = await session.call_tool(
            "create_data",
            {
                "report_id": report_id,
                "prompt": prompt
            }
        )

        data_response = json.loads(data_result.content[0].text)

        rows = data_response.get("data_preview", {}).get("rows", [])

        if not rows:

            actual = "NO DATA RETURNED"
            passed = False

        else:

            actual = list(rows[0].values())[0]

            from evaluators import get_evaluator

            evaluator = get_evaluator(test["evaluator"])

            passed = evaluator(expected, actual)

        results.append(
            {
                "test": index,
                "prompt": prompt,
                "expected": expected,
                "actual": actual,
                "passed": passed
            }
        )

    return results