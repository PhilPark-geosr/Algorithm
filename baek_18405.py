import sys
import heapq

sys.stdin = open('input_18405.txt', 'r')

N, K = map(int, input().split())
# make a grid
grid = []
for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)

S, X, Y = map(int, input().split())

#initialize state
q = []
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if grid[i][j] !=0:
            heapq.heappush(q, (0, grid[i][j], i, j)) #(time, virus, i, j)
            visited[i][j] =1
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# do bfs
while q:
    # print(q, grid)
    time, virus, x, y = heapq.heappop(q)
    # print(time, virus)
    if time == S:
        break
    for k in range(4):
        new_x, new_y = x+ dx[k], y + dy[k]
        if 0<=new_x<N and 0<=new_y<N and visited[new_x][new_y] ==0 \
        and grid[new_x][new_y] ==0:
            visited[new_x][new_y] =1
            grid[new_x][new_y] =virus
            heapq.heappush(q, (time+1, virus, new_x, new_y))

print(grid[X-1][Y-1])