
import sys
lst = []
n = int(input())
for _ in range(n):
    lst.append(tuple(map(int, sys.stdin.readline().split())))
lst.sort()

before = 0
count = 0
for l in lst:
    # print(l)
    if l[0] > before:
        # print(f'l[0] : {l[0]} > before : {before}')
        # print('count +1')
        count += 1
    before = l[0] + l[1]

print(count)
