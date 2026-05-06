n = input().strip()
reversed_n = n[::-1].lstrip('0')
if reversed_n == "":
    reversed_n = "0"

print(reversed_n)

if n == n[::-1]:
    print("YES")
else:
    print("NO")