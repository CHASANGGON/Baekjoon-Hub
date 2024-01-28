n = int(input())
arr = [0] * 10000
for _ in range(n):
    arr[int(input())-1] += 1
for i in range(10000):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i+1)