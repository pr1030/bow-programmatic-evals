import asyncio
import json
import httpx

from pathlib import Path
from evaluator import numeric_eval
from mcp.client.streamable_http import streamable_http_client
from mcp.client.session import ClientSession

# Replace with your API key
API_KEY = "bow_lTHUcS9mtBZ4S0Uzvfsix5HxxShPo5uyP-dDuzlMyrY"

# MCP endpoint
MCP_URL = "http://localhost:3000/api/mcp"


async def main():

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    async with httpx.AsyncClient(headers=headers) as http_client:

        async with streamable_http_client(
            MCP_URL,
            http_client=http_client,
        ) as (read_stream, write_stream, _):

            async with ClientSession(read_stream, write_stream) as session:

                print("Initializing...")
                await session.initialize()
                print("Connected!")

                print("\nAvailable tools:\n")

                tools = await session.list_tools()

                for tool in tools.tools:

                    if tool.name == "create_data":
                        print(tool)

                print("\nCreating report...\n")

                result = await session.call_tool(
                    "create_report",
                    {
                        "title": "Programmatic Evaluation Test"
                    }
                )

                # Convert the returned JSON string into a Python dictionary
                response = json.loads(result.content[0].text)

                print("\nParsed Response:\n")
                print(response)

                report_id = response["report_id"]

                # Load all evaluation test cases
                test_file = Path("test_cases/movie_tests.json")

                with open(test_file, "r") as f:
                    test_cases = json.load(f)

                print("\nReport ID:")
                print(report_id)

                print("\nGetting context...\n")

                context_result = await session.call_tool(
                    "get_context",
                    {
                        "report_id": report_id
                    }
                )

                context = json.loads(context_result.content[0].text)

                print("\nAvailable Data Sources:\n")

                for ds in context["data_sources"]:
                    print(f"Data Source: {ds['name']} ({ds['type']})")

                    for table in ds["tables"]:
                        print(f"   Table: {table['name']}")

                print("\n========== Running Evaluation ==========\n")

                passed_tests = 0

                for index, test in enumerate(test_cases, start=1):

                    print(f"\nTest {index}")

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

                    first_row = data_response["data_preview"]["rows"][0]

                    actual = list(first_row.values())[0]

                    passed = numeric_eval(expected, str(actual))

                    print("Prompt   :", prompt)
                    print("Expected :", expected)
                    print("Actual   :", actual)
                    print("Result   :", "PASS ✅" if passed else "FAIL ❌")

    if passed:
        passed_tests += 1


if __name__ == "__main__":
    asyncio.run(main())