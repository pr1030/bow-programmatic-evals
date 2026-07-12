def numeric_eval(expected, actual):
    """
    Compare the expected numeric value with the actual numeric value.
    Returns PASS if they match, otherwise FAIL.
    """
    if expected == actual:
        return "PASS"
    else:
        return "FAIL"


def main():
    print("=" * 50)
    print("Bag of Words - Programmatic Evaluation")
    print("=" * 50)

    # User's question
    prompt = "What is the average movie rating?"

    # Simulated Bag of Words response
    actual_rating = 8.74

    # Correct answer
    expected_rating = 8.74

    # Run the evaluation
    result = numeric_eval(expected_rating, actual_rating)

    print(f"Prompt: {prompt}")
    print(f"Expected Rating: {expected_rating}")
    print(f"Actual Rating: {actual_rating}")
    print(f"Evaluation Result: {result}")


if __name__ == "__main__":
    main()