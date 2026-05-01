#set : unique items collections

numbers = [12,32,55,35,53,646,64,64,64,12]

# print(numbers)
numbers_set = set(numbers)

print(numbers_set)

numbers_set.add(51)
# numbers_set[1] = 5 # not posible to set
numbers_set.remove(55)
print(numbers_set)


for item in numbers_set:
    print(item)


if 9 in  numbers_set:
    print("Ache")
else:
    print("nai")