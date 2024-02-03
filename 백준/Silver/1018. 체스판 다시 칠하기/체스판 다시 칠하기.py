import sys
N,M = map(int,sys.stdin.readline().split())

board = [sys.stdin.readline().rstrip() for _ in range(N)]


# like 파리채
BW = []
for i in range(8):
    if i % 2 == 0:
        BW.append('BWBWBWBW')
    else:
        BW.append('WBWBWBWB')
    
WB = []
for i in range(8):
    if i % 2 == 1:
        WB.append('BWBWBWBW')
    else:
        WB.append('WBWBWBWB')

WB_cnt = 0
BW_cnt = 0
min_cnt = 64
for a in range(N-8+1):
    for b in range(M-8+1):
        WB_cnt = 0
        BW_cnt = 0
        for i in range(8):
            for j in range(8):
                if board[a+i][b+j] != WB[i][j]:
                    WB_cnt += 1
                if board[a+i][b+j] != BW[i][j]:
                    BW_cnt += 1
        min_cnt = min(min_cnt, WB_cnt, BW_cnt)

print(min_cnt)