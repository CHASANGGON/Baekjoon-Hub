N, M = map(int, input().split())
basket = list(range(1,N+1))

for _ in range(M):
    i, j = map(int, input().split())
    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp

for i in range(N):
    print(basket[i], end =' ')