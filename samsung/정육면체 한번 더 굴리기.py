import sys
sys.stdin = open('정육면체 한번 더 굴리기.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [[0]*(N+1)]
for _ in range(N):
    line = [0] + list(map(int, input().split()))
    grid.append(line)
dirs = [(-1,0), (0,1), (1,0), (0,-1)]
dice = {
    "bottom" : 6,
    "roof" : 1,
    "right" : 3,
    "left" : 4,
    "up" : 5,
    "down" : 2,
}


global total_score #얻게 되는 총 점수
global x, y
x, y = 1, 1
global d #출발은 항상 오른쪽
d = 1

def get_direction():
    global x, y
    global d
    num = grid[x][y] #현재위치 불러오기
    # print('num', num)
    if dice["bottom"] > num:
        d = d+1 if d<3 else 0
    elif dice['bottom'] == num:
        pass
    else:
        d = d-1 if d>0 else 3




def is_range(x,y):
    if 1<=x <=N and 1<=y<=N:
        return True
    return False
def reverse_dir():
    global d
    if d ==0:
        d = 2
    elif d == 1:
        d = 3
    elif d ==2:
        d =0
    else:
        d =1


def turn_right():
    dice['left'], dice['bottom'], dice['right'], dice['roof'] = \
    dice['bottom'],dice['right'], dice['roof'],  dice['left']
    # print('dice', dice)

def turn_left():
    dice['right'], dice['bottom'], dice['left'], dice['roof'] = \
        dice['bottom'], dice['left'], dice['roof'], dice['right']
    # print('dice', dice)

def turn_down():
    dice['up'],   dice['bottom'], dice['down'], dice['roof'] = \
    dice['bottom'], dice['down'],  dice['roof'], dice['up']
    # print('dice', dice)
def turn_up():
    dice['down'], dice['bottom'], dice['up'], dice['roof'] = \
    dice['bottom'], dice['up'], dice['roof'], dice['down']
    # print('dice', dice)

def rolling(i):
    global x, y
    if i !=0:
        get_direction()
        # print('바뀐 dir', d)
    temp_x, temp_y = x + dirs[d][0],  y+ dirs[d][1]
    if is_range(temp_x, temp_y) == False:
        reverse_dir()
        # print('벽이 있어서 방향을 바꾸겠습니다', d)
        new_x, new_y = x + dirs[d][0],  y+ dirs[d][1] # 새로운 방향
    else:
        new_x, new_y = temp_x, temp_y  #그대로 이동
    # 좌표 이동
    x, y = new_x, new_y

    # 주사위 굴리기
    if d == 0:
        turn_up()
    elif d ==1:
        turn_right()
    elif d ==2:
        turn_down()
    else:# d ==3:
        turn_left()



def get_total_score():
    global x, y
    global score
    global total_score
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    cur_x, cur_y = x, y # 현재 위치 받아옴
    num = grid[cur_x][cur_y]
    # print('현재 격자의 번호', num)
    visited = [[0]*(N+1) for _ in range(N+1)]
    def dfs(v, i,j):
        global score
        if grid[i][j] !=v:
            return
        score += grid[i][j] #점수 입력
        visited[i][j] =1
        for k in range(4):
            new_x, new_y = i + dx[k], j + dy[k]
            if is_range(new_x, new_y) == True and visited[new_x][new_y] == 0 and grid[new_x][new_y] == v:
                dfs(v, new_x, new_y)
        # visited[i][j] = 0
    score = 0
    dfs(num, cur_x, cur_y)
    # print('점수', score)
    total_score += score


# 수행
total_score = 0
for i in range(M):

    rolling(i)
    # print('x,y', x, y)
    # print('bottom', dice['bottom'])
    # print('move_dir', d)
    get_total_score()

print(total_score)