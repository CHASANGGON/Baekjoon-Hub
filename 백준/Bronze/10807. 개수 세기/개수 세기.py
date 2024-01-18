import sys

N = int(input())
numList = list(map(int, sys.stdin.readline().split()))
v = int(input())

count = 0
for i in range(N):
    if numList[i] == v:
        count += 1

print(count)