#!/usr/bin/python3
"""Base class test module."""
from models.base import Base
from models.rectangle import Rectangle
import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO

class TestRectangle(TestCase):
    """Test class for rectangle class."""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_new_no_x_y(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 1)

    def test_new_with_x_y(self):
        rect = Rectangle(5, 10, 3, 4, 8)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 8)

    def test_is_the_same(self):
        rec1 = Rectangle(5, 10)
        rec2 = Rectangle(5, 10)
        self.assertEqual(False, rec1.id == rec2.id)
        self.assertEqual(False, rec1 is rec2)

    def test_few_attributes(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5)

    def test_inheritance(self):
        rect = Rectangle(5, 10)
        self.assertEqual(True, isinstance(rect, Base))

    def test_no_attributes(self):
        with self.assertRaises(TypeError):
            rect = Rectangle()

    def test_access_width(self):
        rect = Rectangle(5, 10)
        with self.assertRaises(AttributeError):
            rect.__width

    def test_access_height(self):
        rect = Rectangle(5, 10)
        with self.assertRaises(AttributeError):
            rect.__height

    def test_access_x(self):
        rect = Rectangle(5, 10)
        with self.assertRaises(AttributeError):
            rect.__x

    def test_access_y(self):
        rect = Rectangle(5, 10)
        with self.assertRaises(AttributeError):
            rect.__y

    def test_valid_width(self):
        with self.assertRaises(TypeError):
            rect = Rectangle('5', 10)

    def test_valid_height(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, '10')

    def test_valid_x(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10, '3', 4)

    def test_valid_y(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10, 3, '4')

    def test_valid_value_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 10, 3, 4)

    def test_valid_value_height(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 0, 3, 4)

    def test_valid_value_x(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10, -1, 4)

    def test_valid_value_y(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10, 3, -1)

    def test_area(self):
        rect1 = Rectangle(5, 10)
        rect2 = Rectangle(3, 4)
        rect3 = Rectangle(4, 8)
        self.assertEqual(rect1.area(), 50)
        self.assertEqual(rect2.area(), 12)
        self.assertEqual(rect3.area(), 32)

    def test_display(self):
        rect = Rectangle(1, 2)
        result = "#\n#\n"
        with patch("sys.stdout", new=StringIO()) as out:
            rect.display()
            self.assertEqual(out.getvalue(), result)

    def test___str__(self):
        rect = Rectangle(1, 2)
        result = "[Rectangle] (1) 0/0 - 1/2\n"
        with patch("sys.stdout", new=StringIO()) as out:
            print(rect)
            self.assertEqual(out.getvalue(), result)
