import sys
input = sys.stdin.readline
a = input().rstrip()

lst = []
for i in range(len(a)): # 0 / 1 / 2 
    for j in range(len(a)-i): # 3개 2개 1개
        lst += [a[j:j+i+1]]
print(len(set(lst)))