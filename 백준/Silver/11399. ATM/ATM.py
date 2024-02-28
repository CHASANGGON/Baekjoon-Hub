import sys
input = sys.stdin.readline

n = int(input())

people = list(map(int,input().split()))

people.sort()

s = 0
for i in range(1,n+1):
    s += sum(people[:i])

print(s)