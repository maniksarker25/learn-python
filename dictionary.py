
numbers = [12,32,55,35,53,646,64,64,64,12]


person = {"name":"Kala Pakhi","address":"Kaliapur","age":23,"job":"student"}

print(person)
print(person["job"])

print(person.keys())
print(person.values())
person["language"] = "python"
del person['age']
print(person)

# special dictoionary looping

for key,value in person.items():
    print(key,value)