from abc import ABC,abstractmethod
class Account(ABC):
    def __init__(self,balance:float):
        self.balance=balance
    @abstractmethod
    def deposit():
        pass

class WithdrawableAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)
    @abstractmethod
    def withdraw():
        pass

class SavingAccount(WithdrawableAccount):
    def __init__(self, balance):
        super().__init__(balance)
    def deposit(self,amount):
        self.balance+=amount
        print(f"Depositted {amount}tk. Current Balance: {self.balance}tk")
        
    def withdraw(self,amount):
        self.balance-=amount
        print(f"Withdrawn {amount}tk . Current Balance:{self.balance}tk")
             

class FixedDeposit(Account):
    def __init__(self, balance):
        super().__init__(balance)
    def deposit(self,amount):
        print(f"Depositted {amount}tk. Current Balance:{self.balance+amount}")
        print("Depositted to Fixed Deposit Account")

acc1=SavingAccount(1000)
acc1.deposit(500)
acc1.withdraw(700)

acc2=FixedDeposit(1000)
acc2.deposit(300)
