import sys
n = int(input())
lst = []
for _ in range(n):
    command = sys.stdin.readline().rstrip()
    if command[-1] in '1234567890':
        command, num = command.split()
        lst.append(num)
    elif command == 'pop':
        if len(lst):
            print(lst.pop(0))
        else:
            print(-1)
    elif command == 'size':
        print(len(lst))
    elif command == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if len(lst):
            print(lst[0])
        else:
            print(-1)
    elif command == 'back':
        if len(lst):
            print(lst[len(lst)-1])
        else:
            print(-1)
    elif command == 'top':
        if len(lst):
            print(lst[len(lst)-1])
        else:
            print(-1)