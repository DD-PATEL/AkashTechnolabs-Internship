'''Task5 - Consider an employee class, which contains fields such as name and designation.
And a subclass, which contains a field salary. Write a program for inheriting this relation.'''

class employee:
    def emp(self):
        self.name = input("Enter your name:")
        self.designation = input("Enter your designation:")

class detail(employee):
    def det(self):
        self.salary = int(input("Enter your Salary:"))
        print("My name is", self.name, "and my salary for working as a", self.designation, "is $",self.salary)
        
c = detail()
c.emp()
c.det()





