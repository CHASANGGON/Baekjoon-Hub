from collections import deque
import sys

input = sys.stdin.readline
dq_l, dq_r = deque(list(input().strip())), deque() # dq_l   dq_r 
n = int(input())                                   #    L ↑ D
                                                   #    cursor         
for _ in range(n):
    cmd = input().rstrip().split()
    
    if cmd[0] == 'L':
        if dq_l:
            dq_r.appendleft(dq_l.pop())
    elif cmd[0] == 'D':
        if dq_r:
            dq_l.append(dq_r.popleft())
    elif cmd[0] == 'B':
        if dq_l:
            dq_l.pop()
    else:
        dq_l.append(cmd[-1])

print(*dq_l,sep='',end='')
print(*dq_r,sep='')