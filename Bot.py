from Car import Car

class Bot(Car):


    def __init__(self, botname, x_coord, y_coord,a,b):
        super().__init__(x_coord,y_coord,a,b)
        self.carModelPhoto = self.setCarModelPhoto()
        self.name = "Bot Player: " + botname
