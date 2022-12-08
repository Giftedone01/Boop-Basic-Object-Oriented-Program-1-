class Game:
  def __init__(self):
    self.size = 4
    self.card_options = ['Add', 'Boo', 'Cat', 'Dev', 
                         'Egg', 'Far', 'Gum', 'Hut']  
    self.columns = ['A', 'B', 'C', 'D']
    self.cards = []
    self.locations = []
    for column in self.columns:
          for num in range(1, self.size + 1):
             print(f'{column}{num}')



 #if __name == '__main__':  
 #Game()
  