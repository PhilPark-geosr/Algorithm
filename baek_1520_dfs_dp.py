import sys
sys.stdin = open('input_1520.txt', 'r')

M, N = map(int, input().split())

# grid, visited 생성
visited = [[0]*N for _ in range(M)]
grid = []
for _ in range(M):
    line = list(map(int, input().split()))
    grid.append(line)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
# dfs 정의

## 시간초과 풀이
# global cnt
# def dfs(i, j, prev_h):
#     global cnt
#     print(f"dfs{i, j, prev_h}")
#     if i == M-1 and j == N-1:
#         cnt +=1
#     else:
#         for k in range(4):
#             new_x, new_y = i + dx[k], j + dy[k]
#             if 0<=new_x< M and 0<=new_y<N and visited[new_x][new_y] ==0 and grid[new_x][new_y] < prev_h:
#                 visited[new_x][new_y] =1
#                 dfs(new_x, new_y, grid[new_x][new_y])
#                 visited[new_x][new_y] =0

# dfs구하기
# cnt = 0
# visited[0][0] = 1
# dfs(0,0, grid[0][0])
# print(cnt)


# dp 풀이
# dp[i][j] : i,j 에서 ~ (M-1, N-1) 까지 가는 경우의 수
# dp[i][j] = dp[i+1][j] + dp[i-1][j] + dp[i][j+1] + dp[i][j-1]
# dp = [[0]*N for _ in range(M)]
# def dfs(i, j, prev_h):
#     # print(f"dfs{i,j} {dp}")
#     if i == M-1 and j ==N-1: #맨끝에 잘 도달했을때,
#         return 1
#     else:
    
#         if dp[i][j]==0 or visited[i][j] ==0: # 계산 안된 애들만 처리
#             for k in range(4):
#                 new_x, new_y = i + dx[k], j + dy[k]
#                 if 0<=new_x< M and 0<=new_y<N and visited[new_x][new_y] ==0 and grid[new_x][new_y] < prev_h:
#                     ## 이미 처리가 된 애들이면..
#                     visited[new_x][new_y] =1
#                     # dp에 기록
#                     dp[i][j] += dfs(new_x, new_y, grid[new_x][new_y])                
                    
#                     visited[new_x][new_y] =0
#         # else: #계산된 애들은 바로 리턴
#         return dp[i][j]

# visited[0][0] =1
# dfs(0,0, grid[0][0])
# print(dp[0][0])


dp = [[-1]*N for _ in range(M)]
def dfs(i, j, prev_h):
    # print(f"dfs{i,j} {dp}")
    if i == M-1 and j ==N-1: #맨끝에 잘 도달했을때,
        return 1
    else:
    
        if dp[i][j]==-1 : # 계산 안된 애들만 처리
            dp[i][j] = 0 # 탐색 유무
            for k in range(4):
                new_x, new_y = i + dx[k], j + dy[k]
                if 0<=new_x< M and 0<=new_y<N and grid[new_x][new_y] < prev_h:
                    # dp에 기록
                    dp[i][j] += dfs(new_x, new_y, grid[new_x][new_y])                
                    
        # else: #계산된 애들은 바로 리턴
        return dp[i][j]


dfs(0,0, grid[0][0])
print(dp[0][0])