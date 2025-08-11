# String Calculator TDD Kata

A Python implementation of the String Calculator kata using Test-Driven Development (TDD) principles. This project demonstrates clean code practices and comprehensive test coverage.

## Project Description

The String Calculator kata is a classic programming exercise that involves creating a method to add numbers from a string input. The implementation follows TDD methodology, where tests are written first to drive the development of the functionality.

## Features

The `StringCalculator` class implements the following features:

1. **Empty String Handling**: Returns 0 for empty strings
2. **Single Number**: Returns the number itself
3. **Multiple Numbers**: Adds comma-separated numbers
4. **Newline Support**: Handles newlines as delimiters
5. **Custom Delimiters**: Supports custom delimiters using `//` syntax
6. **Negative Number Validation**: Throws exceptions for negative numbers

## Usage Examples

```python
from string_calculator import StringCalculator

calculator = StringCalculator()

# Empty string
result = calculator.add("")  # Returns 0

# Single number
result = calculator.add("1")  # Returns 1

# Multiple numbers
result = calculator.add("1,2,3")  # Returns 6

# Numbers with newlines
result = calculator.add("1\n2,3")  # Returns 6

# Custom delimiter
result = calculator.add("//;\n1;2")  # Returns 3

# Negative numbers (throws exception)
try:
    result = calculator.add("1,-1,2")
except ValueError as e:
    print(e)  # "negative numbers not allowed -1"
```

## Project Structure

```
string_calculator_tdd_kata/
├── README.md                 # This file
├── pyproject.toml           # Project configuration and dependencies
├── uv.lock                  # Lock file for dependency versions
├── string_calculator.py     # Main implementation
└── test_string_calculator.py # Test suite
```

## Setup and Installation

This project uses Python 3.12+ and `uv` for dependency management.

### Prerequisites

- Python 3.12 or higher
- `uv` package manager

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd string_calculator_tdd_kata
   ```

2. Install dependencies:

   ```bash
   uv sync
   ```

## Running Tests

The project uses `pytest` for testing. To run the test suite:

```bash
uv run pytest
```

To run tests with verbose output:

```bash
uv run pytest -v
```

To run tests with coverage:

```bash
uv run pytest --cov=string_calculator
```

## Test Coverage

The test suite covers all implemented features:

- ✅ Empty string handling
- ✅ Single number input
- ✅ Multiple comma-separated numbers
- ✅ Newline delimiter support
- ✅ Custom delimiter support
- ✅ Negative number validation
- ✅ Multiple negative number handling

## Development

This project follows TDD principles:

1. Write a failing test
2. Write the minimum code to make the test pass
3. Refactor the code while keeping tests green

### Adding New Features

When adding new features:

1. Add a new test case in `test_string_calculator.py`
2. Run tests to ensure the new test fails
3. Implement the feature in `string_calculator.py`
4. Run tests to ensure all tests pass
5. Refactor if necessary

## Dependencies

- **pytest**: Testing framework
- **Python 3.12+**: Runtime requirement

## License

This project is open source and available under the MIT License.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes following TDD principles
4. Ensure all tests pass
5. Submit a pull request

## References

- [String Calculator Kata](http://osherove.com/tdd-kata-1/)
- [Test-Driven Development](https://en.wikipedia.org/wiki/Test-driven_development)
