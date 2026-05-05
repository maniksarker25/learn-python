#abstrack base class
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod # enforce all derived calss to have a eat method
    def eat(self):
        print("I need food!")
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self,name):
        self.name = name
        self.category = 'Monkey'
        super().__init__()
    
    def eat(self):
        print("Hey nanana, i am eating banana")

layka = Monkey("laika")
layka.eat()