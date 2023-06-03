import sys
sys.stdin = open('input_1520.txt', 'r')

n, m = map(int, input().split())

grid = []
for _ in range(n):
    line = list(map(int, input().split()))
    grid.append(line)

# dfs 구현
dx = [1,  -1, 0, 0]
dy = [0,  0,  1, -1]

# visited = [[0]*m for _ in range(n)]
# global min_result
# def dfs(i, j, cost):
#     print(f"dfs{i, j, cost}")
#     global min_result
#     if i == n-1 and j == m-1:
#         if cost < min_result:
#             min_result = cost
#     else:
#         for k in range(4):
#             new_x, new_y = i + dx[k], j + dy[k]
#             if 0<= new_x< n and 0<=new_y< m and visited[new_x][new_y] ==0 and grid[new_x][new_y]< grid[i][j]:
#                 visited[new_x][new_y] =1
#                 dfs(new_x, new_y, cost + grid[new_x][new_y])
#                 visited[new_x][new_y] =0

# min_result = 1e9
# visited[0][0] =1
# # print(grid[0][0])
# dfs(0,0, grid[0][0])
# print(min_result)


visited2 = [[0]*m for _ in range(n)]
result = set()
global cnt
def dfs2(i, j, cost):
    # print(f"dfs{i, j,  cost,path}")
    global cnt
    if i == n-1 and j == m-1:
        cnt = cnt +1
    else:
        for k in range(4):
            new_x, new_y = i + dx[k], j + dy[k]
            if 0<= new_x< n and 0<=new_y< m and visited2[new_x][new_y] ==0 and grid[new_x][new_y]< grid[i][j]:
                visited2[new_x][new_y] =1
                dfs2(new_x, new_y, cost + grid[new_x][new_y])
                visited2[new_x][new_y] =0

cnt = 0
visited2[0][0] =1
dfs2(0,0, grid[0][0])
print(cnt)

# print(50+35+30+27+24+22+15+10)