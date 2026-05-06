N = int(input())
A = list(map(int,input()).split())

min_index = 0
max_index = 0

for i in range(1,N):
    if A[i] < A[min_index]:
        min_index = i
    if A[i] > A[max_index]:
        max_index = i


A[min_index], A[max_index] = A[max_index],A[min_index]

print(*A)