from collections import deque
import sys
input = sys.stdin.readline

# 0은 큐, 1은 스택

n = int(input())
q_s = list(map(int,input().split()))
in_lst = list(map(int,input().split()))
input()
push_lst = list(map(int,input().split()))

qs = deque()
for i in range(n):
    if q_s[i] == 0:
        qs.append(in_lst[i])

result = []
for p in push_lst:
    qs.appendleft(p)
    result.append(int(qs.pop()))

print(*result)