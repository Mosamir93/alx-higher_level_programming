#!/usr/bin/python3
"""Student class module."""


class Student:
    """class definition."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        try:
            for attr in attrs:
                if not isinstance(attr, str):
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
