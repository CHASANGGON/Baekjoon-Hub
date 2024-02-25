import sys
input = sys.stdin.readline

n, p = map(int,input().split())
stack = [[] for _ in range(n+1)]


cnt = 0
for _ in range(n):
    a, b = map(int,input().split())

    if stack[a] and stack[a][-1] < b:
        stack[a].append(b)
        cnt += 1
    
    elif stack[a] and stack[a][-1] > b:
        while stack[a] and stack[a][-1] > b:
            stack[a].pop()
            cnt += 1
        if stack[a] and stack[a][-1] < b:
            stack[a].append(b)
            cnt += 1
        elif not stack[a]:
            stack[a].append(b)
            cnt += 1
            
    elif not stack[a]:
        stack[a].append(b)
        cnt += 1

print(cnt)