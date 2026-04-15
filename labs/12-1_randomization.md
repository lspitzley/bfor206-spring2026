# BFOR 206 Lab 12-1: Tests for Randomization

## Task Description

Create a test script file called `tests/test_exam.py`.

This file should import the `exam.py` module to test functions in the
`Exam` class.

It should have the following method:

- `test_randomize_exam()`: a method that tests randomizes the order of the questions in the exam.

Use the example data created in Lab 9-2 to test the `randomize_exam()` method. You can use the `assert` statement to check that the order of the questions is different after randomization.

Set the seed such that each version of the exam has a different order of questions, and 
that the order is different from the original order. You can use the `random.seed()` function to set the seed for reproducibility.

## Testing

```bash
# run this in the terminal
python -m -s pytest
```

The `-s` flag will show any print statements, which is can be helpful for debugging. If successful, the test should pass without any errors.

## Submission instructions

**Scripts that output Python errors will not be accepted!**

Run your script to show that the output matches the definitions above.

When you are finished, show the instructor:

1. The successful test run.
2. Your code.
