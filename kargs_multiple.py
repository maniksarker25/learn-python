def full_name(first,last):
     name = f'${first} ${last}'
     return name

# take parametter in order
# name = full_name ("Manik","Sarker")
#take parameter without order
name = full_name(last="Sarker",first="Manik")
print(name)


#
def famous_name(first,last,**addition):
     name = f'${first} ${last}'
     print(addition)
    #  print(addition['title'])
     for key,value in addition.items():
          print(key,value)
     return name

name = famous_name(first="Arno",last="Tomalika",title="Talukdar",addition="Anuza")
print(name)


# return multiple 

def a_lot(num1,num2):
     sum = num1+num2
     multi = num1 * num2
     return sum,multi
    #  return [sum,multi]

everything = a_lot(55,21)
print(everything)