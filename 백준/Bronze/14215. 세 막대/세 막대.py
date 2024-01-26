lst=list(map(int,input().split()))
lst_set=set(lst)
if len(lst_set) == 1:
    print(lst[0]*3)
else:
    lst.sort()
    dif = lst[2] - lst[0] - lst[1]
    if dif >= 0:
        lst[2] = lst[2] - dif - 1 
    print(lst[0]+lst[1]+lst[2])