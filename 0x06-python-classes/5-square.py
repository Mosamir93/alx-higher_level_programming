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

    @property
    def size(self):
        """
        Getter method to tetrieve size.

        Returns:
            int: size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size attribute.

        Args:
            value (int): The size to be set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Prints the square with the character #.

        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
