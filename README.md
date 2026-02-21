# LAB1 - MLOps (IE-7374)

This lab focuses on 5 modules: creating a virtual environment, creating a GitHub repository, creating Python files, creating test files using pytest and unittest, and implementing GitHub Actions.

## Modification
Instead of a basic calculator, this lab implements **statistics functions** (mean, median, standard deviation) to demonstrate MLOps concepts in a data analytics context.

## Project Structure
```
mlops-github-lab/
├── src/
│   ├── __init__.py
│   └── statistics_functions.py
├── test/
│   ├── __init__.py
│   ├── test_pytest.py
│   └── test_unittest.py
├── .github/
│   └── workflows/
│       ├── github_lab1_pytest_action.yml
│       └── github_lab2_unittest_action.yml
├── requirements.txt
└── README.md
```

## Functions
- `fun1(data)` - Calculates the **mean** of a list of numbers
- `fun2(data)` - Calculates the **median** of a list of numbers
- `fun3(data)` - Calculates the **standard deviation** of a list of numbers
- `fun4(data)` - Returns a summary dictionary with mean, median, and standard deviation

## Setup

### Create and activate virtual environment
```bash
python -m venv lab_01
lab_01\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

## Running Tests

### Pytest
```bash
pytest test/test_pytest.py -v
```

### Unittest
```bash
python -m unittest test.test_unittest -v
```

## GitHub Actions
Two workflows are configured to run automatically on every push to `main`:
- `github_lab1_pytest_action.yml` - Runs pytest tests
- `github_lab2_unittest_action.yml` - Runs unittest tests