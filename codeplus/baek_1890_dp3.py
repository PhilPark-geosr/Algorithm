import sys
sys.stdin = open('input_1890.txt','r')
N = int(input())

grid = []
for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)
# print("grid", grid)

dp = [[0]*N for  _ in range(N)]
dp[0][0] =1
for x in range(N):
    for y in range(N):
        for k in range(x):
            if k + grid[k][y] ==x:
                dp[x][y] += dp[k][y]
        for k in range(y):
            if k + grid[x][k] ==y:
                dp[x][y] += dp[x][k]

print(dp[x][y])