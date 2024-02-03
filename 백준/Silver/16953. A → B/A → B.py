# A -> B
import sys

A, B = map(int,sys.stdin.readline().split())
cnt = 0

while A != B:
    if str(B)[-1] == '1':
        B = int(B//10)
        cnt += 1
    else:
        if B % 2 == 1:
            cnt = -2
            break
        B = B//2
        cnt += 1
        if A > B:
            cnt = -2
            break

print(cnt+1)