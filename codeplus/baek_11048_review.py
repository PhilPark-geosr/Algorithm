import sys
sys.setrecursionlimit(10**9)

sys.stdin = open('input_11048.txt', 'r')

N, M = map(int, input().split())
grid = []
for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)

''' 방법 1'''
# def solution1(N,M, grid):
#     dp = [[-1]*(M) for _ in range(N)]
    
#     def dfs(i, j):
#         # print(f"dfs{i,j}")

#         if i < 0 or j<0:
#             return 0

#         if dp[i][j] !=-1:
#             return dp[i][j]
        
#         dp[i][j] = max(dfs(i-1, j-1), dfs(i-1, j), dfs(i, j-1))+ grid[i][j]
#         return dp[i][j]

#     answer = dfs(N-1, M-1)
#     return answer

# print(solution1(N, M, grid))


''' 방법 2 '''
def solution2(N,M, grid):
    dp = [[0]*(M) for _ in range(N)]
    
    dp[0][0] = grid[0][0]

    for i in range(N):
        for j in range(M):

            if i+1 < N:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j] + grid[i+1][j])
            if i+1 < N and j+1 <M :
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + grid[i+1][j+1])
            if j+1< M:
                dp[i][j+1] = max(dp[i][j+1], dp[i][j] + grid[i][j+1])
    
    answer = dp[N-1][M-1]
    return answer


print(solution2(N, M, grid))

