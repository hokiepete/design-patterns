from copy import deepcopy

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y

class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        return deepcopy(self)
    
    def __eq__(self, __o: object) -> bool:
        return self.start == __o.start and self.end == __o.end

linea = Line(Point(0,0), Point(1,1))
lineb = linea.deep_copy()
print(linea==lineb)
lineb.end = Point(2,2)
print(linea==lineb)