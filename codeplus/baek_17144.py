import sys
import copy
sys.stdin = open('input_17144.txt', 'r')
input = sys.stdin.readline

N, M, T = map(int, input().split())
grid = []
for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)

# find 공기청정기
upper_i = 0
lower_i = 0
for i in range(N):
    if grid[i][0] ==-1:
        if upper_i ==0:
            upper_i = i
        else: 
            lower_i = i
    if upper_i !=0 and lower_i !=0:
        break


# print(grid)
def solution(N, M, T, grid):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    def spread(i, j):
        count = 0
        for k in range(4):
            new_x, new_y = i+ dx[k], j + dy[k]
            if 0<=new_x < N and 0<=new_y <M and grid[new_x][new_y] !=-1:
                temp[new_x][new_y] += grid[i][j] //5
                count+=1

            
        temp[i][j] -= (count)*(grid[i][j]//5)

    def circulate(i, dir):
        copy_grid = copy.deepcopy(grid)
        # print("copy", copy_grid)
        if dir == -1: #반시계
            for j in range(2, M):
                
                grid[i][j] = copy_grid[i][j-1]
            grid[i][1] = 0
            for k in range(i-1, -1, -1):
                grid[k][M-1] = copy_grid[k+1][M-1]

            for j in range(M-2, -1, -1):
                grid[0][j]= copy_grid[0][j+1]

            for k in range(1, i):
                grid[k][0] = copy_grid[k-1][0]

        else: #시계
            for j in range(2, M):
                grid[i][j] = copy_grid[i][j-1]
            grid[i][1] = 0

            for k in range(i+1, N):
                grid[k][M-1] = copy_grid[k-1][M-1]

            for j in range(M-2, -1, -1):
                grid[N-1][j]= copy_grid[N-1][j+1]

            for k in range(N-2, i, -1):
                grid[k][0] = copy_grid[k+1][0]


    for _ in range(T):
        temp = [[0]*M for _ in range(N)]
        # spread(0,7)
        for i in range(N):
            for j in range(M):
                if grid[i][j] == -1:
                    continue
                spread(i,j)
        # print("temp", temp)

        for i in range(N):
            for j in range(M):
                if grid[i][j] ==-1:
                    continue
                grid[i][j] += temp[i][j]
        
        # print("grid", grid)
    
        circulate(upper_i, -1)
        circulate(lower_i, 1)

        # print(grid)
            
    answer = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] ==-1:
                continue
            answer += grid[i][j]
    
    return answer

# 정답 계산
print(solution(N, M, T, grid))