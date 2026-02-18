"""
A few example functions to demonstrate 
unit tests.
"""

def string_checker(input_string:str, substring:str) -> bool:
    """
    Check for a substring in an input string.
    
    :param input_string: longer string to check
    :type input_string: str
    :param substring: substring to check
    :return: True of False if the substring is found.
    :rtype: bool
    """

    if substring in input_string:
        return True
    else:
        return False

def validate_conversion_type(conversion_type:str) -> bool:
    """
    Docstring for validate_conversion_type
    
    :param conversion_type: Description
    :type conversion_type: str
    :return: Description
    :rtype: bool
    """

    pass