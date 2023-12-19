import sys
sys.setrecursionlimit(10**9)

sys.stdin =open('input_2169.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [[0]*(M+2)]
for _ in range(N):
    line = [0] + list(map(int, input().split())) +[0]
    grid.append(line)
# print(grid)
dp = [[[False]*(3) for _ in range(M+2)] for _ in range(N+2)]
dp[1][1][0], dp[1][1][1], dp[1][1][2] = grid[1][1],grid[1][1],grid[1][1]
def dfs(i ,j, dir):
    # print(f"dfs{i,j,dir}")
    if i==1 and dir ==0:
        return -float('inf')
    if j == M and dir ==2:
        return -float('inf')
    
    if dp[i][j][dir] !=False:
        return dp[i][j][dir]

    if dir ==0:
        if i-1 >0:
            dp[i][j][dir] = max(dfs(i-1, j, 0), dfs(i-1,j, 1), dfs(i-1, j,2)) +grid[i][j]

    elif dir ==1:
        if j-1 >0:
            dp[i][j][dir] = max(dfs(i, j-1, 0), dfs(i, j-1, 1)) +grid[i][j]

    else: # dir ==2:
        if j+1 <=N:
            dp[i][j][dir] = max(dfs(i, j+1, 0), dfs(i,j+1, 2)) +grid[i][j]

    
    return dp[i][j][dir]
# print(dfs(1,2,2))
print(max(dfs(N, M,0), dfs(N,M,1)))

# dp = [[[-float('inf')]*(3) for _ in range(M+2)] for _ in range(N+2)]


# for i in range(1, N+1):
#     for j in range(1, M+1):
#         for dir in range(3):
            
#             dp[i][j][dir] = max(dfs(i-1, j, 0), dfs(i-1,j, 1), dfs(i-1, j,2))
