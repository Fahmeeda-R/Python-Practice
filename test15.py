class Shape:
    def area(self):
        print("Area of shape")
class Circle(Shape):
    def area(self):
        r=5
        print("Area of circle:",3.14*r*r)
class Rectangle(Shape):
    def area(self):
        l=12
        b=4
        print("Area of rectangle:",l*b)
c1=Circle()
r1=Rectangle()
c1.area()
r1.area()