lst = sorted(map(int,input().split()))
print(lst[0]+lst[1]+min(lst[2],lst[0]+lst[1]-1))