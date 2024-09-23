**inheritance**  

Inheritance is a fundamental concept of object-oriented programming (OOP).  
It allows you to create a new class based on an existing class.  
This favors code reuse and enables you to extend or modify the behavior of a class without rewriting the whole thing.  


**1. Definition of inheritance**  

- Parent class (superclass): This is the base class from which all other classes inherit.  
- Child class (subclass): This is the class that inherits from the parent class.  

In Python, inheritance is defined simply by enclosing the parent class in parentheses when defining the subclass.  

**2. The constructor and inheritance**  

During inheritance, the __init__ constructor of the parent class is not automatically called.  
You must use the super() function to call it explicitly in the subclass.  

**3. Multiple inheritance**  

Python supports multiple inheritance, i.e. a class can inherit from several classes.  
This can be useful, but also dangerous if the parent classes have identical methods.  

**4. Redefining methods (Overriding)**  

A subclass can redefine a method of the parent class to suit its needs.  
This is useful for modifying the behavior of certain methods without affecting the parent class.  


**5. super() function**    
super() is used to call a method or constructor of the parent class from a subclass.  
- In a constructor, super() calls the superclass constructor.  
- In a redefined method, super() calls the parent version of this method.  

**6. Polymorphism**  
Polymorphism allows methods to be used generically for objects of different subclasses.  

**7. Inheritance check**  

- isinstance(obj, Class): Checks whether an object is an instance of a class or subclass.  
- issubclass(SubClass, Class): Checks whether a class is a subclass of another class.  

**8. Composition vs. Inheritance**  

Sometimes, instead of using inheritance, it may be more useful to compose a class by including objects from other classes as attributes.    
This is a form of code reuse without creating an "is-one" relationship (as in inheritance), but rather an "a-one" one.  

**Summary:**   
- Inheritance: Allows a class to inherit attributes and methods from another class.  
- super() : Used to call methods or constructors of the parent class.  
- Multiple inheritance: A class can inherit from several classes.  
- Polymorphism: Ability to use methods on different objects in a generic way.  
- Composition: Alternative to inheritance, where a class includes instances of other classes.  




