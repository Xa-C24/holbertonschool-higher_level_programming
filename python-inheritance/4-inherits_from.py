#!/usr/bin/python3
def inherits_from(obj, a_class):
  """ 
  Returns True if the object is an instance of a class that inherits from the specified class, 
  but not if the object is a direct instance of the specified class. 
  """
  return isinstance(obj, a_class) and type(obj) != a_class
