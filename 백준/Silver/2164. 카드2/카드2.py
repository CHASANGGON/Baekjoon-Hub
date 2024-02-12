import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

queue = deque()
for i in range(n):
    queue.append(i+1)

while True:
    if len(queue) == 1:
        break
    queue.popleft() # cut
    queue.append(queue.popleft()) # back

print(*queue)