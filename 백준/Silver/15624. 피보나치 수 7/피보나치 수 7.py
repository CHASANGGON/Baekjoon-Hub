n = int(input())

dp = [0,1]
for i in range(1,n):
    dp.append((dp[i-1]+dp[i])%1000000007)
print(dp[n])