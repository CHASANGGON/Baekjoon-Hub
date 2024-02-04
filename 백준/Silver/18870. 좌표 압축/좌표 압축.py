import sys
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
nums_set = list(set(nums))
nums_set.sort()
length = len(nums_set)
nums_accu_sum = [0] + [1]*(length-1)

for i in range(length-1):
    nums_accu_sum[i+1] += nums_accu_sum[i]

dic = {}
for i in range(length):
    dic[nums_set[i]] = nums_accu_sum[i]

for num in nums:
    print(dic[num],end=' ')