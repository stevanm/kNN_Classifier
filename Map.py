from Point import Point
import numpy as np
from VectorMap import VectorMap


class Map:

    def __init__(self, w, h):
        self.winWidth = w
        self.winHeight = h
        self.startPosition = Point(100,300) #start race position
        self.endPosition = None # end race position
        self.vectorMap = VectorMap()
        self.TriangleList = self.vectorMap.triangleObjects
        self.relativeCheckLines = [[Point(0.5, 0.4), Point(0.5, 0.2)],[Point(0.6, 0.5), Point(0.8, 0.5)],[Point(0.5, 0.6), Point(0.5, 0.8)],[Point(0.2, 0.5), Point(0.4, 0.5)]]
        self.checkLines = list(map(lambda x: self.scaleCheckpoints(x), self.relativeCheckLines))


    def scaleCoordinates(self, x):
        return np.array([x[0] * self.winWidth, x[1] * self.winHeight])

    def scaleCheckpoints(self, p):
        return [Point(p[0].x * self.winWidth, p[0].y * self.winHeight),
                Point(p[1].x * self.winWidth, p[1].y * self.winHeight)]

    '''
    TODO:
    2. Singlton klasa
    3. Start i EndPosition da se obradi kad je presao trku i stigao do cilja
    '''


