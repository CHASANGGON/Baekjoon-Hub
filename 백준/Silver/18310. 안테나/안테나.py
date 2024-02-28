def calc(num):
    s = 0
    for a in arr:
        s += abs(num-a)
    return s

import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))
arr.sort()

if n % 2 == 0:
    if arr[n//2] == arr[n//2-1]:
        print(arr[n//2])
    else:
        if calc(arr[n//2]) < calc(arr[n//2-1]):
            print(arr[n//2])
        else:
            print(arr[n//2-1])
else:
    print(arr[n//2])