'''Task1 - Create a class cal1 that will calculate sum of three numbers. 
 Create setdata() method which has three parameters that contain numbers. 
 Create display() method that will calculate sum and display sum.'''


class cal1:

    def setdata(self):
        self.x = int(input("Enter first number: "))
        self.y = int(input("Enter second number: "))
        self.z = int(input("Enter third number: "))

    def display(self):
        total = self.x+self.y+self.z
        print("Sum of three number is ", total)

cal = cal1()

cal.setdata()
cal.display()