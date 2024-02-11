import sys
input = sys.stdin.readline

n = int(input())
stack = [0]*1000000
top = -1

for _ in range(n):    
    
    command = input().rstrip()
    
    if command[0] == '1': # push
        c, x = map(int,command.split())
        top += 1
        stack[top] = x
    
    elif command == '2': # pop
        if top >= 0:
            print(stack[top])
            top -= 1
        else:
            print(-1)
    
    elif command == '3': # len
        print(top+1)
    
    elif command == '4': # is_empry
        if top == -1:
            print(1)
        else:
            print(0)
    
    elif command == '5': # top
        if top == -1:
            print(-1)
        else:
            print(stack[top])