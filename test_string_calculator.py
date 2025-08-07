import pytest
from string_calculator import StringCalculator


def test_add_empty_string_returns_zero():
    """Test that add method returns 0 for empty string"""
    calculator = StringCalculator()
    assert calculator.add("") == 0


def test_add_single_number_returns_number():
    """Test that add method returns the number for single number input"""
    calculator = StringCalculator()
    assert calculator.add("1") == 1

def test_add_two_numbers_returns_sum():
    """Test that add method returns sum for two comma-separated numbers"""
    calculator = StringCalculator()
    assert calculator.add("1,5") == 6

def test_add_multiple_numbers_returns_sum():
    """Test that add method returns sum for multiple comma-separated numbers"""
    calculator = StringCalculator()
    assert calculator.add("1,2,3,4,5") == 15

def test_add_numbers_with_newlines():
    """Test that add method handles newlines between numbers"""
    calculator = StringCalculator()
    assert calculator.add("1\n2,3") == 6

def test_add_with_custom_delimiter():
    """Test that add method handles custom delimiters"""
    calculator = StringCalculator()
    assert calculator.add("//;\n1;2") == 3

def test_add_with_negative_number_throws_exception():
    """Test that add method throws exception for negative numbers"""
    calculator = StringCalculator()
    with pytest.raises(ValueError, match="negative numbers not allowed -1"):
        calculator.add("1,-1,2")
    
def test_add_with_multiple_negative_numbers_throws_exception():
    """Test that add method throws exception for multiple negative numbers"""
    calculator = StringCalculator()
    with pytest.raises(ValueError, match="negative numbers not allowed -1,-2"):
        calculator.add("1,-1,2,-2,3")
    
def test_add_with_multiple_negative_numbers_throws_exception():
    """Test that add method throws exception for multiple negative numbers"""
    calculator = StringCalculator()
    with pytest.raises(ValueError, match="negative numbers not allowed -1,-2"):
        calculator.add("1,-1,2,-2,3")