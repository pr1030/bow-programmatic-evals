import json

from evaluators import get_evaluator
from extractors import get_extractor


async def run_tests(session, report_id, test_cases):

    results = []

    for index, test in enumerate(test_cases, start=1):

        prompt = test["prompt"]
        expected = test["expected"]
        evaluator_name = test["evaluator"]

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

            # Get the correct extractor
            extractor = get_extractor(evaluator_name)

            # Extract the answer
            actual = extractor(rows)

            # Get the correct evaluator
            evaluator = get_evaluator(evaluator_name)

            # Compare expected vs actual
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