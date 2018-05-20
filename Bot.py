from Car import Car
from Item import Item

class Bot(Car):

    def __init__(self, x_coord, y_coord):
        super(Bot, self).__init__(x_coord, y_coord)
        super().name = "Bot Player: " + Item.id


'''
TODO:
1. Generisanje imena igraca - random
2. AI 
'''