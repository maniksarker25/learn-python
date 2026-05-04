# parent class / base class/ common attribute + funtionality class
class Gadget:
    def __init__(self,brand,price,color,origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

        def run(self):
          return f'Running laptop: {self.brand}'


# derived class, child class , uncommon attribute + funtionality class
class Laptop:
    def __init__(self,memory,ssd):
        self.memoery = memory
        self.ssd = ssd
    
    def coding(self):
        return f'Learning python and practicing'
    

class Phone(Gadget):
    def __init__(self,brand,price,color,origin,dual_sim):
        self.dual_sim = dual_sim
        # super for use parent class
        super().__init__(brand,price,color,origin)

    def phone_call(self,number,text):
         return f'Sneding sms to: {number} and text: {text}'

    def __repr__(self):
        return f'Phone: {self.brand},{self.price}'
class Camara:
    def __init__(self,pixel):
        self.pixel = pixel

        def change_lens(self):
            pass


# inheritance

my_phone = Phone("Iphone",12000,"silver",'china',True)
print(my_phone)