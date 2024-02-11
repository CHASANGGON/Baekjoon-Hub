import sys
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
nums_set = list(set(nums))
nums_set.sort()
nums_accu_sum = range(len(nums_set))

dic = {}
for i in range(len(nums_set)):
    dic[nums_set[i]] = nums_accu_sum[i]

for num in nums:
    print(dic[num],end=' ')