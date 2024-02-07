import sys
input = sys.stdin.readline

string = input().rstrip()
bomb = list(input().rstrip())
b_l = len(bomb)

stack = []
for s in string:
    if len(stack) == 0:
        stack.append(s)
    else:
        stack.append(s)
    if stack[-b_l:] == bomb:
        for _ in range(b_l):
            stack.pop()

if len(stack) == 0:
    stack = 'FRULA'
    print(stack)
else:
    print(*stack,sep='')