class Shopping:
    cart = [] # class attribute / static attribute
    origin = 'china'
    def __init__(self,name,location):
        self.name = "jamu na city" # instance attribute
        self.location = "Jam ar maj khana"

    def purchse(self,item,price,amount):
        remaining = amount - price
        print(f'buying : {item} for price : {price} and remaining: {remaining}')
    @classmethod
    def hudai_dakhi(self,item):
        print(f'Hudai dakhi kinmu na , ac ar haua khaita aisi',item)

    @staticmethod
    def multiply(a,b): # satic method a self daua laga na
        print(a*b)
    

basundara = Shopping("Basun dara","Kawran bazer")
basundara.purchse("lungi",500,1000)
Shopping.purchse("A",2,3,4) # if we want to use direact class then need to pass self

# basundara.hudai_dakhi("lungi")

Shopping.hudai_dakhi("Lungi") # use can use without self if we use classMethod decorator


Shopping.multiply(4,3)
