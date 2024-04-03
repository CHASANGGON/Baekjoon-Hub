def bfs(now):
    dq = deque()
    dq.append(now)
    visited[now] = 0
    
    while dq:
        now = dq.popleft()
        if now == k: # 도착
            print(visited[now])
            return

        # 순서가 중요
        # 인덱스 검사 및 방문 체크
        if now * 2 <= 100000 and visited[now*2] == -1:
            visited[now * 2] = visited[now]
            dq.append(now * 2)
        # 인덱스 검사 및 방문 체크
        if now - 1 >= 0 and visited[now-1] == -1:
            visited[now - 1] = visited[now] + 1
            dq.append(now - 1)
        # 인덱스 검사 및 방문 체크
        if now + 1 <= 100000 and visited[now+1] == -1:
            visited[now + 1] = visited[now] + 1
            dq.append(now + 1)
            

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

visited = [-1] * 100001
bfs(n)