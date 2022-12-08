# Challenge Task 1 of 3
#Using your Panda class, add two arguments to your class in the __init__ method called name and age. Set the values inside of the __init__ method using self.

#ln 11 and 12 were added for task 1 I added name, age in the pare on ln 9
class Panda:
    species = 'Ailuropoda melanoleuca'
    food = 'bamboo'

    def __init__(self, name, age):
        self.is_hungry = True
        self.name = name
        self.age = age
      
      #Challenge Task 2 of 3
#Create a method called eat. It should only take self as an argument. Inside of the method, set the is_hungry attribute to False, since the Panda will no longer be hungry when it eats. Also, return a string that says 'Bao Bao eats bamboo.' where 'Bao Bao' is the name attribute and 'bamboo' is the food attribute.
     
  def eat(self):
       self.is_hungry = False  
       name = "Bao Bao"
       return "{} eats {}.".format(self.name, self.food)
    
# Challenge Task 3 of 3