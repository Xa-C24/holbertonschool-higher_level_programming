**Python - Classes and Objects**  

The first line **#!/usr/bin/python3** is mandatory for the file to be interpreted as an executable Python script.  

For check indentation  
 autopep8 --in-place *.py for all file.py  

For check your Output for exemple chmod +x 0-main.py  
python3 0-main.py  
./0-name_file.py  



**1. What is a Class?**  
A class is a model or structure used to create objects.  
It defines a set of attributes (variables) and methods (functions) that characterize the objects created from this class.  

            class Person:
    def __init__(self, name, age):
        self.name = name  # Attribut de l'instance
        self.age = age    # Attribut de l'instance  

In this example, Person is a class.  
The special __init__ method is the class constructor, used to initialize the object's attributes (here, name and age).  

**2. What is an Object?**    
An object is an instance of a class. It is a concrete entity created from the model defined by the class.   


        person1 = Person("Alice", 30)
print(person1.name)  # Affiche: Alice
print(person1.age)   # Affiche: 30  

Here, person1 is an object of class Person with attributes name and age  

**3. Class attributes**  
Attributes are variables that belong to a class. A distinction is made between : 
 - Instance attributes: specific to each object in the class.   
- Class attributes (not discussed in depth here): Shared by all instances of the class.  

**. Getters et Setters**  
Getters and setters are methods used to access and modify the attributes of a class.  
In Python, getters and setters can be defined using the @property decorator.  

**Conclusion**
Classes and objects are at the heart of Object-Oriented Programming.  
Classes define the structure and behavior of objects.  
Objects are the concrete instances of these classes, and class methods enable interaction with object attributes. Encapsulation, getters and setters help control access to and modification of object data.  

Key points to remember :  
  
Class: Model or plan for creating objects.  
Object: Instance of a class.  
Attribute: Variable defined in a class.  
Method: Function defined in a class.  
self : Référence à l'instance courante de la classe.  
Encapsulation: Hide the internal details of a class to protect its data.  


0. My first square  
1. Square with size  
2. Size validation  
3. Area of a square  
4. Access and update private attribute  
5. Printing a square  
6. Coordinates of a square  




