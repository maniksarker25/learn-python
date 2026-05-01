# list, array , collection is same (simple terms)
 # index   0   1  2  3  4  5  6   7  8 9  10
numbers = [23,453,64,64,66,73,747,86,8,57,50]
 # rev ind -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1  

print(numbers[3])
print(numbers[-3])

#list(start:end)

print(numbers[2:6]) #[64, 64, 66, 73]

# list(start:end : step)
print(numbers[1:7:2]) #[453, 64, 73]

print(numbers[7:2:-1]) #[86, 747, 73, 66, 64]
print(numbers[4:]) #[66, 73, 747, 86, 8, 57, 50]
print(numbers[:5])#[23, 453, 64, 64, 66]
print(numbers[:])#[23, 453, 64, 64, 66, 73, 747, 86, 8, 57, 50]
print(numbers[::-1])#[50, 57, 8, 86, 747, 73, 66, 64, 64, 453, 23] short cut to reverse

# here we just get value but not get index
for num in numbers:
    print(num)


# with index
for i,num in enumerate(numbers):
    print(i,num)