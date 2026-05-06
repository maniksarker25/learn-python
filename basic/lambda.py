# lambda

# def double(x):
#     return x * 2

double = lambda num : num *2
squared = lambda num : num * num
result = double(44)
output = squared(9)
print(result)
print(output)

add = lambda x,y : x + y
print(add(2,3))

# map
numbers = [12,32,55,35,53,646,64,64,64,12]

# doubled_num = map(double,numbers)\
doubled_num = map(lambda x : x * 2,numbers)
squared_num = map(lambda x:x*x,numbers)
print(list(doubled_num))
print(list(squared_num))

#filter
actors = [
    {"name":"sabana","age":65},
    {"name":"sabnur","age":45},
    {"name":"sabila nur","age":35},
    {"name":"srabonti","age":38},
    {"name":"shaon","age":47},
]


juniors = filter(lambda actor : actor['age'] < 40, actors)

print(list(juniors))