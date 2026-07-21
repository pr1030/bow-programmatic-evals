# Bag of Words Programmatic Evaluations

A lightweight evaluation framework for testing the accuracy and reliability of SQL generation using the Bag of Words analytics platform.

The project connects to a PostgreSQL database, executes evaluation cases, compares generated SQL with expected behavior, and measures the quality of responses. It also includes an exploration of the Bag of Words Model Context Protocol (MCP) server for future MCP-based automated evaluations.

---

## Features

- PostgreSQL database integration
- JSON-based evaluation test cases
- Automatic evaluator for SQL responses
- Configurable database connection
- GitHub Actions workflow for automated testing
- MCP server exploration using the official MCP Inspector
- Modular project structure for extending evaluation datasets

---

## Project Structure

```
bow-programmatic-evals/
│
├── clients/              # Client implementations
├── config/               # Configuration files
├── database/             # PostgreSQL connection utilities
├── evaluators/           # Evaluation logic
├── test_cases/           # JSON evaluation datasets
├── tests/                # Automated tests
├── utils/                # Helper functions
│
├── evaluator.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.11+
- PostgreSQL
- Git

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Database Setup

Update the database configuration inside:

```
config/config.py
```

or your `.env` file with your PostgreSQL credentials.

Example:

```
Host=localhost
Port=5432
Database=movies
Username=bow
Password=********
```

---

## Running the Evaluator

Execute:

```bash
python main.py
```

or run individual tests:

```bash
python test_evaluator.py
```

---

## Evaluation Dataset

The current evaluation dataset uses a custom **Movies PostgreSQL database** containing attributes such as:

- Movie Title
- Rating
- Genre
- Director
- Revenue
- Release Date
- Streaming Platform
- Region
- Awards
- Languages
- Content Rating

Evaluation cases are stored in:

```
test_cases/movies_eval_cases.json
```

---

## MCP Exploration

This project also explores the **Bag of Words Model Context Protocol (MCP)**.

### What was done

- Enabled MCP in the Bag of Words settings
- Generated an API key
- Connected using the official MCP Inspector
- Explored the available MCP tools
- Successfully invoked:
  - `create_report`
  - `get_context`

### MCP Workflow

The recommended workflow is:

```
create_report
      ↓
get_context
      ↓
inspect_data (optional)
      ↓
create_data
      ↓
create_artifact
```

This workflow helps reduce schema hallucinations by discovering tables and columns before generating SQL.

---

## Future Work

- Automate evaluation through MCP instead of direct PostgreSQL queries
- Expand the evaluation dataset
- Add additional evaluation metrics
- Compare multiple LLMs
- Generate automated evaluation reports

---

## License

This project is licensed under the MIT License.