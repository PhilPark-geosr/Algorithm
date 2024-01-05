import sys
sys.stdin = open('input_20543.txt', 'r')
N, M = map(int, input().split())

grid = []
for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)


#폭탄위치 기록
bomb = [[0]*N for _ in range(N)]
def find_largest_idx():
    largest_value = -float('inf')
    answer_i, answer_j = -1, -1
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                continue
            if grid[i][j] > largest_value :
                largest_value = grid[i][j]
                answer_i, answer_j = i, j
    # print("가장 큰 인덱스", answer_i, answer_j)
    return answer_i, answer_j, -largest_value


def is_range(new_x, new_y):
    if 0<=new_x<N and 0<=new_y<N:
        return True
    return False


def can_bomb(x, y, dx, dy):
    if dx <0 and dy >0:

        for i in range(x, x+ dx-1, -1):
            for j in range(y, y+dy+1):
                if grid[i][j] == 0:
                    return False
    elif dx < 0 and dy < 0:
        for i in range(x, x+ dx-1, -1):
            for j in range(y, y+dy-1, -1):
                if grid[i][j] == 0:
                    return False

    elif dx > 0 and dy < 0:
        for i in range(x, x+ dx +1):
            for j in range(y, y+dy-1, -1):
                if grid[i][j] == 0:
                    return False

    else:
        for i in range(x, x + dx+1):
            for j in range(y, y+dy+1):
                if grid[i][j] == 0:
                    return False

    return True




def find_center(x, y, m):
    step = m//2
    dx = [-step, step, -step, step]
    dy = [step, step, -step, -step]

    for k in range(4):
        new_x, new_y = x + 2*dx[k], y + 2*dy[k]
        # print('new_x, new_y', (new_x, new_y))
        if is_range(new_x, new_y) == True and can_bomb(x, y, 2*dx[k], 2*dy[k]) == True:
            # print('중심점', (new_x, new_y))
            return x + dx[k], y+dy[k]


def heal(c_x, c_y, m, _amount_of_heal):
    # 왼쪽상단
    step = m//2
    bomb[c_x][c_y] += _amount_of_heal #힐량 기록
    left_x, left_y = c_x - step, c_y - step
    # print("left_x, left_y, m", left_x, left_y, m)
    for i in range(left_x, left_x +m):
        for j in range(left_y, left_y+ m):
            grid[i][j] += _amount_of_heal


def show_grid(arr):
    for line in arr:
        print(line)


for t in range(1000):
    print("t", t)
    show_grid(grid)
    x, y, amount_of_heal = find_largest_idx()
    print("x,y", x,y)
    if (x,y) == (-1,-1): #더이상 없을경우 종료
        break
    c_x, c_y = find_center(x,y, M)
    heal(c_x,c_y, M, amount_of_heal)

show_grid(bomb)