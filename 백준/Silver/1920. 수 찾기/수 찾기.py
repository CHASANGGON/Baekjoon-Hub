import sys
input()
lst_n = list(set(map(int,sys.stdin.readline().split())))
m = int(input())
n = len(lst_n)
lst_n.sort()

lst_m = list(map(int,sys.stdin.readline().split()))

for m in lst_m:
    if m in lst_n:
        print(1)
    else:
        print(0)