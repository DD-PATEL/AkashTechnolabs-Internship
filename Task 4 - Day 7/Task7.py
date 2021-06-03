'''Task7 - Create a class cal6 that will calculate area of a square.
Create setdata() method that should take length from the user.
Create area() method that will calculate area.
Create display() method that will display area.'''

class cal6:

    def setdata(self):
        self.l = int(input("Enter length of the square in meters: "))

    def area(self):
        self.a = self.l**2

    def display(self):
        print("Area of the Square is", self.a, "meter square.")

c = cal6()

c.setdata()
c.area()
c.display()
