#class - the keyword you use in Python to create an object
#Instantiation - creating an object from a class by calling the class like a function
#Instance - the object that was instantiated (created) Ex: Car()
#isinstance(object, type or class) - check if an object is an instance of the given type or class
#You can use print, type, and isinstance to see if you've correctly made an object.


class Car:
  pass

my_car = Car()

print(my_car)
print(type(my_car))
print(isinstance(my_car, Car))