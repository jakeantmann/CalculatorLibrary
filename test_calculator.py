"""Unit tests for the calculator library."""

import calculator


class TestCalculator:
    """Test the calculator."""

    def test_addition(self):
        """Test addition."""
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        """Test subtraction."""
        assert 2 == calculator.subtract(4, 2)
