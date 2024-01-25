while 1:
    n = int(input())
    if n == -1: break
    lst=[]
    for i in range(1,n):
        rem = n % i
        if rem == 0:
            lst.append(i)
    if sum(lst) == n:
        print(f'{n} = ', end='')
        print(*lst, sep=' + ')
    else:
        print(f'{n} is NOT perfect.')