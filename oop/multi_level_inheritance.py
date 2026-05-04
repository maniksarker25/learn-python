class Vehicle:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{self.name}, {self.price}'

    def move(self):
        pass

class Bus(Vehicle):
    def __init__(self, name, price,seat):
        self.seat = seat
        super().__init__(name, price)

    def __repr__(self):
        return super().__repr__()
    
class Truck(Vehicle):
    def __init__(self, name, price,weight):
        self.weight = weight
        super().__init__(name, price)
class PicputTruck(Truck):
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)

class AcBus(Bus):
    def __init__(self, name, price, seat,temperature):
        self.temperature = temperature
        super().__init__(name, price, seat)
    def __repr__(self):
        return super().__repr__()
    def move(self):
        pass

green_line = AcBus("green",500000,22,16)
print(green_line)
print(green_line.price)