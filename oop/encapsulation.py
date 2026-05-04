# encapsulation
# access modifier (private,public,protected)
#__ private(__balance)
class Bank:
    def __init__(self,holder_name,initial_deposit):
        self.holder_name = holder_name
        self._brance = 'banani'
        self.__balance = initial_deposit

    def deposit(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    def withdraw(self,amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'Forira taka nai'
        

rafsan = Bank("Choto bro",1000)
print(rafsan.holder_name)
print(rafsan._brance)
# print(rafsan.__balance) # private variable not posible to access 
rafsan.deposit(3000)
print(rafsan.get_balance())

# churi kora jai ababa
print(dir(rafsan))
print(rafsan._Bank__balance)