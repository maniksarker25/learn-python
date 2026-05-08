class Person:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Cricketer(Person):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age, height, weight)

     # operator overloading for >
    def __gt__(self, other):
        return self.age > other.age

    # operator overloading for <
    def __lt__(self, other):
        return self.age < other.age

    # operator overloading for ==
    def __eq__(self, other):
        return self.age == other.age
    

sakib = Cricketer('Sakib', 38, 68, 91)
musfiq = Cricketer('Rahim', 36, 68, 88)
kamal = Cricketer('Kamal', 39, 68, 94)
jack = Cricketer('Jack', 38, 68, 91)
kalam = Cricketer('Kalam', 37, 68, 95)

# compare player
print(sakib> musfiq)
print(musfiq > kalam)
print(sakib == jack)

players = [sakib,musfiq,kamal,jack,kalam]
oldest = players[0]
 
for player in players:
    if player > oldest:
        oldest = player
print(f'Oldest player: {oldest.name} ({oldest.age})')