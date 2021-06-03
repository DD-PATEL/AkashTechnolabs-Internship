'''Task6 - Create a class cal5 that will calculate area of a rectangle. 
Create a constructor method which has two parameters.
Create calArea() method that will calculate area of a rectangle.
Create display() method that will display area of a rectangle.'''

class cal5:
    
    def __init__(self):
        self.l = float(input("Enter length of Rectangle in meter: "))
        self.b = float(input("Enter breadth of Rectangle in meter: "))

    def calArea(self):
        self.a = self.l*self.b

    def display(self):
        print("Area of Rectangle is", self.a, "meter square")

c = cal5()

c.calArea()
c.display()