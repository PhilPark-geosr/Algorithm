import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input_12872.txt', 'r')

N, M, P = map(int, input().split())


dp = [[-1]*(N+1) for _ in range(P+1)]
# dp[i][j] 길이 i의 수열을 j개로 만들었을때의 경우의 수

def dfs(i, j):
    # print(f"dfs{i,j}")

    if (i,j) ==(0,0):
        return 1
    
    if i ==0:
    
        return 0
    
    if j==0:

        return 0
    
    if dp[i][j] !=-1:
        return dp[i][j]

    dp[i][j] = 0
    if j>M:
        dp[i][j] += dfs(i-1, j)*(j-M)
    dp[i][j] += dfs(i-1, j-1)*(N-(j-1))
    dp[i][j] %= 1000000007 

    return dp[i][j]


print(dfs(P, N))
