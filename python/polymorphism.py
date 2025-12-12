class circle:
    def area(self, radius):
        return 3.14 * radius * radius


class square:
    def area(self, side):
        return side * side


class rectangle:
    def area(self, length, breadth):
        return length * breadth


c = circle()
s = square()
r = rectangle()
print("Area of Circle:", c.area(5))
print("Area of Square:", s.area(4))
print("Area of Rectangle:", r.area(4, 6))
