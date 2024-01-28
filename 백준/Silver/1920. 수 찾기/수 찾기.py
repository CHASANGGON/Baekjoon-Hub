import sys
input()
lst_n = set(map(int,sys.stdin.readline().split()))
input()
lst_m = list(map(int,sys.stdin.readline().split()))

for m in lst_m:
    if m in lst_n:
        print(1)
    else:
        print(0)