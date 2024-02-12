import sys
input = sys.stdin.readline
n, k = map(int,input().split())

queue = []
for i in range(n):
    queue.append(i+1)
l = n
idx = -1
Josephus = []
while queue:
    idx = (idx+k)%l
    Josephus.append(str(queue.pop(idx)))
    l -= 1
    idx -= 1
print('<',', '.join(Josephus), '>',sep='')