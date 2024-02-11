import sys
input = sys.stdin.readline

n = int(input())
i, cnt = 1, 0
while i**2 <= n:
    cnt += 1
    i += 1
print(cnt)