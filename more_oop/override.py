class Person:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def eat(self):
        print("Vat mangso polaw korma")
    # force to override on derived class
    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, weight,team):
        self.team = team
        super().__init__(name, age, height, weight)

    # override---------
    def eat(self):
        print("Vagetables")

    def exercise(self):
        print("Gym a gia gam jorai")

    def __add__(self,other):
        return self.age + other.age
    
    def __mul__(self,other):
        return self.weight * other.weight
    
    def __len__(self):
        return self.height
    def __gt__(self,other):
        return self.age > other.age


sakib = Cricketer("Sakib",39,68,91,"BD")
musi = Cricketer("Mushi",36,65,78,"BD")
# sakib.eat()
# sakib.exercise()


print(45+63)
print("Sakib"+ "Rakib")
print([12,65] + [3,5,7,2])
# operator overloading
print(sakib + musi)
print(sakib * musi)
print(len(sakib))
print(sakib>musi)