# string is a sequences of character

name = "Manik Sarker"
name2 = 'manik\'s sarker' #escape \
name3 = """
    Sakib khan
    Number One
"""

# for char in name2:
#     print(char)
print(name2[3])
print(name2[2:5])
print(name2[-2])
print(name2[::-1]) # reserve
print(name)

print(name2.upper())

# string is mutable
# name2[0] = 'r' #TypeError: 'str' object does not support item assignment
# print(name2)

if "sarker" in name2:
    print("Exits")