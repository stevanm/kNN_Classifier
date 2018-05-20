from Point import Point
from Triangle import Triangle
from Delaunay2d import Delaunay2d


class Map:

    # List of triangulated map
    triangleList = [Triangle(Point(0,400), Point(200,400), Point(200, 600)),
                    Triangle(Point(0,400), Point(0,600), Point(200, 600))]


    def __init__(self):
        self.startPosition = Point(0,400) #start race position
        self.endPosition = None # end race position
        self.DelaunayTriangleList = list()


    # Triangulate map
    def TriangulateMap(self):
        self.DelaunayTriangleList = Delaunay2d()



    '''
    TODO:
    1. Trangulacija staze
    2. Singlton klasa
    3. Start i EndPosition da se obradi kad je presao trku i stigao do cilja
    4. Generisanje komplikovanije staze
    '''