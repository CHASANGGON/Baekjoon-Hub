import sys

N, X = map(int, input().split())
numList = list(map(int, sys.stdin.readline().split()))

count = 0
for i in range(N):
    if numList[i] < X:
        print(numList[i], end = ' ')