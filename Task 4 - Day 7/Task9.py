'''Task9 - Create a class called scheme with scheme_id, scheme_name, outgoing_rate and message_charge.
Derive customer class from scheme and include cust_id, name and mobile_no data.
Define necessary functions to read and display data.'''

class scheme:

    def sch(self):
        self.scheme_id = int(input('Enter scheme_id "1" for Jio, "2" for Airtel and "3" for Vodafone: '))
        
        self.scheme_name = ""
        if self.scheme_id == 1:
            self.scheme_name += "Jio"
            print("Your scheme is ", self.scheme_name)
        elif self.scheme_id == 2:
            self.scheme_name += "Airtel"
            print("Your scheme is ", self.scheme_name)
        elif self.scheme_id == 3:
            self.scheme_name += "Vodafone"
            print("Your scheme is ", self.scheme_name)
        else:
            print("You are using a different scheme")
            

        self.outgoing_rate = ""
        if self.scheme_id == 1:
            self.outgoing_rate += "Rs0.75/min"
            print("Outgoing rate is ", self.outgoing_rate)
        elif self.scheme_id == 2:
            self.outgoing_rate += "Rs1/min"
            print("Outgoing rate is ", self.outgoing_rate)
        elif self.scheme_id == 3:
            self.outgoing_rate += "Rs1.25/min"
            print("Outgoing rate is ", self.outgoing_rate)
        else:
            print("You are using a different scheme.")
            

        self.message_charge = ""
        if self.scheme_id == 1:
            self.message_charge += "Rs0.5/msg"
            print("Message charge is", self.message_charge)
        elif self.scheme_id == 2:
            self.message_charge += "Rs0.75/msg"
            print("Message charge is", self.message_charge)
        elif self.scheme_id == 3:
            self.message_charge += "Rs1/msg"
            print("Message charge is", self.message_charge)
        else:
            print("You are using a different scheme.")
            

class customer(scheme):

    def cus(self):
        self.customer_id = int(input("Enter customer id: "))

        self.name = ""
        if self.customer_id == 1:
            self.name += "John Wick"
            print("Customer name: ", self.name)
        elif self.customer_id == 2:
            self.name += "Jack Statham" 
            print("Customer name: ", self.name)
        elif self.customer_id == 3:
            self.name += "Jackie Chan"
            print("Customer name: ", self.name)
        else:
            print("Enter a valid customer id.")
    
        self.mobile_no = ""
        if self.customer_id == 1:
            self.mobile_no += "9876543210"
            print("Customer mobile number: ", self.mobile_no)
        elif self.customer_id == 2:
            self.mobile_no += "9898987676" 
            print("Customer mobile number: ", self.mobile_no)
        elif self.customer_id == 3:
            self.mobile_no += "9797976565"
            print("Customer mobile number: ", self.mobile_no)
        else:
            print("Enter a valid customer id")
            

c = customer()

c.sch()
c.cus()




