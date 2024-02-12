import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    string = input().rstrip()

    sum = 0
    cnt = 0
    for s in string:
        if s == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)