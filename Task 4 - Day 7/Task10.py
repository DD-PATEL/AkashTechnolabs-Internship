'''Task10 - Create a arith class. The class should have a parameterized constructor and methods to
add, subtract and multiply two numbers and to return the answers.'''

class arith:

    def __init__(self):

        self.x = int(input("Enter first number: "))
        self.y = int(input("Enter second number: "))
        x = self.x
        y = self.y 

        self.add = x + y
        self.sub = x - y
        self.mul = x * y

c = arith() 

print("Addition is ", c.add)
print("Subtraction is ", c.sub)
print("Multiplication is ", c.mul)
