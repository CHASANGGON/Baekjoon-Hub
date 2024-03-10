def dfs(now_node):
    visited[now_node] = 0 # 방문 체크
    
    for next_node in edge[now_node]:
        if visited[next_node]: # 아직 방문하지 않았다면(1)
            dfs(next_node) # 방문

import sys
input = sys.stdin.readline

n = int(input()) # 컴퓨터의 개수

edge = [[] for _ in range(n+1)] # 컴퓨터의 간선 정보
visited = [1]*(n+1) # 1로 초기화

m = int(input()) # 간선의 개수

for _ in range(m):
    s, e = map(int,input().split())
    edge[s].append(e)
    edge[e].append(s)

dfs(1)
print(visited.count(0)-1) # 방문한 노드는 0 - 1(1번 컴퓨터)