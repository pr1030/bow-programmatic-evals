def print_summary(results, execution_time):

    print("\n")
    print("=" * 60)
    print("              MCP Evaluation Framework")
    print("=" * 60)

    print(f"\nRunning {len(results)} evaluation tests...\n")

    passed = 0

    for result in results:

        status = "PASS ✅" if result["passed"] else "FAIL ❌"

        print(
            f"{status:8} Test {result['test']:>2}  {result['prompt']}"
        )

        if result["passed"]:
            passed += 1

    failed = len(results) - passed

    accuracy = passed / len(results) * 100

    print("\n")
    print("=" * 60)
    print("Evaluation Summary")
    print("=" * 60)

    print(f"Total Tests   : {len(results)}")
    print(f"Passed        : {passed}")
    print(f"Failed        : {failed}")
    print(f"Accuracy      : {accuracy:.2f}%")
    print(f"Execution Time: {execution_time:.2f} sec")

    if failed:

        print("\nFailed Tests\n")

        for result in results:

            if not result["passed"]:

                print(f"Test {result['test']}")
                print(f"Prompt   : {result['prompt']}")
                print(f"Expected : {result['expected']}")
                print(f"Actual   : {result['actual']}")
                print()