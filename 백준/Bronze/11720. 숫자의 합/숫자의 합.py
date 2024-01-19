n = int(input())
N = int(input())

sum = 0
for _ in range(n):
    sum += N % 10
    N //= 10
print(sum)