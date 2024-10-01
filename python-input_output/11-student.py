#!/usr/bin/python3

class Student:
    def __init__(self, first_name, last_name, age):
        """Inialise a new class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary with the specified attributes"""
        if attrs is None:
            return self.__dict__

        else:
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

    def reload_from_json(self, json):
        """"Replaces all the object's attributes."""
        value = 0
        for key, value in json.items():
            setattr(self, key, value)
