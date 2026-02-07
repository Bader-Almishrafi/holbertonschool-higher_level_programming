#!/usr/bin/python3
"""
Defines a Student class with JSON serialization and reloading.
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of the instance"""
        if isinstance(attrs, list):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace attributes of the instance from a dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
