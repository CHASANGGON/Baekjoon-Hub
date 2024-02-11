# 1377번 버블 소트
# 몇 번 만에 정렬이 완료되는지 출력
import sys
input = sys.stdin.readline

n = int(input())
nums = [0]*n
for i in range(n):
    nums[i] = (int(input()),i) # 입력값과 인덱스를 함께 저장
                               # nums = [(5,0), (10,1), (1,2)~]

sorted_nums = sorted(nums) # 리스트 내부 튜플의 첫 번째 요소를 기준으로 정렬

idx_difference = [0]*n # 인덱스 차이값을 담아줄 리스트
for i in range(n):
    idx_difference[i] = sorted_nums[i][1] - nums[i][1]

print(max(idx_difference)+1)