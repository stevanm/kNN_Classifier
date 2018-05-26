from Point import Point
import numpy as np
from VectorMap import VectorMap


class Map:

    def __init__(self, w, h):
        self.winWidth = w
        self.winHeight = h
        self.startPosition = Point(890,565) #start race position
        self.endPosition = None # end race position
        self.vectorMap = VectorMap()
        self.TriangleList = self.vectorMap.triangleObjects
        self.checkLines = [[Point(1420, 450), Point(1480, 530)], [Point(1360, 140), Point(1440, 80)],
                           [Point(900, 225), Point(900, 335)], [Point(360, 50), Point(440, 130)],
                           [Point(90, 410), Point(190, 410)],[Point(470, 420), Point(470, 520)],[Point(890, 510), Point(890, 620)]]



    def scaleCoordinates(self, x):
        return np.array([x[0] * self.winWidth, x[1] * self.winHeight])

    '''
    TODO:
    2. Singlton klasa
    3. Start i EndPosition da se obradi kad je presao trku i stigao do cilja
    '''


