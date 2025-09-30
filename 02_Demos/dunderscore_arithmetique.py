class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, other:"Point") -> "Point": # point1 + point2
        return Point(self.x + other.x, self.y + other.y)
    
    def __neg__(self): # -point
        return Point(-self.x, -self.y)

    def __abs__(self): # abs(point) valeur absolue
        return Point(abs(self.x), abs(self.y))

    def __str__(self):
        return f'Point x:{self.x}, y:{self.y}'
    
if __name__ == '__main__':
    p1 = Point(2,-3)
    p2 = Point(3,1)
    p3 = p1 + p2
    p4 = -p3
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(abs(p4))