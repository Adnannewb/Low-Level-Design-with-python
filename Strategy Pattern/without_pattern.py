class DiscountService:
    def calculate_discount(self,discount_type:str):
        if(discount_type=="Eid"):
            print("Eid discount 20%")
        elif(discount_type=="First order"):
            print("First Order discount 30%")
        elif(discount_type=="Puja"):
            print("Eid discount 15%")
        else:
            print("No Discount Applied")

ds=DiscountService()
ds.calculate_discount("First order")

#in that code whenever new strategy added it will need to change everytime on client side and 
#problem with testing 
#more if  else condition 