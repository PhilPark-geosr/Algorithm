import sys
sys.stdin  = open('input_12911.txt', 'r')
sys.setrecursionlimit(10**9)
N, K = map(int, input().split())

dp = [[-1]*(K+1) for _ in range(N+1)]


def dfs(n, i):
    if n ==1:
        return 1
    if dp[n][i] !=-1:
        return dp[n][i]
    # 경우의 수 계산
    dp[n][i] =0
    for j in range(1, i+1):
        dp[n][i] += dfs(n-1, j)

    for j in range(i+1, K+1):
        if j%i != 0:
            dp[n][i] += dfs(n-1, j)
    dp[n][i] %= 1000000007
    return dp[n][i]


    



answer = 0
for i in range(1, K+1):
    answer += dfs(N, i)

print(answer)

