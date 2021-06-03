'''Task8 - Write a program with use of inheritance:
Define a class publisher that stores the name of the title.
Derive two classes book and tape, which  inherit publisher.
Book class contains member data called page no and tape class contain time for playing.
Define functions in the appropriate classes to get and print the details.'''

class publisher:
    def title(self):
        self.name = input("Enter Title: ")


class book(publisher):
    def data(self):
        self.pgn = int(input("Enter number of pages: "))
        

class tape(publisher):
    def time(self):
        self.t = input("Enter time for playing: ")
    

class temp(tape, book):
    def tmp(self):
        print("Title of the book is", self.name, ". This book contains", self.pgn, "number of pages and it will take", self.t, "mins to play.")

c= temp()

c.title()
c.data()
c.time()
c.tmp()