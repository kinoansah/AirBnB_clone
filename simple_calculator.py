#!/usr/bin/python3

"""
This is a sample module for demonstrating pycodestyle compliance.

Module Description:
This module contains functions to perform basic arithmetic operations.

Functions:
- add(x, y): Returns the sum of two numbers.
- subtract(x, y): Returns the difference between two numbers.
- multiply(x, y): Returns the product of two numbers.
- divide(x, y): Returns the result of dividing one number by another.
"""


class Calculator:
    """
    Calculator Class

    Class Description:
    This class provides methods for performing arithmetic operations.

    Methods:
    - add(x, y): Returns the sum of two numbers.
    - subtract(x, y): Returns the difference between two numbers.
    - multiply(x, y): Returns the product of two numbers.
    - divide(x, y): Returns the result of dividing one number by another.
    """

    def add(self, x, y):
        """
        Add two numbers.

        Args:
            x (int): The first number.
            y (int): The second number.

        Returns:
            int: The sum of x and y.
        """
        return x + y

    def subtract(self, x, y):
        """
        Subtract two numbers.

        Args:
            x (int): The first number.
            y (int): The second number.

        Returns:
            int: The difference between x and y.
        """
        return x - y

    def multiply(self, x, y):
        """
        Multiply two numbers.

        Args:
            x (int): The first number.
            y (int): The second number.

        Returns:
            int: The product of x and y.
        """
        return x * y

    def divide(self, x, y):
        """
        Divide two numbers.

        Args:
            x (int): The dividend.
            y (int): The divisor.

        Returns:
            float: The result of dividing x by y.
        """
        if y != 0:
            return x / y
        else:
            raise ValueError("Cannot divide by zero")


if __name__ == "__main__":
    calculator = Calculator()
    result = calculator.multiply(5, 3)
    print("Multiplication result:", result)

if __name__ == "__main__":
    calculator = Calculator()
    result = calculator.add(5, 3)
    print("Addition result:", result)
