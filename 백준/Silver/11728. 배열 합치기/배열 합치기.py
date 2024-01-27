input()
n = list(map(int,input().split()))
n += list(map(int,input().split()))
n.sort()
for m in n:
    print(m,end=' ')