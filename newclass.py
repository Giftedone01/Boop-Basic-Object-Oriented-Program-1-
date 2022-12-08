class Car:
# # class attributes
  
  wheels = 4
  doors = 2
  engine = True

car_one = Car()
car_two = Car()
print(car_one.doors)
print(car_two.doors)
print(Car.doors)

# see example below of changing attributes
car_one.doors = 4
car_two.doors = 4
print(car_one.doors)
print(car_two.doors)
print(Car.doors)

car_one.doors = 6
Car.doors = 3 
print(f'car_one.doors {car_one.doors}')
print(id(car_one.doors))
print(f'car_two.doors {car_two.doors}')
print(id(car_two.doors))
print(f'Car {Car.doors}')
print(id(Car.doors))


my_car = Car()

#print(my_car)
#print(type(my_car))
#print(isinstance(my_car, Car))