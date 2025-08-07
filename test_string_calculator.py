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