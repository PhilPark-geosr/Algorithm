import sys
sys.stdin = open('input_5547.txt', 'r')
input = sys.stdin.readline

W, H = map(int, input().split())
grid = [[0]*(W+2)]
for _ in range(H):
    line =[0]  + list(map(int, input().split())) + [0]
    grid.append(line)
grid.append([0]*(W+2))
# print(grid)

def is_range(x,y):
    if 0<=x<=H+1 and 0<=y<=W+1:
        return True
    return False

def is_hole(i,j):

    if i<=1 or i >= H or j<=1 or j>=W: #가생이 있는 애들은 다 구멍이 아님(둘러쌓이지 않았음)
        return False
    if i %2 ==1: #홀수
        dx = [-1, -1, 0, 0, 1, 1]
        dy = [1,   0, -1,1, 0, 1]

    else:
        dx = [-1, -1, 0, 0, 1, 1]
        dy = [0, -1, -1, 1, -1, 0]

    visited[i][j] = 1
    for k in range(6):
        new_x, new_y = i + dx[k], j + dy[k]
        if is_range(new_x, new_y) == True and grid[new_x][new_y] == 0 and visited[new_x][new_y] ==0:
            check = is_hole(new_x, new_y)
            if check == False:
                return False
    visited[i][j] = 0
    return True





def check_cnt(i,j):# 맞닿은 면 계산하는 함수
    cnt =0
    if i %2 ==1: #홀수
        dx = [-1, -1, 0, 0, 1, 1]
        dy = [1,   0, -1,1, 0, 1]

    else:
        dx = [-1, -1, 0, 0, 1, 1]
        dy = [0, -1, -1, 1, -1, 0]

    for k in range(6):
        new_x, new_y = i + dx[k], j + dy[k]
        # print(new_x, new_y)

        if grid[new_x][new_y] == 0 and is_hole(new_x, new_y) == False:
            cnt += 1

    return cnt

answer = 0
for i in range(1, H+1):
    for j in range(1, W+1):
        # print(f"{i}행, {j}열")
        if grid[i][j] == 1:
            # print(f"{j},{i} 면{check_cnt(i, j)}")
            visited = [[0] * (W + 2) for _ in range(H + 2)]
            answer += check_cnt(i,j)
#
print(answer)

#
# print(check_cnt(3,1))
# print(is_hole(3,1))