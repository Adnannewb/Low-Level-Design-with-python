from abc import ABC,abstractmethod

class BankAccount(ABC):
    def __init__(self,balance:float):
        self.balance=balance
        
    @abstractmethod
    def deposit():
        pass
    @abstractmethod
    def withdraw():
        pass
class SavingAcc(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)
    def deposit(self,amount):
        self.balance+=amount
        print(f"Depositted {amount}tk. Current Balance:{self.balance}")
        print("Depositted to Saving Account")
    def withdraw(self,amount):
        if(self.balance<amount):
            print("Cannot Withdraw")
        else:
            self.balance-=amount
            print(f"Withdrow {amount}tk. Current Balance={self.balance}")
        print("Withdrawn from Saving Account ")
class FixedDeposit(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)
    def deposit(self,amount):
        print(f"Depositted {amount}tk. Current Balance:{self.balance+amount}")
        print("Depositted to Fixed Deposit Account")
    def withdraw(self,amount):
        raise Exception("Cannot withdrawn from Fixed Deposit account ")

acc1=SavingAcc(1000)
acc1.deposit(500)
acc1.withdraw(700)

acc2=FixedDeposit(1000)
acc2.deposit(300)
acc2.withdraw(500)

#this violates Liskov Substitution Principle 
# because  Fixed deposit doesen't have withdraw option but as it inherited from the bank account class
#it should follow that method 

