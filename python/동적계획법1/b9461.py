from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0,1,1,1,2] + [0] * (n-4)
    for i in range(4,n+1):
        dp[i] = dp[i-3] + dp[i-2]
    print(dp[n])