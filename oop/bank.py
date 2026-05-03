class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
    
    def withdraw(self,amount):
        if amount < self.min_withdraw:
            print (f'You can not withdraw below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print (f'YOu can not withdraw more then {self.max_withdraw}')
        elif amount > self.balance:
            print (f'Insufficient balance is')
        else:
            self.balance -= amount
            print (f'Here is your updated balance {self.balance}')
        
brac = Bank(15000)
brac.withdraw(1000)