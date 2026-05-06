# read only ===> you can not set the value , value con not be assigned
# getter ====> get a value of a property through a method, MOst of the time you will get the vlue of a private attribute
# setter ===> set a value of a property through a method , most of the time you will set the value of a private property

class User:
    def __init__(self,name,age,money):
       self._name = name
       self._age = age
       self._money = money
    # getter without any setter is readonly attribute
    @property # by default it's getter 
    def age(self): # now it's a attribute
        return self._age
    @property
    def salary(self):
        return self._money
    
    #setter
    @salary.setter
    def salary(self,value):
        if value < 0:
            return "Salary can not be negative"
        self._money += value

samsu = User("Kopa",21,12000)

# print(samsu.__money)
# print(samsu.age())
print(samsu.age) # now we call like attribute
print(samsu.salary)
samsu.salary = 4500
print(samsu.salary)