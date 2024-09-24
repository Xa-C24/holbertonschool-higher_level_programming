**Python - Abstract Classes and Interfaces**  


**In Python,** abstract classes and interfaces are essential concepts for object-oriented programming (OOP).  
They allow you to define behaviour common to several classes without implementing any concrete logic in the base class.  
Let's explore these concepts in detail.  

**1. Abstract classes in Python**  

An abstract class is a class that cannot be instantiated directly. It serves as a model for other classes.  
In Python, abstract classes are defined using the abc (Abstract Base Classes) module.  


Main features:  

- An abstract class can contain normal methods (with implementation) and abstract methods (without implementation).  
- If a class contains one or more abstract methods, it must be declared abstract.  
- The sub-classes of an abstract class must implement all the abstract methods in order to be instantiated.  

Key points:   

- An abstract class is defined by inheriting from ABC.   
- Abstract methods are defined using the @abstractmethod decorator.   
- Subclasses must implement all abstract methods in order to be usable in practice.  

**2. Interfaces en Python**  

In Python, there is no concept of a "pure" interface as in some other languages (e.g. Java).  
However, interfaces can be simulated through abstract classes. An interface is a class that contains only abstract methods.  
It defines a contract that subclasses must respect.  

Key points:  

- Interfaces in Python are created using abstract classes that contain only abstract methods.  
- They define a contract: all classes that inherit from the interface must implement the methods defined in that interface.  

**3. Using super() and abstract classes**  

super() is used to call a method or constructor of the parent class.  
This is very useful when using multiple inheritance or abstract classes.  

**4. When should abstract classes and interfaces be used?**  

Abstract classes:  
Use these when you have common behaviours between several classes, but you want to impose certain methods that the sub-classes must implement.  

- Interfaces:  
Use these to define a contract that classes must follow, especially when classes implement similar methods but need to define their own logic.  

Main difference:  
- An abstract class can contain both concrete methods (with implementation) and abstract methods.  
- An interface contains only abstract methods, which means that it contains only the declaration of methods, without any implementation.  

**Conclusion**   

Abstract classes and interfaces in Python are powerful tools for organising and structuring code in OOP.  
They allow you to force the implementation of specific methods in subclasses while sharing common behaviours.  
Although Python has no formal concept of interface, abstract classes can be used to create similar structures to respect contracts and enforce rules in code.  




0. Abstract Animal Class and its Subclasses  
1. Shapes, Interfaces, and Duck Typing  
2. Extending the Python List with Notifications  
3. CountedIterator - Keeping Track of Iteration  
4. The Enigmatic FlyingFish - Exploring Multiple Inheritance  
5. The Mystical Dragon - Mastering Mixins  
