def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

import sys
input = sys.stdin.readline

n = int(input())

trees = []
for i in range(n):
    trees.append(int(input()))
trees.sort()

trees_interval = [0]*(n-1)
for i in range(n-1):
    trees_interval[i] = trees[i+1] - trees[i]

for i in range(1,n-1):
    if trees_interval[0] > trees_interval[i]:
        trees_interval[0] = gcd(trees_interval[0],trees_interval[i])
    else:
        trees_interval[0] = gcd(trees_interval[i],trees_interval[0])

print((trees[-1]-trees[0])//trees_interval[0] - n + 1)
