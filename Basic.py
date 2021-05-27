#Task 1- printing value of variables and finding variable type

a=7
b=3.6
c= "DD"

print("value of a is :", a)
print("value of b is :", b, type)
print(c)

#Task 2- Basic string commands such as printing and slicing of string

name = "Divyesh"

print(name)
print(name[1:5])
print(name[:4])
print("Hello", name)

#Task 3- Basic commands for list such as printing a list and creating a new list

l1 = [10, 'Oreo', 6.9, "Divyesh"]

print("l1 ="  ,l1)
print(l1[1])

list =[]
x= int(input("Enter number of elements in list :"))
for i in range(0,x):
    element=input("Enter value of Element: ")
    list.append(element)
print(list)  

#Task 4- Basic Tuple Commands such as printing, slicing and creating a new tuple

T1 = (8, 420, 10.7, "Attitude")
print("Third element of the tuple: ", T1[2])
print(T1[1:3])

list =[]
x= int(input("Enter number of Elements in tuple: "))
for i in range(0,x):
    element=input("Enter value of Element: ")
    list.append(element)
T2= tuple(list)
print(T2)

#Task 5- Basic Dictionary Commands such as printing value of a specific key

D1= {1: "DD", 2: "Patel", 3: 9}
print(D1[2])