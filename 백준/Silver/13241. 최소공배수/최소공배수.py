def common_divisor(a,b):
    if b == 0:
        return a
    else:
        return common_divisor(b,a%b)

import sys
input = sys.stdin.readline

a,b = map(int,input().split())
if b > a:
    a,b = b,a
print((a*b)//common_divisor(a,b))