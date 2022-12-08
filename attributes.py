class Car:
  
    #class attributes
    wheels = 4
    doors = 2
    engine = True

    def __init__(self):

car_one = Car()
car_two = Car()
print(car_one.doors)
print(car_two.doors)
print(Car.doors)

Car.doors = 4
print(car_one.doors)
print(car_two.doors)
print(Car.doors)

my_car = Car()

print(my_car)
print(type(my_car))
print(isinstance(my_car, Car))