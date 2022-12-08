#Challenge Task 1 of 3
#Create a __str__ method for this book class. Return a string with the author and title of the book. Ex: John Green, Paper Towns example below on line 9-10 adding the comma was the key:

class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        
    def __str__(self):
        return f'{self.author}, {self.title}'

      #Add a __eq__ method for this book class. It should check if the author and title of the book are the same and return true if they are and false if they aren’t example below see ln 22-26.

    class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def __str__(self):
        return f'{self.author}, {self.title}'

    def __eq__(self, other):
        if self.author == other.author and self.title == other.title:
            return True
        else:
            return False
    
  
#Challenge Task 3 of 3
#I’ve added a Bookcase class inside bookcase.py. It will hold some books in a list. Add a __iter__ method so I can loop through the books. Use yield from and the book list inside the method.

