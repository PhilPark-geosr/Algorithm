import sys
sys.stdin = open('input_1937.txt', 'r')
sys.setrecursionlimit(10 ** 9)
# input
n = int(input())
grid = []
for _ in range(n):
    line = list(map(int, input().split()))
    grid.append(line)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
# dp 정의
# dp[i][j] # i, j에서 출발해서 방문할 수 있는 최대칸수
dp = [[-1]*n for _ in range(n)]
# dfs 정의
def dfs(i, j, prev):
    if dp[i][j] ==-1 : #방문하지 않는 것들에 한해서만 처리
        dp[i][j] = 0
        for k in range(4):
            new_x, new_y = i + dx[k], j +dy[k]
            if 0<=new_x<n and 0<=new_y<n:
                if grid[new_x][new_y] > prev:
                    dp[i][j] = max(dp[i][j],dfs(new_x, new_y, grid[new_x][new_y])+1)

    # 방문한 애들에 대해서는 
    return dp[i][j]
# test
# dfs(2,2, grid[2][2])
# print(dp)

# 모든 노드에 대해 dfs수행
for i in range(n):
    for j in range(n):
        dfs(i,j, grid[i][j])

# print(dp)

# #정답
answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dp[i][j])

print(answer+1)