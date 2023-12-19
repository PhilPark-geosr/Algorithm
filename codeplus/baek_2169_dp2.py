import sys
sys.setrecursionlimit(10**9)

sys.stdin =open('input_2169.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [[0]*(M+1)]
for _ in range(N):
    line = [0] + list(map(int, input().split()))
    grid.append(line)
# print(grid)
dp = [[[-float('inf')]*(3) for _ in range(M+1)] for _ in range(N+1)]


dp[1][1][0], dp[1][1][1], dp[1][1][2] = grid[1][1],grid[1][1],grid[1][1]
for i in range(1, N+1):
    for j in range(1, M+1):
        if i-1>0:
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1], dp[i-1][j][2]) + grid[i][j]
        if j-1 >0:
            dp[i][j][1] = max(dp[i][j-1][0],dp[i][j-1][1]) + grid[i][j]
    for j in range(M-1, 0, -1):
        dp[i][j][2] = max(dp[i][j+1][0],dp[i][j+1][2]) + grid[i][j]

# print(dp[2][2][2])
                
print(max(dp[N][M][0], dp[N][M][1]))