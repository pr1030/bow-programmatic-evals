import json
from evaluator import numeric_eval


def load_test_cases(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def main():

    print("=" * 60)
    print("Bag of Words - Programmatic Evaluation Framework")
    print("=" * 60)

    test_cases = load_test_cases("test_cases/movie_eval_cases.json")

    passed = 0
    failed = 0

    for index, case in enumerate(test_cases, start=1):

        print("\n----------------------------------------")
        print(f"Test Case {index}: {case['name']}")
        print("----------------------------------------")

        result = numeric_eval(case["expected"], case["response"])

        print(f"Prompt   : {case['prompt']}")
        print(f"Response : {case['response']}")

        if result:
            print("Result   : PASS")
            passed += 1
        else:
            print("Result   : FAIL")
            failed += 1

    print("\n" + "=" * 60)
    print("Evaluation Summary")
    print("=" * 60)
    print(f"Total Tests : {len(test_cases)}")
    print(f"Passed      : {passed}")
    print(f"Failed      : {failed}")


if __name__ == "__main__":
    main()