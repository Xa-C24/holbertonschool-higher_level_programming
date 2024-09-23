#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Classe Rectangle qui hérite de BaseGeometry."""

    def __init__(self, width, height):
        """Initialise le rectangle avec une largeur et une hauteur."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Retourne l'aire du rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Retourne une représentation lisible de l'objet Rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
