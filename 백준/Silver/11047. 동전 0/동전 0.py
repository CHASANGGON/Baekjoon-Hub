import sys
input = sys.stdin.readline

n, k = map(int,input().split())

coins = [int(input()) for _ in range(n)]

cnt = 0
for coin in coins[::-1]:
    while coin <= k:
        k -= coin
        cnt +=1
    if k == 0:
        print(cnt)
        break