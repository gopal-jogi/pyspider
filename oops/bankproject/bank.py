class bank:
    bank_name="SBI"
    branch_name="Marathahalli"
    IFSC="SBI9090C100"
    ROI=0.06
    def __init__(self,name,acc_no,mno,bal,pin):
        self.name=name
        self.acc_no=acc_no
        self.mno=mno
        self.bal=bal
        self.pin=pin

    @staticmethod
    def autontication():
        return int(input("Enter Your 4-digite PIN:- "))
    def deposite(self):
        if self.pin==self.autontication():
            amount=int(input("Enter Your amount:- "))
            self.bal+=amount
            print(f"Deposited {amount} RS. Current balance: {self.bal} RS")
        else:
            print("Incorrect PIN")

    def withdraw(self):
        if self.pin==self.autontication():
            amount=int(input("Enter Your amount:- "))
            if self.bal>=amount:
                self.bal-=amount
                print(f"Withdrew {amount} RS. Current balance: {self.bal} RS")
            else:
                print("Insufficient funds!")
        else:
            print("Incorrect PIN")       
    def checkBalance(self):
        if self.pin==self.autontication():
            print(f"{self.name} account balance is {self.bal}")
        else:
            print("Incorrect PIN") 

    @classmethod
    def changeROI(cls):
        cls.ROI=float(input("Enter the New ROI:- "))
        print(f"New ROI is {cls.ROI}")

    def changePin(self):
        if self.pin==self.autontication():
            pin1=int(input("Enter Your New 4-digite PIN:- "))
            pin2=int(input("Enter Confirm 4-digit PIN:- "))
            if pin1==pin2:
                self.pin=pin1
                print("PIN changed successfully!")
            else:
                print("New PIN and confirmation PIN do not match. PIN change failed.")
        else:
            print("Incorrect PIN")

p1=bank("Gopal",8900232134,9807654321,100000000,1234)
p2=bank("Akshay",6789123454,6788012345,1000000,2345)

p1.changePin()


