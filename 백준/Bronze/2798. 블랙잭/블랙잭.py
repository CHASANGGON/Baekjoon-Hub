import sys
n, m = map(int,input().split())
nums = list(map(int,sys.stdin.readline().split()))
max_sum = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            s = nums[i] + nums[j] + nums[k]
            if max_sum < s and s <= m:
                max_sum = s
print(max_sum)