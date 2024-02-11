def prime_list(n):
    m = int(n**0.5)
    sieve = [1]*(n+1)

    for i in range(2,m+1):
        if sieve[i] == 1:
            for j in range(i+i,n+1,i):
                sieve[j] = 0
    return sieve

import sys
input = sys.stdin.readline

t = int(input())
lst = prime_list(1000000)

for _ in range(t):
    n = int(input())
    
    cnt = 0
    for i in range(2,n//2 + 1): # n//2 까지 진행, 중복 방지
        if lst[i] and lst[n - i]: # i가 소수고, n - i 또한 소수 일 때
            cnt += 1
        i += 1
    print(cnt)