import sys
input = sys.stdin.readline

n, m = map(int,input().split())

tk = [0]*n
for i in range(n):
    tk[i] = int(input())
tk.sort()

start, end = tk[0], tk[-1]*m
ans = end
while start <= end:
    thr = 0
    mid = (start+end)//2

    for i in range(n):
        thr += mid // tk[i]
        if thr >= m:
            break

    if thr >= m:
        end = mid -1
        # 예제 입력 1의 경우 mid = 28 이었다가
        # end = mid - 1 = 27-> mid = (start + end)//2 = 27 로 감소시키는 경우
        # 조건을 만족시키지 못 하고, 그 때의 mid 값을 출력(오답)
        # 이런 경우를 위해 ans = min(ans,mid) 로 이전의 mid값을 기억
    
    else:
        start = mid + 1

print(start)