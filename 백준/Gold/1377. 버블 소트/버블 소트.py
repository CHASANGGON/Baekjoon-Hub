# 1377번 버블 소트
# 몇 번 만에 정렬이 완료되는지 출력
import sys
input = sys.stdin.readline

n = int(input())
nums = [0]*n
for i in range(n):
    nums[i] = (int(input()),i) # 입력값과 인덱스를 함께 저장

sorted_nums = sorted(nums)

idx_difference = [0]*n
for i in range(n):
    idx_difference[i] = sorted_nums[i][1] - nums[i][1]

print(max(idx_difference)+1)