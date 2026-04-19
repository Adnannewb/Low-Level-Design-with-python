from abc import ABC,abstractmethod
class PaymentMethod(ABC):
    
    @abstractmethod
    def pay(self,amount:float):
        pass
class Nagad(PaymentMethod):
    def pay(self,amount:float):
        print(f"Nagad Transactions of Tk. {amount}")
class Bkash(PaymentMethod):
    def pay(self,amount:float):
        print(f"Bkash Transactions of Tk. {amount}")

# class NexuxPay(PaymentMethod):
#     def pay(self,amount:float):
#         print(f"Nexuspay Transactions of Tk. {amount}")

class PaymentProcessor:
    def process_method(self,payment_method:PaymentMethod,amount:float):
        payment_method.pay(amount)

p1=Nagad()
p2=Bkash()
# p3=NexuxPay()

payment_proc=PaymentProcessor()
payment_proc.process_method(p1,500)
payment_proc.process_method(p2,5000)
# payment_proc.process_method(p3,10000)


#in this if i want to add new payment method i dont need to modify any existing code ,
# all i need to do is add new payment method class and just object call 
#No modifications only extensions 