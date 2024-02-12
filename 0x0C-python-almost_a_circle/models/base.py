#!/usr/bin/python3
"""Class base module."""
import json
import csv
import turtle


class Base:
    """Class definition."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor."""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list into a json string."""
        if list_dictionaries and len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves json string into file."""
        if list_objs is None:
            list_objs = []
        file = cls.__name__ + ".json"
        str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(file, "w") as fl:
            fl.write(str)

    @staticmethod
    def from_json_string(json_string):
        """Reads a json string from a file."""
        if json_string and len(json_string) > 0:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance and sets it's attributes."""
        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a json file."""
        file = cls.__name__ + ".json"
        try:
            with open(file, mode="r", encoding="utf-8") as fl:
                str = fl.read()
                list = cls.from_json_string(str)
                return [cls.create(**dict) for dict in list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes into csv."""
        file = cls.__name__ + ".csv"
        with open(file, mode="w", newline="", encoding="utf-8") as fl:
            writer = csv.writer(fl)
            if list_objs:
                for object in list_objs:
                    dict = object.to_dictionary()
                    if cls.__name__ == "Square":
                        writer.writerow([dict['id'],
                                        dict['size'],
                                        dict['x'],
                                        dict['y']])
                    elif cls.__name__ == "Rectangle":
                        writer.writerow([dict['id'],
                                        dict['width'],
                                        dict['height'],
                                        dict['x'],
                                        dict['y']])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes from csv."""
        file = cls.__name__ + ".csv"
        try:
            with open(file, mode="r", encoding="utf-8") as fl:
                reader = csv.reader(fl)
                attrs = []
                for line in reader:
                    if cls.__name__ == "Square":
                        dict = {'id': int(line[0]),
                                'size': int(line[1]),
                                'x': int(line[2]),
                                'y': int(line[3])}
                    elif cls.__name__ == "Rectangle":
                        dict = {'id': int(line[0]),
                                'width': int(line[1]),
                                'height': int(line[2]),
                                'x': int(line[3]),
                                'y': int(line[4])}
                    attr = cls.create(**dict)
                    attrs.append(attr)
            return attrs
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws rectangles and squares using turtule module."""
        screen = turtle.Screen()
        pen = turtle.Turtle()
        pen.speed(2)
        pen.color("blue")
        pen.shape("turtle")

        for rect in list_rectangles:
            pen.up()
            pen.goto(rect.x, rect.y)
            pen.down()

            for i in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)

            pen.up()
            pen.goto(0, 0)
            pen.down()

        pen.color("green")
        pen.shape("square")

        for square in list_squares:
            pen.up()
            pen.goto(square.x, square.y)
            pen.down()

            for i in range(4):
                pen.forward(square.size)
                pen.left(90)

            pen.up()
            pen.goto(0, 0)
            pen.down()
        screen.mainloop()
