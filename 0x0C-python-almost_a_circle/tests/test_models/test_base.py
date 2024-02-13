#!/usr/bin/python3
"""Base class test module."""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
from unittest import TestCase
from unittest.mock import patch
import os
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

    def test_id2(self):
        base = Base('3')
        self.assertEqual(base.id, '3')

    def test_args(self):
        with self.assertRaises(TypeError):
            base = Base(1, 2)
    
    def test_save_to_file_None_rec(self):
        Rectangle.save_to_file(None)
        result = "[]\n"
        file = "Rectangle.json"
        with open(file, mode='r') as fl:
            with patch('sys.stdout', new=StringIO()) as out:
                print(fl.read())
                self.assertEqual(out.getvalue(), result)
            try:
                os.remove(file)
            except:
                pass

    def test_save_to_file_empty_rec(self):
        Rectangle.save_to_file([])
        with open('Rectangle.json') as fl:
            self.assertEqual(fl.read(), '[]')

    def test_save_to_file_None_sq(self):
        Square.save_to_file(None)
        result = "[]\n"
        file = "Square.json"
        with open(file, mode='r') as fl:
            with patch('sys.stdout', new=StringIO()) as out:
                print(fl.read())
                self.assertEqual(out.getvalue(), result)
            try:
                os.remove(file)
            except:
                pass

    def test_save_to_file_empty_sq(self):
        Square.save_to_file([])
        with open('Square.json') as fl:
            self.assertEqual(fl.read(), '[]')
 
    if __name__ == "__main__":
        unittest.main()
