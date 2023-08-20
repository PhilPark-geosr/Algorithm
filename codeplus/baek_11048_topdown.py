import sys
sys.setrecursionlimit(10**9)

sys.stdin = open('input_11048.txt', 'r')

N, M = map(int, input().split())
grid = []
for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)

# print('grid', grid)

# dp
#dp[i][j] = max(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + grid[i-1][j-1]
dp = [[-1]*(M+1) for _ in range(N+1)]

def dfs(i, j):
    # print(f"dfs{i,j}")
    if i ==0 or j ==0:
        return 0
    if dp[i][j] !=-1:
        return dp[i][j]
    
    dp[i][j] = 0
    dp[i][j] = max(dfs(i-1, j), dfs(i, j-1), dfs(i-1, j-1)) + grid[i-1][j-1]

    return dp[i][j]


print(dfs(N, M))