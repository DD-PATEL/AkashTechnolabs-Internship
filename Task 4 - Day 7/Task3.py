'''Task3 - Create a class cal3 that will calculate simple interest.
Create constructor method which has three parameters.
Create  calInterest() method that will calculate Interest.  
Create display() method that will display Interest.'''


class cal3():

    def __init__(self):
        self.P = float(input("Enter Principal= "))
        self.R = float(input("Enter Rate= "))
        self.T = float(input("Enter Time= "))
    
    def calInterest(self):
        self.interest = (self.P * self.R * self.T)/100
    
    def display(self):
        print("Your Simple Interest is ", self.interest)

cal = cal3()

cal.calInterest()
cal.display()

