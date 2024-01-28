n = int(input())
if n >= 10:
    n_len = len(str(n))
    if len(str(n-9*(n_len-1))) !=  n_len:
        n_len -= 1
    num = n - 9*n_len
    
    check = 0    
    for i in range(9*n_len):
        sum = num + i
        for s in str(sum):
            sum += int(s)
        if sum == n:
            check = 1
            break

    if check:
        print(num+i)
    else:
        print(0)
else:
    if n % 2 == 0:
        print(n//2)
    else:
        print(0)