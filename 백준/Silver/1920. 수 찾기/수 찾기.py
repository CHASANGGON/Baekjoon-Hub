input()
lst_n = set(map(int,input().split()))
input()
lst_m = list(map(int,input().split()))

for m in lst_m:
    if m in lst_n:
        print(1)
    else:
        print(0)