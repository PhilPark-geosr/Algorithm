import sys
sys.stdin = open('input_1890.txt','r')


N = int(input())

grid = []
for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)
# print("grid", grid)

#
dp = [[0]*N for  _ in range(N)]
dp[0][0] =1
for x in range(N):
    for y in range(N):
        if grid[x][y] ==0:
            continue
        
        caselist = [(x+ grid[x][y], y), (x, y+grid[x][y])]
        # print(caselist)
        for new_x, new_y in caselist:
            if 0<=new_x<N and 0<=new_y<N:
                dp[new_x][new_y] += dp[x][y]

print(dp[x][y])