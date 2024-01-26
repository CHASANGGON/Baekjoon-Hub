count = int(input())
nums = list(map(int, input().split()))
for num in nums:
    for n in range(2,num//2 + 1):
        if num % n == 0:
            count -= 1
            break
if 1 in nums:
    count -= 1
print(count)