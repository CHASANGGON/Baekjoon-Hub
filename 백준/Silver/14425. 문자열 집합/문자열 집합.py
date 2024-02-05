import sys
n, m = map(int,sys.stdin.readline().split())

nn, mm = {}, []
for _ in range(n):
    nn[sys.stdin.readline()] = 0

cnt = 0
for _ in range(m):
    if sys.stdin.readline() in nn:
        cnt += 1

print(cnt)