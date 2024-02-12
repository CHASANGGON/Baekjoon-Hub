import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    lst = list(input().rstrip().split())
    
    for i in range(len(lst)):
        lst[i] = lst[i][::-1]

    for i in range(len(lst)):
        print(''.join(lst[i]),end=' ')
    print()