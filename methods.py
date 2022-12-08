class Car:
  
    #class attributes
    wheels = 4
    doors = 2
    engine = True

    def __init__(self, model, year, make = "Ford"):
        self.make = make
        self.model = model
        self.year = year



#a method below and they all take self
    def stop(self):
        print('The car has stopped')

    def go(self, speed):
        print(f'The car is going {speed}')
      

# ln 24 is an example of how to call a method
car_one = Car("Model T", 1908)  
car_two = Car("Benz", 1999, "Mercedes")
print(car_one.make)
print(car_two.make)
car_one.stop()