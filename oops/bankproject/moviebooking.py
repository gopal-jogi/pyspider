def single_ton(cls):
    L=[]
    def inner():
        if len(L)==0:
            obj=cls()
            L.append(obj)
        return L[0]
    return inner

@single_ton
class leo:
    def __init__(self):
        self.tickets = 250
    def booking(self):
        tickets=int(input("Enter Numbers of  Tickets:- "))
        if self.tickets >= tickets:
            self.tickets -= tickets
            print("Tickets Confirm")
        else:
            print("Tickets Not Available")

@single_ton
class javan:
    def __init__(self):
        self.tickets = 250
    def booking(self):
        tickets=int(input("Enter Numbers of  Tickets:- "))
        if self.tickets >= tickets:
            self.tickets -= tickets
            print("Tickets Confirm")
        else:
            print("Tickets Not Available")

def BookMyshow():
    print("1. Leo /n 2. javan /n ")
    option=int(input("Choose Your Movie:- "))
    if option==1:
        l1=leo()
        l1.booking()
    elif option==2:
        j1=javan()
        j1.booking()
    else:
        print("Invalide Option")

while True:
    BookMyshow()
    print("_"*30)