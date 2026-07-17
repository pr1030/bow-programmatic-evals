import json

from database.postgres_client import PostgresClient


def load_test_cases(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def main():
    print("=" * 50)
    print("Bag of Words - Programmatic Evaluation Framework")
    print("=" * 50)

    test_cases = load_test_cases("test_cases/movie_eval_cases.json")

    client = PostgresClient()
    client.connect()

    for test_case in test_cases:
        print("\n" + "=" * 50)
        print(f"Test: {test_case['name']}")

        result = client.execute_query(
            test_case["ground_truth_sql"]
        )

        expected_value = result[0][0]

        print(f"Prompt: {test_case['prompt']}")
        print(f"Ground Truth: {expected_value}")

    client.close()


if __name__ == "__main__":
    main()