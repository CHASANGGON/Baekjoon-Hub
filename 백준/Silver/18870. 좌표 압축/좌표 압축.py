import sys
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

nums_set = list(set(nums)) # 본인보다 작은 수의 종류만 따지니까 set
nums_set.sort() # 오름차순 정렬

nums_ord = range(len(nums_set)) # 압축된 좌표를 나타내는 리스트 

dic = {}
for i in range(len(nums_set)):
    dic[nums_set[i]] = nums_ord[i]

for num in nums:
    print(dic[num],end=' ')