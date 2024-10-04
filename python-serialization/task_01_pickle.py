#!/usr/bin/python3
import pickle
"""Import module pickle"""


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student


    def display(self):
        """Displays the object's attributes in a specific format."""

        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Erreur lors de la sérialisation : {e}")

    @classmethod
    def deserialize(cls, filename):
        """Deserializes and returns an instance of CustomObject"""

        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Erreur lors de la désérialisation : {e}")
            return None
        