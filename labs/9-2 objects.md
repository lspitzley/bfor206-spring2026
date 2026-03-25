# BFOR 206 Lab 5-2: Tests

## Task Description

Create a class `Exams` in a file called `exams.py` that has the following attributes:

- `exam_number`: an integer representing the exam number.
- `exam_version`: an integer representing the version of the exam.
- `questions`: a list of strings representing the questions in the exam.

It should also have the following methods:

- `randomize_exam()`: a method that randomizes the order of the questions in the exam.
- `display_exam()`: a method that prints the exam number, version, and questions in a readable format.

After defining the class, add a `if __name__ == "__main__":` block that creates two
instances of the `Exams` class (version 1 and version 2), populates them with three example
questions, and demonstrates the functionality of the methods.

The questions can be simple strings like "What is 2 + 2?" or "What is the capital of France?".
For now, they do not need answers.

## Testing

```bash
# run this in the terminal
python exams.py
```

If successful, the script should print two exams with the exam number, exam version,
and the questions in a different order for each exam.

## Submission instructions

**Scripts that output Python errors will not be accepted!**

Run your script to show that the output matches the definitions above.

When you are finished, show the instructor:

1. The successful test run.
2. Your code.
