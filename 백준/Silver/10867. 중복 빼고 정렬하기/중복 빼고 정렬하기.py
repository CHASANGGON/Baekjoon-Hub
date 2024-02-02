import sys
n = int(input())
lst = []


lst = list(map(int,sys.stdin.readline().split()))

lst = list(set(lst))

lst.sort()

print(*lst)