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
dp = [[0]*(M+1) for _ in range(N+1)]
dp[1][1] = grid[0][0] 
for i in range(1, N+1):
    for j in range(1, M+1):

        if i+1 <=N and j+1<=M:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+  grid[i][j]) 
        if i+1 <=N:
            dp[i+1][j] =   max(dp[i+1][j], dp[i][j]+ grid[i][j-1]) 
        if j+1 <=M:
            dp[i][j+1] =   max(dp[i][j+1], dp[i][j]+ grid[i-1][j]) 

        


print(dp[N][M])