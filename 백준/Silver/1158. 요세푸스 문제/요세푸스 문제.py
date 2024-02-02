import sys
N, K = map(int,sys.stdin.readline().split())
lst = list(range(1,N+1))
lst_zero = [0] * N
lst_pop = []
count = 0
i = 0
N_copy = N
while N_copy:
    if lst[i] != 0:
        i += 1
        count += 1
    else:
        lst[i] == 0
        i += 1
    i %= N

    if count == K:
        lst_pop += [lst[i-1]]
        lst[i-1] = 0
        count = 0
        N_copy -= 1
    
print('<',end='')
print(*lst_pop,sep=', ',end='')
print('>')