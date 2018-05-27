from Point import Point
import numpy as np
from VectorMap import VectorMap
from Triangle import Triangle


class Map:

    def __init__(self, w, h):
        self.winWidth = w
        self.winHeight = h
        self.startPosition = Point(890,565) #start race position
        self.endPosition = None # end race position
        #self.vectorMap = VectorMap()
        #self.TriangleList = self.vectorMap.triangleObjects
        self.TriangleList = [Triangle(Point(1270.0,510.0), Point(890.0,620.0), Point(890.0,510.0)),Triangle(Point(780.0,510.0), Point(780.0,620.0), Point(700.0,600.0)),Triangle(Point(1500.0,500.0), Point(1390.0,450.0), Point(1410.0,400.0)),Triangle(Point(1500.0,500.0), Point(1410.0,400.0), Point(1530.0,410.0)),Triangle(Point(1270.0,510.0), Point(1270.0,620.0), Point(890.0,620.0)),Triangle(Point(1270.0,620.0), Point(1270.0,510.0), Point(1410.0,580.0)),Triangle(Point(1410.0,580.0), Point(1270.0,510.0), Point(1390.0,450.0)),Triangle(Point(1390.0,450.0), Point(1500.0,500.0), Point(1410.0,580.0)),Triangle(Point(1520.0,200.0), Point(1530.0,410.0), Point(1410.0,400.0)),Triangle(Point(800.0,220.0), Point(790.0,330.0), Point(550.0,180.0)),Triangle(Point(90.0,160.0), Point(170.0,90.0), Point(220.0,190.0)),Triangle(Point(220.0,190.0), Point(170.0,90.0), Point(330.0,150.0)),Triangle(Point(90.0,160.0), Point(220.0,190.0), Point(180.0,230.0)),Triangle(Point(50.0,290.0), Point(180.0,230.0), Point(160.0,300.0)),Triangle(Point(180.0,230.0), Point(50.0,290.0), Point(90.0,160.0)),Triangle(Point(70.0,440.0), Point(50.0,290.0), Point(160.0,300.0)),Triangle(Point(450.0,150.0), Point(320.0,40.0), Point(460.0,40.0)),Triangle(Point(450.0,150.0), Point(460.0,40.0), Point(600.0,80.0)),Triangle(Point(450.0,150.0), Point(330.0,150.0), Point(320.0,40.0)),Triangle(Point(450.0,150.0), Point(600.0,80.0), Point(550.0,180.0)),Triangle(Point(320.0,40.0), Point(330.0,150.0), Point(170.0,90.0)),Triangle(Point(150.0,560.0), Point(70.0,440.0), Point(180.0,410.0)),Triangle(Point(180.0,410.0), Point(70.0,440.0), Point(160.0,300.0)),Triangle(Point(150.0,560.0), Point(180.0,410.0), Point(240.0,480.0)),Triangle(Point(240.0,480.0), Point(280.0,610.0), Point(150.0,560.0)),Triangle(Point(280.0,610.0), Point(240.0,480.0), Point(310.0,500.0)),Triangle(Point(280.0,610.0), Point(310.0,500.0), Point(420.0,580.0)),Triangle(Point(530.0,500.0), Point(390.0,470.0), Point(510.0,390.0)),Triangle(Point(570.0,500.0), Point(570.0,380.0), Point(730.0,490.0)),Triangle(Point(570.0,380.0), Point(570.0,500.0), Point(530.0,500.0)),Triangle(Point(530.0,500.0), Point(420.0,580.0), Point(390.0,470.0)),Triangle(Point(700.0,600.0), Point(570.0,500.0), Point(730.0,490.0)),Triangle(Point(510.0,390.0), Point(570.0,380.0), Point(530.0,500.0)),Triangle(Point(730.0,490.0), Point(780.0,510.0), Point(700.0,600.0)),Triangle(Point(390.0,470.0), Point(420.0,580.0), Point(310.0,500.0)),Triangle(Point(550.0,180.0), Point(600.0,80.0), Point(800.0,220.0)),Triangle(Point(1120.0,110.0), Point(1260.0,50.0), Point(1270.0,170.0)),Triangle(Point(1270.0,170.0), Point(1260.0,50.0), Point(1330.0,160.0)),Triangle(Point(1120.0,110.0), Point(1270.0,170.0), Point(1170.0,210.0)),Triangle(Point(930.0,220.0), Point(1120.0,110.0), Point(1170.0,210.0)),Triangle(Point(940.0,330.0), Point(930.0,220.0), Point(1170.0,210.0)),Triangle(Point(800.0,220.0), Point(930.0,220.0), Point(940.0,330.0)),Triangle(Point(1380.0,170.0), Point(1350.0,50.0), Point(1440.0,70.0)),Triangle(Point(1380.0,170.0), Point(1440.0,70.0), Point(1490.0,120.0)),Triangle(Point(1380.0,170.0), Point(1330.0,160.0), Point(1350.0,50.0)),Triangle(Point(1410.0,210.0), Point(1520.0,200.0), Point(1410.0,400.0)),Triangle(Point(1410.0,210.0), Point(1380.0,170.0), Point(1490.0,120.0)),Triangle(Point(1490.0,120.0), Point(1520.0,200.0), Point(1410.0,210.0)),Triangle(Point(1350.0,50.0), Point(1330.0,160.0), Point(1260.0,50.0)),Triangle(Point(940.0,330.0), Point(790.0,330.0), Point(800.0,220.0)),Triangle(Point(780.0,620.0), Point(890.0,510.0), Point(890.0,620.0)),Triangle(Point(890.0,510.0), Point(780.0,620.0), Point(780.0,510.0))]
        self.checkLines = [[Point(940, 565), Point(940, 566)], [Point(990, 565), Point(990, 566)], \
                       [Point(1060, 560), Point(1060, 570)], [Point(1160, 570), Point(1160, 560)], \
                       [Point(1300, 560), Point(1300, 562)], [Point(1440, 490), Point(1440, 491)], \
                       [Point(1460, 430), Point(1460, 431)], [Point(1465, 330), Point(1465, 331)], \
                       [Point(1440, 160), Point(1440, 161)], [Point(1350, 100), Point(1350, 101)], \
                       [Point(1220, 130), Point(1220, 131)], [Point(1070, 200), Point(1070, 201)], \
                       [Point(850, 280), Point(850, 281)], [Point(680, 200), Point(680, 201)], \
                       [Point(500, 100), Point(500, 101)], [Point(300, 100), Point(300, 101)], \
                       [Point(150, 170), Point(150, 171)], [Point(110, 370), Point(110, 371)], \
                       [Point(200, 520), Point(200, 521)], [Point(420, 520), Point(420, 521)], \
                       [Point(560, 440), Point(560, 441)], [Point(750, 550), Point(750, 551)]]
