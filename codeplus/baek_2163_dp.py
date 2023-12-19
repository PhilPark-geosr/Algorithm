import sys
sys.setrecursionlimit(10**9)
#sys.stdin = open('input_2163.txt', 'r')

N, M = map(int, input().split())
# print(N, M)
dp = [[-1]*(M+1) for _ in range(N+1)]

def dfs(i, j):
    # print(f"dfs{i,j}")
    
    if (i, j) == (1,1):
        return 0
    if i ==1:
        return j-1
    if j ==1:
        return i-1
    if dp[i][j] != -1:
        return dp[i][j]
    

    dp[i][j] = float('inf')
    for k in range(1, i):
        dp[i][j] = min(dp[i][j], dfs(k,j) + dfs(i-k,j) +1)

    for k in range(1, j):
        dp[i][j] = min(dp[i][j], dfs(i,k) + dfs(i,j-k) +1)

    dp[j][i] = dp[i][j]
    return dp[i][j]

print(dfs(N, M))