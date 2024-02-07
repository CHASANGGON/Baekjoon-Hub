def prime_list(m,n):
    sieve = [True]*(n+1)

    nn = int(n**0.5)
    for i in range(2,nn+1): 
        if sieve[i] == True:
            for j in range(i+i,n+1,i):
                sieve[j] = False
    if m == 1:
        m = 2
    return [ i for i in range(m,n+1) if sieve[i] == True]
    

import sys
input = sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break
    print(len(prime_list(n+1,n+n)))