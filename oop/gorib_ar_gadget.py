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
    

class Phone:
    def __init__(self,dual_sim):
        self.dual_sim = dual_sim

    def phone_call(self,number,text):
         return f'Sneding sms to: {number} and text: {text}'

    
class Camara:
    def __init__(self,pixel):
        self.pixel = pixel

        def change_lens(self):
            pass

