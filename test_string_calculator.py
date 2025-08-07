import pytest
from string_calculator import StringCalculator


def test_add_empty_string_returns_zero():
    """Test that add method returns 0 for empty string"""
    calculator = StringCalculator()
    assert calculator.add("") == 0