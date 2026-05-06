from abc import ABC
class DiscountStrategy(ABC):
    def calculate_discount(self):
        pass

class EidDiscount(DiscountStrategy):
    def calculate_discount(self):
        print("Eid discount 20%")
class FirstOrderDiscount(DiscountStrategy):
    def calculate_discount(self):
        print("First Order discount 30%")

class DiscountService:
    def __init__(self,discount_strategy:DiscountStrategy):
        self.__discount_strategy=discount_strategy
    def set_strategy(self):
        pass
        
