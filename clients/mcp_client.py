import asyncio
import json
import time
import httpx

from pathlib import Path
from evaluator import numeric_eval
from mcp.client.streamable_http import streamable_http_client
from mcp.client.session import ClientSession

API_KEY = "bow_lTHUcS9mtBZ4S0Uzvfsix5HxxShPo5uyP-dDuzlMyrY"
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

                await session.initialize()

                # -----------------------------
                # Create report
                # -----------------------------

                result = await session.call_tool(
                    "create_report",
                    {
                        "title": "Programmatic Evaluation Test"
                    }
                )

                response = json.loads(result.content[0].text)
                report_id = response["report_id"]

                # -----------------------------
                # Load test cases
                # -----------------------------

                with open(Path("test_cases/movie_tests.json"), "r") as f:
                    test_cases = json.load(f)

                print("\n" + "=" * 60)
                print("              MCP Evaluation Framework")
                print("=" * 60)
                print(f"\nRunning {len(test_cases)} evaluation tests...\n")

                total_tests = len(test_cases)
                passed_tests = 0
                failed_tests = []

                start_time = time.perf_counter()

                # =====================================================
                # Run Tests
                # =====================================================

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

                        row = rows[0]

                        # Count query
                        if isinstance(expected, (int, float)):

                            value = None

                            for v in row.values():
                                if isinstance(v, (int, float)):
                                    value = v
                                    break

                            if value is None:
                                value = list(row.values())[0]

                            actual = value
                            passed = numeric_eval(expected, str(actual))

                        # String query
                        else:

                            actual = list(row.values())[0]
                            passed = str(actual).strip().lower() == str(expected).strip().lower()

                    status = "PASS ✅" if passed else "FAIL ❌"

                    print(f"{status}  Test {index:2}  {prompt}")

                    if passed:
                        passed_tests += 1
                    else:
                        failed_tests.append({
                            "test": index,
                            "prompt": prompt,
                            "expected": expected,
                            "actual": actual
                        })

                end_time = time.perf_counter()

                accuracy = (passed_tests / total_tests) * 100

                # =====================================================
                # Summary
                # =====================================================

                print("\n")
                print("=" * 60)
                print("Evaluation Summary")
                print("=" * 60)

                print(f"Total Tests   : {total_tests}")
                print(f"Passed        : {passed_tests}")
                print(f"Failed        : {total_tests - passed_tests}")
                print(f"Accuracy      : {accuracy:.2f}%")
                print(f"Execution Time: {end_time - start_time:.2f} sec")

                if failed_tests:

                    print("\nFailed Tests\n")

                    for failure in failed_tests:

                        print(f"Test {failure['test']}")
                        print(f"Prompt   : {failure['prompt']}")
                        print(f"Expected : {failure['expected']}")
                        print(f"Actual   : {failure['actual']}")
                        print()

                else:

                    print("\n🎉 All tests passed!")



if __name__ == "__main__":
    asyncio.run(main())