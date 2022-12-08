class Car:
  # class attributes
  wheels = 4
  steering = 1
  doors = 4 
  engine = True

car_one = Car()
car_two = Car()
print(f'car_one {car_one.doors}')
print(f' car_two {car_two.doors}')
print(f'Car {Car.doors}')
#print(car_one.steering)
#print(car_two.steering)


Car.doors = 7
car_one.doors = 6
car_two.doors = 6
print(f'car_one {car_one.doors}')
print(id(car_one.doors))
print(f'car_two {car_two.doors}')
print(id(car_two.doors))
print(f'Car {Car.doors}')
print(id(Car.doors))
