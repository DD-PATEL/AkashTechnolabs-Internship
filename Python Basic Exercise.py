#1 - Calculate average of 5 numbers

total=0
for i in range(0,5):
    num=int(input("Enter a number: "))
    total += num
avg = total/5
print('Average of 5 numbers= ', avg)


#2 - Check whether number is even or odd

x=int(input("Enter a number: "))
if x%2==0:
    print("Number is even")
else:
    print("Number is odd")


#3 - Take a year and check whether it is leap year or not

y=int(input("Enter year: "))
if y%4==0:
    if y%400:
        if y%100!=0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
else:
    print("It is not a leap year")


#4 - Take a number amd check whether it is zero, positive or negative.

x=int(input("Enter a number: "))
if x>0:
    print("Number is positive")
elif x==0:
    print("Number is zero")
else:
    print("Number is negative")


#5 - Take 2 numbers and display greatest number.

num1=int(input("Enter a first number: "))
num2=int(input("Enter a second number: "))
if num1>num2:
    print("First number is greatest")
if num1<num2:
    print("Second number is greatest")
else:
    print("Both number are equal numbers")


#6 - Take a number and find factorial of that number.

x=int(input("Enter a number: "))
factorial = 1
for i in range(1, x+1): 
    factorial = factorial * i
print("Factorial of your number is ", factorial)


#7 - Write a program to swap 2 numbers using third variable

x= int(input("Enter first number n1: "))
y= int(input("Enter second number n2: "))

temp = x
x = y
y = temp 

print("n1: ", x)
print("n2: ", y)


#8 - Take 2 numbers and find smallest number.

n1=int(input("Enter first number n1: "))
n2=int(input("Enter second number n2: "))

if n1>n2:
    print("n2 is smaller than n1")
if n1<n2:
    print("n1 is smaller than n2")
else:
    print("n1 and n2 are equal numbers")


#9 - Take a number check if the number is less than 100 or not. If it is less than 100 then check if is odd or even

x=int(input("Enter a number: "))
if x<100:
    if x%2==0:
        print("Number is less than 100 and number is even")
    else:
        print("Number is less than 100 and number is odd")
else:
    print("Number is greater than 100")


#10 - Take a number to print square of a number if it is less than 10.

x=int(input("Enter a number: "))
if x<10:
    y=x**2
    print("The square of the given number is: ", y)
else:
    print("The given number is greater than 10")


#11 - Take a number and check whether it is a zero, positive or negative using nested IF...ELSE statement.

x=int(input("Enter a number: "))
if x>=0:
    if x>0:
        print("Number is positive")
    else:
        print("Number is zero")
else:
    print("Number is negative")


#12 - Take 3 numbers and find greatest number using nested IF...ELSE statement

n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
n3=int(input("Enter third number:"))
if n1>n2:
    if n1>n3:
        print("n1 is the greatest number")
    else:
        print("n3 is the greatest number")
elif n2>n1:
    if n2>n3:
        print("n2 is the greatest number")
    else:
        print("n3 is the greatest number")


#13 - Take 3 numbers and find smallest number using logical operator.

n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
n3=int(input("Enter third number:"))
if n1>n2 and n1>n3:
    print("n1 is the greatest number")
elif n2>n1 and n2>n3:
    print("n2 is the greatest number")
else:
    print("n3 is the greatest number")


#14 - Write a program to swap 2 numbers without taking third variable

n1=int(input("Enter first number n1:"))
n2=int(input("Enter second number n2:"))

print("n1: ", n2)
print("n2: ", n1)


#15 - Take starting number and ending number from the user and print descending series in multiple of 3.

x=int(input("Enter starting number: "))
y=int(input("Enter ending number: "))
for i in (range(x,y-1,-3)):
    print(i)









