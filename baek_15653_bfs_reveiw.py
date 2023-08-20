import sys
import collections
sys.stdin =open('input_15653.txt', 'r')
# input = sys.stdin.readline
n, m  = map(int, input().split())
# 1. make a grid

grid = []
for i in range(n):
    line = input()
    temp = []
    for s in line:
        temp.append(s)
    grid.append(temp)
# print('grid', grid)

# 함수 정의
# 양옆 가기
def cal_up(grid, x, y):
    pt = x
    # print('pt',pt)
    while True:
        new_x = pt-1
        # print("new_x", new_x)
        # pt -=1 #왼쪽으로 한칸 이동
        if grid[new_x][y] =="#":
            return (pt, y)
        if grid[new_x][y] =="O": #중간에 구멍이 있어도
            # print('중간에 구멍에 빠집니다')
            return (new_x, y)
        pt = new_x 
def cal_down(grid,x, y):
    pt = x
    while True:
        new_x = pt+1
        # pt -=1 #왼쪽으로 한칸 이동
        if grid[new_x][y] =="#":
            return (pt, y)
        if grid[new_x][y] =="O": #중간에 구멍이 있어도
            # print('중간에 구멍에 빠집니다')
            return (new_x, y)
        pt = new_x
def cal_left(grid,x, y):
    pt = y
    while True:
        new_y = pt-1
        # pt -=1 #왼쪽으로 한칸 이동
        if grid[x][new_y] =="#":
            return (x, pt)
        if grid[x][new_y] =="O": #중간에 구멍이 있어도
            # print('중간에 구멍에 빠집니다')
            return (x, new_y)
        pt = new_y 
def cal_right(grid,x, y):
    pt = y
    while True:
        new_y = pt+1
        # pt -=1 #왼쪽으로 한칸 이동
        if grid[x][new_y] =="#":
            return (x, pt)
        if grid[x][new_y] =="O": #중간에 구멍이 있어도
            # print('중간에 구멍에 빠집니다')
            return (x, new_y)
        pt = new_y 

def vertical(grid, xr, yr, xb,yb): # 좌우로 갈 수 있는 
    result = []
    # 왼쪽
    (new_xr, new_yr), (new_xb, new_yb) = cal_up(grid,xr, yr), cal_up(grid,xb, yb)
    if yr == yb and new_xr == new_xb:
        #구멍에 빠졌을때
        if grid[new_xr][new_yr] == "O":
            pass
        elif xr < xb: # R이 왼쪽에 있었을 경우
            new_xb +=1
        else: # B가 왼쪽에 있었을 경우
            new_xr +=1
    
    result.append((new_xr, new_yr, new_xb, new_yb))

    # 오른쪽
    (new_xr, new_yr), (new_xb, new_yb) = cal_down(grid,xr, yr), cal_down(grid,xb, yb)
    if yr == yb and new_xr == new_xb: # 기울였을때 같은 좌표로 갈때
        #구멍에 빠졌을때
        if grid[new_xr][new_yr] == "O":
            pass
        elif xr < xb: # R이 왼쪽에 있었을 경우
            new_xr -=1
        else: # B가 왼쪽에 있었을 경우
            new_xb -=1

    result.append((new_xr, new_yr, new_xb, new_yb))
    return result
def horizon(grid, xr, yr, xb,yb):
    result = []
    # 위
    (new_xr, new_yr), (new_xb, new_yb)= cal_left(grid,xr, yr), cal_left(grid,xb, yb)
    if xr == xb and new_yr == new_yb:
        #구멍에 빠졌을때
        if grid[new_xr][new_yr] == "O":
            pass
        elif yr < yb: # R이 아래에 있었을 경우
            new_yb +=1
        else: # B가 아래에 있었을 경우
            new_yr +=1
    
    result.append((new_xr, new_yr, new_xb, new_yb))

    # 아래
    (new_xr, new_yr), (new_xb, new_yb) = cal_right(grid,xr, yr), cal_right(grid,xb, yb)
    if xr == xb and new_yr == new_yb:
        #구멍에 빠졌을때
        if grid[new_xr][new_yr] == "O":
            pass
        elif yr < yb: # R이 아래에 있었을 경우
            new_yr -=1
        else: # B가 아래에 있었을 경우
            new_yb -=1
    
    result.append((new_xr, new_yr, new_xb, new_yb))
    return result

# R, B 위치 추출
def extract(grid):
    xr, yr, xb, yb = None, None, None, None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "R":
                xr, yr = i, j
                continue
            if grid[i][j] =="B":
                xb, yb = i, j
                continue
    return (xr, yr, xb, yb)




xr,yr, xb, yb = extract(grid)
cnt = 0 # 공 굴린 횟수
q = collections.deque()
q.append((xr,yr, xb, yb, cnt))
visited = [[[[0]*m for _ in range(n)] for _ in range(m)]  for _ in range(n)]
visited[xr][yr][xb][yb] =1

# test
# print("xr,yr, xb, yb", xr,yr, xb, yb)
# horizon_list = horizon(grid, xr, yr, xb, yb)
# print(horizon_list)

answer = -1
while q:
    # print("q", q)
    xr, yr, xb, yb, cnt = q.popleft()

    if (xr, yr) == (xb, yb) and grid[xr][yr] == "O" : # 둘다 구멍에 빠졌을 경우
        continue

    if (xr, yr) != (xb, yb) and grid[xr][yr] == 'O': # 빨간 애들만 구멍에 빠졌을 경우
        answer = cnt
        break
    if (xr, yr) != (xb, yb) and grid[xb][yb] == 'O': # 파란 애들이 구멍에 빠졌을 경우
        continue

    # 갈 수 잇는 후보지 계산
    horizon_list = horizon(grid,xr, yr, xb, yb)
    vertical_list = vertical(grid, xr, yr, xb, yb)

    # print('horizon_list', horizon_list)
    # print("vertical_list", vertical_list)
    candidates = horizon_list + vertical_list

    for new_xr, new_yr, new_xb, new_yb in candidates:
        if visited[new_xr][new_yr][new_xb][new_yb] == 0 :
            visited[new_xr][new_yr][new_xb][new_yb] =1
            q.append((new_xr, new_yr, new_xb, new_yb, cnt+1))


print(answer)