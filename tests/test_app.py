"""
Unit tests for the main application classes.
"""

import datetime
import pytest
from myapp.app import Calculator, GreetingService, ListUtils


class TestCalculator:
    """Test cases for Calculator class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_add(self):
        """Test addition operation."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
        assert self.calc.add(2.5, 3.5) == 6.0

    def test_subtract(self):
        """Test subtraction operation."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(1, 1) == 0
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(7.5, 2.5) == 5.0

    def test_multiply(self):
        """Test multiplication operation."""
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(-1, 5) == -5
        assert self.calc.multiply(0, 10) == 0
        assert self.calc.multiply(2.5, 4) == 10.0

    def test_divide(self):
        """Test division operation."""
        assert self.calc.divide(6, 2) == 3
        assert self.calc.divide(7, 2) == 3.5
        assert self.calc.divide(-10, 2) == -5

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)


class TestGreetingService:
    """Test cases for GreetingService class."""

    def test_default_greeting(self):
        """Test default greeting."""
        service = GreetingService()
        assert service.get_greeting() == "Hello World from Jenkins Pipeline!"

    def test_custom_greeting(self):
        """Test custom name greeting."""
        service = GreetingService("Jenkins")
        assert service.get_greeting() == "Hello Jenkins from Jenkins Pipeline!"

    def test_get_current_time_format(self):
        """Test current time format."""
        service = GreetingService()
        time_str = service.get_current_time()
        # Verify format YYYY-MM-DD HH:MM:SS
        datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

    def test_is_weekend(self):
        """Test weekend detection."""
        service = GreetingService()

        # Test with known dates
        monday = datetime.date(2023, 1, 2)  # Monday
        saturday = datetime.date(2023, 1, 7)  # Saturday
        sunday = datetime.date(2023, 1, 8)  # Sunday

        assert not service.is_weekend(monday)
        assert service.is_weekend(saturday)
        assert service.is_weekend(sunday)


class TestListUtils:
    """Test cases for ListUtils class."""

    def test_filter_even_numbers(self):
        """Test filtering even numbers."""
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [2, 4, 6, 8, 10]
        assert ListUtils.filter_even_numbers(numbers) == expected

        # Test empty list
        assert ListUtils.filter_even_numbers([]) == []

        # Test all odd numbers
        assert ListUtils.filter_even_numbers([1, 3, 5]) == []

        # Test all even numbers
        assert ListUtils.filter_even_numbers([2, 4, 6]) == [2, 4, 6]

    def test_find_max(self):
        """Test finding maximum number."""
        assert ListUtils.find_max([1, 5, 3, 9, 2]) == 9
        assert ListUtils.find_max([1]) == 1
        assert ListUtils.find_max([-5, -1, -10]) == -1
        assert ListUtils.find_max([1.5, 2.7, 1.2]) == 2.7

    def test_find_max_empty_list(self):
        """Test finding max of empty list raises ValueError."""
        with pytest.raises(ValueError, match="List cannot be empty"):
            ListUtils.find_max([])

    def test_calculate_average(self):
        """Test calculating average."""
        assert ListUtils.calculate_average([2, 4, 6]) == 4.0
        assert ListUtils.calculate_average([1]) == 1.0
        assert ListUtils.calculate_average([1, 2, 3, 4, 5]) == 3.0
        assert ListUtils.calculate_average([1.5, 2.5]) == 2.0

    def test_calculate_average_empty_list(self):
        """Test calculating average of empty list raises ValueError."""
        with pytest.raises(ValueError, match="List cannot be empty"):
            ListUtils.calculate_average([])
