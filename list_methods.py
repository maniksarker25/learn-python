numbers = [12,32,34]
# push on last index
numbers.append(55)
# push element on specific position
numbers.insert(2,44)
print(numbers)
if 32 in numbers:
     numbers.remove(32)
if 77 in numbers:
     numbers.remove(77)
print(numbers)

last = numbers.pop()
print(last)
print(numbers) 

sorted = numbers.sort()
print(numbers)