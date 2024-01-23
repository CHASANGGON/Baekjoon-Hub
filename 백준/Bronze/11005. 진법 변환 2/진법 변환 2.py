n, b = map(int, input().split())
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lst = []

while n:
    lst.append(n%b)
    n //= b

for n in lst[::-1]:
    print(num[n],end='')