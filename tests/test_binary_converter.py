"""
Use pytest to test the binary converter functions.

Copy this code to your HW1 repository and run pytest to ensure all tests pass.
"""
import pytest
import binary_converter as bc

def test_decimal_to_binary():
    """
    Test the decimal_to_binary function with various inputs.        
    """
    assert bc.decimal_to_binary(0) == '0'
    assert bc.decimal_to_binary(1) == '1'
    assert bc.decimal_to_binary(2) == '10'
    assert bc.decimal_to_binary(5) == '101'
    assert bc.decimal_to_binary(10) == '1010'
    assert bc.decimal_to_binary(255) == '11111111'

def test_binary_to_decimal():
    """
    Test the binary_to_decimal function with various inputs.        
    """
    assert bc.binary_to_decimal('0') == 0
    assert bc.binary_to_decimal('1') == 1
    assert bc.binary_to_decimal('10') == 2
    assert bc.binary_to_decimal('101') == 5
    assert bc.binary_to_decimal('1010') == 10
    assert bc.binary_to_decimal('11111111') == 255

@pytest.mark.parametrize("conversion_type", ["d2b", "b2d"])
def test_check_conversion_type_valid(conversion_type):
    """
    Test the check_conversion_type function with valid inputs.
    """
    assert bc.check_conversion_type(conversion_type) is True


@pytest.mark.parametrize("conversion_type", ["", "d2d", "b2b", "invalid", "D2B"])
def test_check_conversion_type_invalid(conversion_type):
    """
    Test the check_conversion_type function with invalid inputs.
    """
    assert bc.check_conversion_type(conversion_type) is False


@pytest.mark.parametrize("number", ["0", "1", "10", "255", "1000"])
def test_check_decimal_number_valid(number):
    """
    Test the check_decimal_number function with valid inputs.
    """
    assert bc.check_decimal_number(number) is True


@pytest.mark.parametrize("number", ["-1", "3.5", "abc", "", "1 0"])
def test_check_decimal_number_invalid(number):
    """
    Test the check_decimal_number function with invalid inputs.
    """
    assert bc.check_decimal_number(number) is False


@pytest.mark.parametrize("bits", ["0", "1", "10", "1010", "11111111"])
def test_check_binary_number_valid(bits):
    """
    Test the check_binary_number function with valid inputs.
    """
    assert bc.check_binary_number(bits) is True


@pytest.mark.parametrize("bits", ["", "2", "102", "10a", "-101"])
def test_check_binary_number_invalid(bits):
    """
    Test the check_binary_number function with invalid inputs.
    """
    assert bc.check_binary_number(bits) is False

        
    
