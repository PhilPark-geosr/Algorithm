import sys
sys.setrecursionlimit(10**9)

sys.stdin = open('input_12996.txt', 'r')

S, a, b, c= map(int, input().split())
dp = [[[[-1]*(S+1) for _ in range(c+1)] for _ in range(b+1)] for _ in range(a+1)]

def dfs(i,j,k,N):
    # print(f"dfs{i,j,k,N}")
    if i <0 or j< 0 or k <0 or N <0:
        return 0
    if i ==0 and j== 0 and k==0 and N==0: #dp[0][0][0][0] =1
        return 1
    if dp[i][j][k][N] !=-1:
        return dp[i][j][k][N]
    
    dp[i][j][k][N] = dfs(i-1, j, k, N-1) + dfs(i-1, j-1, k, N-1) +dfs(i-1, j, k-1, N-1) +\
    dfs(i-1, j-1, k-1, N-1) +dfs(i, j-1, k, N-1) +dfs(i, j-1, k-1, N-1) +dfs(i, j, k-1, N-1)
    dp[i][j][k][N] %= 1000000007
    return dp[i][j][k][N]

  
    


print(dfs(a,b,c,S))

