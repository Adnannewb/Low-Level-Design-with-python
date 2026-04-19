from abc import ABC,abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass
class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass
    
class Robot(Workable):
    def work(self):
        print("Robot is working")

class Employee(Workable,Eatable):
    def work(self):
        print("Employee is working")
    def eat(self):
        print("Employee is eating")

worker1=Robot()
worker1.work()

worker2=Employee()
worker2.work()
worker2.eat()