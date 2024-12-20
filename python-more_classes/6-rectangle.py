#!/usr/bin/python3
"""Module 6-rectangle: Defines an empty Rectangle class."""


class Rectangle:
    """
    Represents a rectangle.
    """
    number_of_instances = 0                 # compte le nombre d'instances de rectangles créées.

    def __init__(self, width=0, height=0):
        self.width = width                  #initialise longueur/hauteur valeur par default 0.
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width                 #valider les valeurs passées lors de la création d'un rectangle.

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:                                           #vérifie si la valeur est un entier ou bien superieur à 0.
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height             # Calcule et renvoie l'aire du rectangle en multipliant la largeur par la hauteur.

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0                                    #Calcule et renvoie le périmètre du rectangle
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        result = []
        for _ in range(self.__height):
            result.append("#" * self.__width)                       #crée une représentation visuelle du rectangle en utilisant le caractère #
        return "\n".join(result)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"        # fournie une représentation officielle de l'objet.

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1                          #suppression d'une instance de Rectangle.
