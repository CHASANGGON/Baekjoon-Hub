import sys
input = sys.stdin.readline

string = input().rstrip()

cnt = 0
before = string[0]
for s in string[1:]:
    if before == s:
        pass
    else:
        cnt += 1
    before = s

if cnt % 2 == 0:
    print(cnt//2)
else:
    print(cnt//2+1)