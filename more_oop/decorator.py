import math
# def timer(func):
#     def inner():
#         print("time started")
#         # print(func)
#         print(func())
#         print("time ended")
#     return inner


def timer(func):
    def inner(*args,**kwargs):
        print("time started")
        # print(func)
        print(func(*args,**kwargs))
        print("time ended")
    return inner


# timer()()


# @timer # easiar way
# def get_fectorial(n):
#     print("Fectorial starting...")
# vejailla way to decorate
# timer(get_fectorial)()

@timer # easiar way
def get_fectorial(n):
    print("Fectorial starting...")
    result = math.factorial(n)
    print(f'Fectorial of {n} is {result}')

get_fectorial(5)
get_fectorial(n = 10)

