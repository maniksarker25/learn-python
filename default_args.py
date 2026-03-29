def sum(num1,num2,num3=0,num4=0):
    result = num1 + num2+num3+num4
    return result

total = sum(12,12,12)
print("Total:",total)

# args 
def all_sum(*numbers):
    print(numbers)
    for num in numbers:
        print(num)


result = all_sum(45,50,60)
print("All sum",result)