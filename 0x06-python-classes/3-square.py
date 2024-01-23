#!/usr/bin/python3
"""Module that defines Square class."""


class Square:
    """Class definition."""
    def __init__(self, size=0):
        """Initializes instance.

        Args:
            size: size of a square


        Raises:
            TypeError: if size is not an int.
            ValueError: if size is less than zero.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates area of square.


        Returns:
            int: area of the square.
        """
        return self.__size ** 2
