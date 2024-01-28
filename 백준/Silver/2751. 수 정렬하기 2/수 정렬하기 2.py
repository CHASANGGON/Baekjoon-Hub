import sys
n = int(sys.stdin.readline())
arr = [0] * 20000001 # index를 조정 (-1,000,001)
for _ in range(n):
    arr[int(sys.stdin.readline())+1000000] += 1
for i in range(2000001):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i-1000000)