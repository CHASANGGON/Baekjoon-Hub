import sys
input = sys.stdin.readline


nums = input().rstrip()

# 30의 배수 중에서 가장 큰 수를 찾기
# 30은 3과 10의 곱으로 이루어져 있다
# 10의 배수이려면 끝자리가 0 이기만 하면 된다
# 3의 배수이려면 각 자리수의 합이 3의 배수이면 된다.
# 123 -> o / 124 -> x / 39 -> o / 87 -> o
if '0' not in nums:
    print(-1)
else:
    sum = 0
    for num in nums:
        sum += int(num)
    if sum % 3 != 0:
        print(-1)
    else:
        nums = list(nums)
        nums.sort(reverse=True)
        for num in nums:
            print(int(num),end='')
        print()