from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

dq = deque()
for _ in range(n):
    c = input().rstrip()
    
    if c[0] == '1':
        cc, x = c.split()
        dq.appendleft(int(x))
    elif c[0] == '2':
        cc, x = c.split()
        dq.append(int(x))
    elif c == '3':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif c == '4':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif c == '5':
        print(len(dq))
    elif c == '6':
        if not dq:
            print(1)
        else:
            print(0)
    elif c == '7':
        if dq:
            print(dq[0])
        else:
            print(-1)
    else:
        if dq:
            print(dq[-1])
        else:
            print(-1)