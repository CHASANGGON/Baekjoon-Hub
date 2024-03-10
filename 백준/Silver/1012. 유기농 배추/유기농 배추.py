def in_range(ni,nj):
    return 0 <= ni < N and 0 <= nj < M

def dfs():    
    while stack:
        i, j = stack.pop()
        arr[i][j] = 0 # 방문 표시
        
        for k in range(4): # 델타 탐색
            
            ni = i + di[k] # 새로운 좌표
            nj = j + dj[k]
            
            if in_range(ni,nj) and arr[ni][nj]: # 인덱스 검사 및 배추(1) 검사
                stack.append([ni,nj])
    
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(1,t+1):
    M, N, K = map(int,input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        j, i = map(int,input().split())
        arr[i][j] = 1
    
    
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                cnt += 1
                stack = [[i,j]]
                dfs()
    
    print(cnt)