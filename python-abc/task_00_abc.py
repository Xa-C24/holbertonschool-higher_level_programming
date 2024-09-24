#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract Animal class that serves as a model for animals.
    """
    
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"
    