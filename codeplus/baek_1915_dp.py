import sys
sys.setrecursionlimit(10**9)

sys.stdin = open('input_1915.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())
grid = [[0]*(M+1)]
for _ in range(N):
    line_string = input()
    line = []
    for elem in line_string:
        line.append(int(elem))
    line.insert(0,0)
    grid.append(line)
# print(grid)

dp = [[0]*(M+1) for _ in range(N+1)]
# dp계산
for i in range(1, N+1):
    for j in range(1, M+1):
        if grid[i][j] ==1:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) +1
        else:
            dp[i][j] = 0

# 최댓값 추출
max_value = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        max_value = max(max_value, dp[i][j])

answer = max_value**2 #직사각형의 넓이
print(answer)