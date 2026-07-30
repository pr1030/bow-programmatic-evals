import json
from pathlib import Path


async def arrange(session):
    """
    Creates a report and loads all test cases.
    """

    result = await session.call_tool(
        "create_report",
        {
            "title": "Programmatic Evaluation Test"
        }
    )

    response = json.loads(result.content[0].text)

    report_id = response["report_id"]

    with open(Path("test_cases/movie_tests.json"), "r") as f:
        test_cases = json.load(f)

    return report_id, test_cases