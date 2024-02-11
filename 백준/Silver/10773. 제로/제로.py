import sys
input = sys.stdin.readline

k = int(input())
stack = [0]*100000
top = -1

for _ in range(k):    
    
    n = int(input())
    
    if n == 0:
        if top == -1:
            pass
        else:
            top -= 1
    else:
        top += 1
        stack[top] = n
    
sum = 0
for i in range(top+1):
    sum += stack[i]

print(sum)