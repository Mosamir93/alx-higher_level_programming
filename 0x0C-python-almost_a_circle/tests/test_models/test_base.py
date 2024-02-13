#!/usr/bin/python3
"""Base class test module."""
from models.base import Base
import unittest
from unittest import TestCase
from io import StringIO
import json


class testbase(TestCase):
    """Test class definition."""
    def setUp(self):
        """Setup function before each test."""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Id test."""
        base1 = Base()
        base2 = Base(9)
        base3 = Base(100)
        base4 = Base(1000)
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 9)
        self.assertEqual(base3.id, 100)
        self.assertEqual(base4.id, 1000)

    def test_nb_object(self):
        """Nb_objects test."""
        base = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)

    def test_nb_object_private(self):
        """Tests nb_object access."""
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    def test_to_json_string_input(self):
        data = [{'key1': 'value1'}, {'key2': 'value2'}]
        expected = json.dumps(data)
        res = Base.to_json_string(data)
        self.assertEqual(res, expected)

    def test_to_json_string_empty(self):
        data = []
        expected = json.dumps(data)
        res = Base.to_json_string(data)
        self.assertEqual(res, expected)

    def test_to_json_string_None(self):
        data = None
        expected = "[]"
        res = Base.to_json_string(data)
        self.assertEqual(res, expected)

    if __name__ == "__main__":
        unittest.main()
