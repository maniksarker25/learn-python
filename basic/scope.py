# scope

balance = 3000

def buy_things(item,price):
    # you can access global variable without using the global keyword
    # but if you want to modify a global variable into fun then you need to use global keyword
    global balance
    print("Previous balance",balance)
    balance = balance - price
    print("Balance  after buying ",balance)

buy_things("sunglass",1000)