import sys
input = sys.stdin.readline
n, m = map(int,input().split())

l1 = list(map(int,input().split()))
l1 += list(map(int,input().split()))

print(2*len(set(l1))-n-m)