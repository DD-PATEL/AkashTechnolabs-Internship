'''Task4 - Create a class cal4  that will calculate square of a number.
Create setdata() method which has one parameters that contain number.
Create display() method that will calculate sum.(Function should return value)'''

class cal4:

    def setdata(self):
        self.n = int(input("Enter a number:"))

    def display(self):
        return self.n*self.n
    

cal = cal4()

cal.setdata()
cal.display()
print("Square of your number is ", cal.display())
        
        
