N, M = map(int, input().split())
basket = [0]*N

for _ in range(M):
    i, j, k = map(int, input().split())
    for ii in range(i-1,j):
        basket[ii] = k

for i in range(N):
    print(basket[i], end =' ')