import sys
sys.stdin = open('input_1890.txt','r')


N = int(input())

grid = []
for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)
# print("grid", grid)

#
dp = [[-1]*N for  _ in range(N)]

def dfs(x,y):
    # print(f"dfs{x,y}")
    if x >= N or y>=N:
        return 0 #바깥으로 벗어나면 0
    if (x, y) == (N-1, N-1):
        return 1
    if dp[x][y] !=-1:
        return dp[x][y]
    
    dp[x][y] =0 #방문처리
    # 계산
    dp[x][y] = dfs(x + grid[x][y], y) + dfs(x, y+ grid[x][y])
    return dp[x][y]

print(dfs(0,0))