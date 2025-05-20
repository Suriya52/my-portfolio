# Abstraction is Hiding unnecessary details

# Abstract Class and Abstract Method

# -> Abstract Class

from abc import ABC, abstractmethod 

class Car(ABC):
    @abstractmethod
    def movingforword(self):
        pass

    @abstractmethod
    def movingbackword(self):
        pass
    @abstractmethod
    def fm(self):
        pass

class RollsRoy(Car):
    def movingforword(self):
        print("Rolls Roy Car is moving Forword!")

    def movingbackword(self):
        print("Rolls Roy Car is moving Backword!")

    def fm(self):
        print("Rolls Roy Car is playing FM!")
    
class BMW(Car):
    def movingforword(self):
        print("BMW Car is moving Forword!")

    def movingbackword(self):
        print("BMW Car is moving Backword!")

    def fm(self):
        print("BMW Car is playing FM!")
    
RollsRoy=RollsRoy()
RollsRoy.movingbackword()
