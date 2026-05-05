# poly ---> many (multiple)
# morph --> shape

class Animal:
    def __init__(self,name):
        self.name = name

    def make_sound(self):
        print("Animal making some sound")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        print("Meow meow")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print("Gheu Gheu")

class Goat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Beh beh beh")


don = Cat("Real Don")
don.make_sound()

shepard = Dog("Local Shephard")
shepard.make_sound()

mess = Goat("L M")
mess.make_sound()

less = Goat("Gora gori")


animals = [don,shepard,mess,less]

for animal in animals:
    animal.make_sound()
