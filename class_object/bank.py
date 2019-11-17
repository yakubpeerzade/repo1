import random
class Bank:
    def __init__(self):
        self.balance=random.randrange(500,999999)
        
    def Balance(self):
        print("Available Balance=",self.balance)
    def withdraw(self):
         amount=int(input("Enter Withdrwa amount:"))
         if self.balance>amount:
            self.balance=self.balance-amount
            print("Available Balance=",self.balance)
         else:
            print("Sorry!!! Insufficient Balance")
            Balance()
    def Deposite(self):
        amount=int(input("Enter deposite amount:"))
        self.balance=self.balance+amount
        print("Available Balance=",self.balance)
        
if __name__=='__main__':
    B1=Bank()
    while True:
        choice=int(input("1)Check Balance\n2)Deposit\n3)withdraw\n4)Exit\nEnter Your choice:"))
        if choice==1:
            B1.Balance()
        elif choice==2:
            B1.Deposite()
        elif choice==3:
            B1.withdraw()
        elif choice==4:
            exit()
        
        
        
