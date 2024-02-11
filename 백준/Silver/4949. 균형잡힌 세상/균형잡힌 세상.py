import sys
input = sys.stdin.readline

l_parenthesis = ['[', '(']


while True:
    stack = []
    string = input().rstrip()

    if string == '.':
        break
    else:
        for s in string:
            if s in l_parenthesis:
                stack.append(s)
            
            elif s == ']' and len(stack) != 0 and stack[-1] == '[':
                stack.pop()

            elif s == ')' and len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            elif s == ')' or s == ']':
                stack.append(s)

    if stack:
        print('no')
    else:
        print('yes')