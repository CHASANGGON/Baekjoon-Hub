import sys
input = sys.stdin.readline

n = int(input())

queue = [0]*2000000
front, end = 0,-1

for _ in range(n):

    command = input().rstrip()

    if command == 'pop':
        if front <= end:
            print(queue[front])
            front += 1
        else:
            print(-1)
    
    elif command == 'size':
        print(end-front+1)

    elif command == 'empty':
        if front > end:
            print(1)
        else:
            print(0)
    
    elif command == 'front':
        if front <= end:
            print(queue[front])
        else:
            print(-1)
    elif command == 'back':
        if front <= end:
            print(queue[end])
        else:
            print(-1)
    else:
        c, x = command.split()
        end += 1
        queue[end] = x