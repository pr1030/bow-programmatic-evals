from evaluator import numeric_eval


def main():

    expected = 8.74

    response = "The average movie rating is 8.74."

    if numeric_eval(expected, response):
        print("PASS")
    else:
        print("FAIL")


if __name__ == "__main__":
    main()