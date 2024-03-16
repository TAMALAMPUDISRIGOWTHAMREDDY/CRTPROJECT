from abc import ABC, abstractmethod

class Ticket(ABC):
    @abstractmethod
    def book_ticket(self, name, ph_no, email, journey_date):
        pass

class MakeMyTrip(Ticket):
    def book_ticket(self, name, ph_no, email, journey_date):
        print("Thanks for booking from Make My Trip")

class IRCTC(Ticket):
    def book_ticket(self, name, ph_no, email, journey_date):
        trip = input("Enter the journey whether round or one-way: ")
        if trip.lower() == "round":
            end = input("Enter the return date: ")
        print("Thanks for booking from IRCTC")

class Indigo(Ticket):
    def init(self,name,ph_no,email,journey_date):
        mode = input("Enter which mode you want to travel (train, bus, flight): ")
        print("Thanks for Choosing Indigo")
name = input("Enter your name: ")
ph_no = input("Enter your phone number: ")
email = input("Enter your email: ")
journey_date = input("Enter the journey date: ")

n=int(input("enter the 1 for Make My Trip 2 for IRCTC 3 for Indigo"))
match n:
    case 1:
        obj1 = MakeMyTrip()
        obj1.book_ticket(name, ph_no, email,journey_date)
    case 2:
        obj2=IRCTC()
        obj2.book_ticket(name, ph_no, email,journey_date)
    case 3:
        obj3=Indigo()
        #obj3.book_ticket(name, ph_no, email,journey_date)
    case _:
        print("enter the valid option")
