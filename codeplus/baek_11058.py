import sys
sys.stdin = open('input_11058.txt', 'r')

N = int(input())

dp = [0]*(N+1)
# dp[N] : N번눌렀을때 최대 A의 갯수
for i in range(1, N+1):
    if i<=3:
        dp[i] = i
    else:
        for j in range(3, i+1):
            dp[i] = max(dp[i], dp[i-j]*(j-1))
        dp[i] = max(dp[i-1]+1, dp[i])

print(dp[N])