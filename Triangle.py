from Point import Point

class Triangle:

    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    # vector product
    def vectorProduct(self, m, t1, t2):
        return (t1.x - m.x) * (t2.y - m.y) - (t1.y - m.y) * (t2.x - m.x)

    # point p inside triangle
    def isInside(self, p):
        return (self.vectorProduct(p, self.p1, self.p2) >= 0 and \
                self.vectorProduct(p, self.p2, self.p3) >= 0 and \
                self.vectorProduct(p, self.p3, self.p1) >= 0) or  \
               (self.vectorProduct(p, self.p1, self.p2) <= 0 and \
                self.vectorProduct(p, self.p2, self.p3) <= 0 and \
                self.vectorProduct(p, self.p3, self.p1) <= 0)

    def __str__(self):
        return "(" + str(self.p1) + ", " + str(self.p2) + ", " + str(self.p3) + ")"
