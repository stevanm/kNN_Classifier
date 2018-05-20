from Car import Car

class Player(Car):

    def __init__(self, playerName, x, y):
        self.name = playerName
        super().__init__(x,y)
