m = int(input())
n = int(input())
lst = []
if m == 1: m = 2
for num in range(m,n+1):
    prime = 1
    for n in range(2,num//2+1):
        if num % n == 0:
            prime = 0
            break
    if prime: lst.append(num)
if len(lst):
    print(sum(lst), min(lst))
else:
    print(-1)