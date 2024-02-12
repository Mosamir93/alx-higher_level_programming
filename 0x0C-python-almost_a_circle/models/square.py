#!/usr/bin/python3
"""Square class module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class definition."""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Sets the __str__ of square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Size getter."""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of an object."""
        if args and len(args) > 0:
            attrs = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation of an object."""
        return {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y,
                }
