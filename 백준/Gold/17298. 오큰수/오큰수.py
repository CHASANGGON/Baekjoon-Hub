import sys
input = sys.stdin.readline

N = int(input().rstrip())
series = list(map(int,input().split()))
    
stack = [series[-1]]
nge_rvs = [-1]

for i in range(N-2,-1,-1):
    if stack[-1] > series[i]:
        nge_rvs.append(stack[-1]) # 이거 먼저
        stack.append(series[i])
    else:
        while len(stack) != 0 and stack[-1] <= series[i]:
            stack.pop()
        if len(stack) == 0:
            nge_rvs.append(-1)
        else:
            nge_rvs.append(stack[-1])
        stack.append(series[i])
nge_rvs = nge_rvs[::-1]

print(*nge_rvs)