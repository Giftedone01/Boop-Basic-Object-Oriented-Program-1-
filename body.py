class Body:
# class attributes
  legs = 2
  arms = 2
  eyes = 2
  ears = 2
  heart = True

body_one = Body()
body_two = Body()
print(body_one.legs)
print(body_two.legs)
print(Body.legs)

# see example below of changing attributes
body_one.legs = 4
body_two.legs = 4
print(f'body_one.legs {body_one.legs}')
print(id(body_one.legs))
print(f'body_two.legs {body_two.legs}')
print(id(body_two.legs))
print(f'Body {Body.legs}')
print(id(Body.legs))

#print(f'car_one.doors {car_one.doors}')
#print(f'car_two.doors {car_two.doors}')
#print(f'Car {Car.doors}')


my_body = Body()

#print(my_body)
#print(type(my_body))
#print(isinstance(my_body, Body))