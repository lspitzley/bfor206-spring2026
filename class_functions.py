"""
Code to demonstrate how functions work and introduce
the concept of testing functions.

Functions are ordered alphabetically.
"""

# function to add numbers
def add_numbers(num1, num2):
    """
    Add two numbers together
    
    :param num1: first number
    :param num2: second number

    :returns: sum of the two numbers
    """

    sum = num1 + num2
    print(f'The sum of {num1} and {num2} = {sum}')

    # return to where the function was called
    return sum

# function to print an argument
def print_argument(arg1, arg2=None):
    """
    This function prints the argument that it receives
    
    :param arg1: Value to print
    :param arg2: (Optional) second value to print
    """

    print(f'The function received the arguments {arg1}, {arg2}')

# define a function with no arguments
def no_args_function():
    """
    This function prints stuff.
    """
    print('This is no_args_function()')

# call the function
no_args_function()

# call the print_argument function
print_argument('hello!')

# run with two arguments
print_argument('hello', 'again')

# add two numbers
my_sum = add_numbers(10, 20)
print(f'my_sum = {my_sum}')

# introduction to testing
assert add_numbers(1, 2) == 3


