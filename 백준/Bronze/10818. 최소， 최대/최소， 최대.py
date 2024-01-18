import sys

N= int(input())
numList = list(map(int, sys.stdin.readline().split()))

min = max = numList[0]
for i in range(N):
    if numList[i] < min:
        min = numList[i]
    if numList[i] > max:
        max = numList[i]
print(min, max)