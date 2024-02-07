def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    n = int(input())
    if n == 0:
        n = 2
    if n == 1:
        n = 2
    else:
        while not is_prime(n):
            n += 1
    
    print(n)