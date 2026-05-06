A = int(input())
B = int(input())

def isLucky(n):
    while n > 0:
        digit = n % 10
        if digit != 4 and digit != 7:
            return False
        n //= 10  
    return True

found = False  

for i in range(A, B + 1): 
    if isLucky(i):
        print(i, end=" ")  
        found = True

if not found:
    print(-1)