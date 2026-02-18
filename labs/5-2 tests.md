# BFOR 206 Lab 5-2: Tests

## Task Description

Create and test a function using Pytest. You will need to create
two scripts (based on Homework 1). These are: the file with your program
(`binary_converter.py`) and a file with tests, in a folder called
`tests/` ('tests/test_binary_converter.py').

In the `binary_converter.py` file, create a function
named (`validate_conversion_type`) to
check the validity of the first argument (the type of conversion).
The valid input values are `d2b` and `b2d`. The function should
return `True` if the input is valid, otherwise `False`.

In the `tests/test_binary_converter.py` file, create a test function
named `test_validate_conversion_type` that tests the `validate_conversion_type`.

The test should have three cases:

1. A valid input of `d2b` that should return `True`.
2. A valid input of `b2d` that should return `True`.
3. An invalid input of `x2y` that should return `False`.

## Testing

```bash
# run this in the terminal
pytest tests/test_binary_converter.py
```

### Alternate Testing Method

You may also use the integrated testing features in VSCode.

## Submission instructions

**Scripts that output Python errors will not be accepted!**

Run your script to show that the tests pass.

When you are finished, show the instructor:

1. The successful test run.
2. You testing code.
