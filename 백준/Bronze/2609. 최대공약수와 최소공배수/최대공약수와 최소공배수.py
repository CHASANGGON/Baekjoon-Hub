# 최대 공약수 찾기
def GCD(a,b):
    if b == 0:
        return a
    return GCD(b,a%b)

import sys
input = sys.stdin.readline

a, b = map(int,input().split())

if a < b:
    a,b = b,a


gcd = GCD(a,b)
print(gcd)
print(a*b//gcd)