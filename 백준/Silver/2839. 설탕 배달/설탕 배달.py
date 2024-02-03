import sys
N = int(sys.stdin.readline())
max_quo = N // 5
result = -1
for i in range(max_quo,-1,-1):
    if (N-(i*5))%3 == 0:
        result = i + (N-5*i)//3
        break
print(result)