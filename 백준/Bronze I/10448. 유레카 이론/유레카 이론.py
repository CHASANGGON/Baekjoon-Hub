import sys
input = sys.stdin.readline

# 가우스의 삼각수를 리스트를 통해 주어질 수 있는 수까지 만든 다음
# 가능한지
# 주어지는 수의 최댓값 1000
tri_num = [0]*45
tri_num[0] = 1
for i in range(1,45):
    tri_num[i] = tri_num[i-1] + i + 1

n = int(input())
for _ in range(n):
    n_num = int(input()) # 주어진 자연수
    can_make = False
          
    # 3개의 합으로 구해지는 경우 = 주어진 수 - 삼각수1 - 삼각수2 = 삼각수
    if not can_make:
        for i in range(45):
            for j in range(45):
                if n_num - tri_num[i] - tri_num[j] in tri_num:
                    can_make = True
                    break
                # 두 삼각수를 뺀 값이 음수인 경우 -> 생성 불가 -> 미리 탈출 -> 메모리 절약
                elif n_num - tri_num[i] - tri_num[j] < 1:
                    break
    
    if can_make:
        print(1)
    else:
        print(0)