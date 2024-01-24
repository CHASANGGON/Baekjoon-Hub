n = int(input())

a = 0
b = 1
if n != 1:
    for _ in range(n-1):
        temp = b
        b = (b + a)%1000000007  
        a = temp
print(b)