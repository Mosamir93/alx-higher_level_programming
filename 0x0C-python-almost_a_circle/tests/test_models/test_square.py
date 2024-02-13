#!/usr/bin/python3
"""Base class test module."""
from models.base import Base
from models.square import Square
import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO

class Testsquare(TestCase):
    """Test class for Square class."""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_new_no_x_y(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertEqual(square.id, 1)

    def test_new_with_x_y(self):
        square = Square(5, 3, 4, 8)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)
        self.assertEqual(square.id, 8)

    def test_is_the_same(self):
        rec1 = Square(5, 10)
        rec2 = Square(5, 10)
        self.assertEqual(False, rec1.id == rec2.id)
        self.assertEqual(False, rec1 is rec2)

    def test_few_attributes(self):
        with self.assertRaises(TypeError):
            square = Square()

    def test_inheritance(self):
        square = Square(5)
        self.assertEqual(True, isinstance(square, Base))

    def test_no_attributes(self):
        with self.assertRaises(TypeError):
            square = Square()

    def test_access_size(self):
        square = Square(5)
        with self.assertRaises(AttributeError):
            square.__size

    def test_access_x(self):
        square = Square(5, 10)
        with self.assertRaises(AttributeError):
            square.__x

    def test_access_y(self):
        square = Square(5, 10)
        with self.assertRaises(AttributeError):
            square.__y

    def test_valid_size(self):
        with self.assertRaises(TypeError):
            square = Square('5')

    def test_valid_x(self):
        with self.assertRaises(TypeError):
            square = Square(5, '3', 4)

    def test_valid_y(self):
        with self.assertRaises(TypeError):
            square = Square(5, 3, '4')

    def test_valid_value_size(self):
        with self.assertRaises(ValueError):
            square = Square(0, 3, 4)

    def test_valid_value_x(self):
        with self.assertRaises(ValueError):
            square = Square(5, -1, 4)

    def test_valid_value_y(self):
        with self.assertRaises(ValueError):
            square = Square(5, 3, -1)

    def test_area(self):
        square1 = Square(5)
        square2 = Square(3)
        square3 = Square(4)
        self.assertEqual(square1.area(), 25)
        self.assertEqual(square2.area(), 9)
        self.assertEqual(square3.area(), 16)

    def test_display(self):
        square = Square(1)
        result = "#\n"
        with patch("sys.stdout", new=StringIO()) as out:
            square.display()
            self.assertEqual(out.getvalue(), result)

    def test___str__(self):
        square = Square(1)
        result = "[Square] (1) 0/0 - 1\n"
        with patch("sys.stdout", new=StringIO()) as out:
            print(square)
            self.assertEqual(out.getvalue(), result)
