from abc import ABC,abstractmethod
class DiscountStrategy(ABC):
    @abstractmethod
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
    
    def set_strategy(self,new_discount_strategy:DiscountStrategy):
        self.__discount_strategy=new_discount_strategy
    
    def process(self):
        self.__discount_strategy.calculate_discount()

ed=EidDiscount()
fo=FirstOrderDiscount()

ds=DiscountService(fo)
ds.process()

ds.set_strategy(ed)
ds.process()