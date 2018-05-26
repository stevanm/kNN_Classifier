import triangle
from Point import Point
from Triangle import Triangle


class VectorMap:

    def __init__(self):

        self.bounds = {

            'vertices': [  # outside boundary
                [890, 620],[1270, 620],[1410, 580],[1500, 500],
                [1530, 410],[1520, 200],[1490, 120],[1440, 70],
                [1350, 50],[1260, 50],[1120, 110],[930, 220],
                [800, 220],[600, 80],[460, 40],[320, 40],
                [170, 90],[90, 160],[50, 290],[70, 440],
                [150, 560],[280, 610],[420, 580],[530, 500],
                [570, 500],[700, 600],[780, 620],
                # inside boundary
                [890, 510],[1270, 510],[1390, 450],[1410, 400],
                [1410, 210],[1380, 170],[1330, 160],[1270, 170],
                [1170, 210],[940, 330],[790, 330],[550, 180],
                [450, 150],[330, 150],[220, 190],[180, 230],
                [160, 300],[180, 410],[240, 480],[310, 500],
                [390, 470],[510, 390],[570, 380],[730, 490],
                [780, 510],[890, 510]
            ],
            'segments': [  # outside boundary segments
                [0, 1],[1, 2],[2, 3],[3, 4],
                [4, 5],[5, 6],[6, 7],[7, 8],
                [8, 9],[9, 10],[10, 11],[11, 12],
                [12, 13],[13, 14],[14, 15],[15, 16],
                [16, 17],[17, 18],[18, 19],[19, 20],
                [20, 21],[21, 22],[22, 23],[23, 24],
                [24, 25],[25, 26],[26, 0],
                # inside boundary segments
                [27, 28],[28, 29],[29, 30],[30, 31],
                [31, 32],[32, 33],[33, 34],[34, 35],
                [35, 36],[36, 37],[37, 38],[38, 39],
                [39, 40],[40, 41],[41, 42],[42, 43],
                [43, 44],[44, 45],[45, 46],[46, 47],
                [47, 48],[48, 49],[49, 50],[50, 51],
                [51, 52],[52, 53]
            ],
            'holes': [
                [550, 550],[850, 200],[1000, 400]
            ]
        }

        # Constrained Delaunay triangulation
        self.triangulation = triangle.triangulate(self.bounds, opts='pc')
        self.triangulatedPoints =  self.triangulation['vertices']
        self.triangles = self.triangulation['triangles']
        self.segments = self.triangulation['segments']
        self.triangleObjects = list()
        self.getTriangleList()

    def getTriangleList(self):
        for t in self.triangles:
            tr = Triangle(
                Point(self.triangulatedPoints[t[0]][0], self.triangulatedPoints[t[0]][1]),
                Point(self.triangulatedPoints[t[1]][0], self.triangulatedPoints[t[1]][1]),
                Point(self.triangulatedPoints[t[2]][0], self.triangulatedPoints[t[2]][1]))
            self.triangleObjects.append(tr)
        return

