from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    command = input().strip() # RDD
    n = int(input())
    dq = deque(input().rstrip()[1:-1].split(',')) # [1,2,3,4]
    
    reverse = False
    cnt = len(dq)
    output = ''
    
    for c in command:
        if c == 'D':
            
            if cnt == 0 or n == 0: # 요소가 비었으면 에러
                output = 'error'
                break
            else: # reverse 변수를 통해서 pop left or right 판단
                if reverse == False:
                    dq.popleft()
                else:
                    dq.pop()
                cnt -= 1
        else:
            if reverse == True:
                reverse = False
            else:
                reverse = True
    
    lst = list(dq)
    
    if output == 'error':
        print(output)
    elif reverse == True:
        print("["+",".join(lst[::-1])+"]")
    else:
        print("["+",".join(lst)+"]")