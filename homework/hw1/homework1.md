# BFOR 206 Homework 1: Number Converter

## Task Description

Write a Python script to convert decimal numbers to binary or binary numbers to decimal.
The numbers should be integers greater than or equal to zero (no decimals). The script
should receive the type of conversion and the number to convert
as command line arguments.

There are two types of conversions:

1. Decimal to Binary (d2b)
2. Binary to Decimal (b2d)

The script should check the arguments for the following conditions:

1. The first argument should be either "d2b" or "b2d".
2. The second argument should be a valid number for the specified conversion type.
   - For "d2b", the second argument should be a non-negative integer.
   - For "b2d", the second argument should be a string of 0s and 1s.

If the arguments are valid, the script should perform the conversion and print the result. If the arguments are invalid, the script should print an appropriate error message and exit without performing any conversion.

## Basic Requirements

The script needs to be automatically tested. For this, it needs to be named
`binary_converter.py` and should be able to be run from the command line as follows:

```shell
python binary_converter.py <conversion_type> <number>
```

It needs three functions defined in the script:

1. `decimal_to_binary(n)`: This function takes a non-negative integer `n` and returns its binary representation as a string.
2. `binary_to_decimal(b)`: This function takes a string `b` representing a binary number and returns its decimal representation as an integer.
3. `check_arguments(args)`: This function takes a list of command line arguments and checks if they are valid according to the rules specified above. It should return a tuple containing the conversion type and the number if the arguments are valid, or print an error message and exit if they are not.

## Grading Criteria

1. **Argument Validation (4pts)**: The script should verify there are exactly two command line arguments (**1pt**); check the conversion type (d2b or b2d; **1pt**);
verify the number is a non-negative integer for d2b (**1pt**)
or a valid binary string for b2d (**1pt**).

2. **Testing (3pts)**: The script should be tested with various inputs to ensure it works correctly in both normal and edge cases. Each passing test (input validation, decimal to binary conversion, and binary to decimal conversion) will earn **1pt**.

3. **Code Quality (3pts)**: The code should be well-organized, with clear function definitions and appropriate use of comments to explain the logic.

4. **Code Management (2pts)**: The script should be properly committed to GitHub with clear commit messages. There should be at least five commits (**1pt**) over a 48+ hour period (**1pt**).


