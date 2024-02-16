from itertools import permutations
import sys
input = sys.stdin.readline

# 순열 생성
permu = list(permutations(['1','2','3','4','5','6','7','8','9'],3))

# 문제의 알고리즘 분류를 보면, 구현 & 브루트포스 이다.
# 이 문제는 머리를 써서 푸는 거라기 보다는
# 가능한 3자리 수를 모두 생성한 후에
# 주어진 수와 생성된 수들을 비교하면서
# 조건에 맞지 않는 수를 지워주면 된다.

n = int(input())

for _ in range(n):
    input_num, strike, ball = map(int,input().split())
    input_num = list(str(input_num))
    pop_cnt  = 0
    
    for i in range(len(permu)): # permutation 전수조사
        i -= pop_cnt
        
        # strike check
        str_cnt = 0
        for j in range(3):
            if str(permu[i][j]) == input_num[j]:
                str_cnt += 1
        
        if str_cnt != strike:
            permu.pop(i)
            pop_cnt += 1
            continue
        
        # ball check
        ball_cnt = 0
        for j in range(3):    
            if input_num[j] in permu[i] and input_num[j] != permu[i][j]:
                ball_cnt += 1
                
        if ball_cnt != ball:
            permu.pop(i)
            pop_cnt += 1
    
print(len(permu))