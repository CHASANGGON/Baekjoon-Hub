import sys

input = sys.stdin.readline

n = int(input())

dic = {}
for i in range(n):
    k, v = input().rstrip().split()
    dic[k] = v

lst = []
for k in dic.keys():
    if dic[k] == 'enter':
        lst.append(k)


lst.sort(reverse=True)
for l in lst:
    print(l)