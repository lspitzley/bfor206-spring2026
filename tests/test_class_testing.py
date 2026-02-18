"""
Functions to demonstrate testing.

1. run as python -m tests.test_class_testing
2. install pytest: pip install pytest
3. run tests: python -m pytest
"""

# imports
import class_testing


def test_string_checker():
    """
    Tests for the substring checker
    """

    assert class_testing.string_checker('and', 'e') is False
    assert class_testing.string_checker('and', 'a') is True


