# print("Enter a number: ")
# input()

# input("Give me some money: ")

# money = input("Give me some money: ")
# print("Here is your money", money)


versity_cost = input("Versity cost: ")
house_rent = input("House rent: ")
# print(type(versity_cost)) // by default input type is string
# type casting
versity_cost_int = int(versity_cost)
house_rent_int = int(house_rent)
print("Money debit", versity_cost , "and", house_rent)
totalcost = versity_cost_int + house_rent_int
print("Total cost",totalcost)