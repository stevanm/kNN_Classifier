from Item import Item

class Car(Item):

    # X, Y
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.speed_x = 0
        self.speed_y = 0
        self.available = True


    '''
    @property
    def x(self):
        return self.__x

    @name.setter
    def name(self, x_coord):
        self.__x = x_coord


    @property
    def y(self):
        return self.__y

    @name.setter
    def name(self, y_coord):
        self.__y = y_coord
    '''