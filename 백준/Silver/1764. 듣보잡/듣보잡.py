import sys
input = sys.stdin.readline
n, m = map(int,input().split())

dic = {}
for i in range(n):
    dic[input().rstrip()] = ''

hl = []
cnt = 0
for i in range(m):
    h = input().rstrip()
    if h in dic:
        hl += [h]
        cnt += 1
hl.sort()
print(cnt)
for i in range(cnt):
    print(hl[i])