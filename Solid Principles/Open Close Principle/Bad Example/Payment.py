class PaymentProcessor:
    def pay(self,payment_method:str,amount:float):
        if(payment_method=="Nagad"):
            print(f"Starting Nagad Transactions of Tk. {amount}")
            print("Nagad Transactions Finished")
        elif(payment_method=="Bkash"):
            print(f"Starting Bkash Transactions of Tk. {amount}")
            print("Bkash Transactions Finished")
        elif(payment_method=="NexusPay"):
            print(f"Starting Nexuspay Transactions of Tk. {amount}")
            print("NexusPay Transactions Finished")

p1=PaymentProcessor()
p1.pay("Nagad",1660)

#This violates the Open Close Principle because when we want to add new payment 
#we need to modify the pay method conditions . 
        