import sys
input = sys.stdin.readline

while True:
    nums = input().rstrip()

    if nums == '0':
        break
    
    if nums == nums[::-1]:
        print('yes')
    else:
        print('no')