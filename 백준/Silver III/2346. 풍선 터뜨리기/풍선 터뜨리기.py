from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dq = deque(enumerate(map(int,input().split()),1))

result = []
# rotate 함수 - deque를 n만큼 회전
for _ in range(n):
    a = dq.popleft()
    result.append(a[0])
    if a[1] > 0:
        dq.rotate(-a[1]+1)
    elif a[1] < 0:
        dq.rotate(-a[1])
for i in range(n):
    print(result[i],end=' ')