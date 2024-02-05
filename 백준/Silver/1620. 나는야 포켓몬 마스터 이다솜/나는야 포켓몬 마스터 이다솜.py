import sys
input = sys.stdin.readline
n, m = map(int,input().split())

lst = []
for i in range(n):
    lst += [input().rstrip()]
for i in range(m):
    problem = input().rstrip()
    if problem[0] in '0123456789':
        print(lst[int(problem)-1])
    else:
        print(lst.index(problem)+1)