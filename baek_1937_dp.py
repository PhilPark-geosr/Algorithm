import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input_1937.txt', 'r')
input = sys.stdin.readline

N = int(input())
grid = []
for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)

dp = [[-1]*N for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(i,j):
    if dp[i][j] !=-1:
        return dp[i][j]
    
    dp[i][j] = 1
    for k in range(4):
        new_x, new_y = i + dx[k], j + dy[k]
        if 0<=new_x<N and 0<=new_y<N and grid[new_x][new_y] > grid[i][j]:
            dp[i][j] = max(dp[i][j], dfs(new_x, new_y)+1)

    return dp[i][j]
    


# 정답
answer = 0
for i in range(N):
    for j in range(N):
        answer = max(answer, dfs(i,j))

print(answer)