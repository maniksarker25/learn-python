# Class Attributes 
class Shop:
    cart = [] # cart is class attribute
    def __init__(self,buyer):
        self.buyer = buyer

    def add_to_cart(self,item):
        self.cart.append(item)


mahzabin = Shop("Meh jabin")
mahzabin.add_to_cart("Shoes")
mahzabin.add_to_cart("Phone")
print(mahzabin.cart)

nisho = Shop("Nisho")
nisho.add_to_cart("cap")
nisho.add_to_cart("watch")
print(nisho.cart)