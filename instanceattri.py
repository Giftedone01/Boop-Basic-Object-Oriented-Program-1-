class Car:
  
    #class attributes
    wheels = 4
    doors = 2
    engine = True

    def __init__(self, model, year, make = "Ford"):
        self.make = make
        self.model = model
        self.year = year
      
  
car_one = Car("Model T", 1908)  
car_two = Car("Benz", 1999, "Mercedes")
print(car_one.make)
print(car_two.make)

#print(car_one.model)
#print(car_two.model)
#print(car_one.year)
#print(car_two.year)
car_one.year = 2015
print(car_one.year)
print(car_two.year)