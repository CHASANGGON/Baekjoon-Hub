def dfs(now):
    team.append(now) # 팀 리스트에 추가
    
    visited[now] = 0 # 방문 체크
    
    nxt = graph[now] # nxt 변수 갱신
    
    if visited[nxt]: 
        return dfs(nxt)
    if nxt in team:
        return len(team[team.index(nxt):])
    return 0

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    graph = [0] + list(map(int, input().split())) 
    visited = [1] * (n+1)
    
    for i in range(1,n+1):
        if visited[i]:
            team = []
            n -= dfs(i)
    
    print(n)