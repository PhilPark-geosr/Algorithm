import sys
sys.stdin = open('input_나무박멸.txt', 'r')
input = sys.stdin.readline

N, M, K, C = map(int, input().split())
# 격자수, 진행년수, 제초제 확산 범위, 제초제 유지기간

grid = []
for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)

# 제초제 기록 테이블
timetable = [[0]*N for _ in range(N)]
global trees
trees = 0 #박멸한 나무의 수
pos_wall= dict() # 벽위치 기록
# print("grid", grid)
dx = [1,-1,0,0]
dy = [0,0, 1,-1]
def grow():
    for i in range(N):
        for j in range(N):
            if grid[i][j] >0:
                cnt = 0
                for k in range(4):
                    new_x, new_y = i +dx[k], j + dy[k]
                    if 0<=new_x< N and 0<=new_y<N and grid[new_x][new_y] >0:
                        cnt+=1
                grid[i][j] +=cnt
    # print(grid)
def duplicate():
    temp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if grid[i][j] >0:
                cnt =0
                for k in range(4):
                    new_x, new_y = i +dx[k], j+ dy[k]
                    if 0<=new_x<N and 0<=new_y<N and grid[new_x][new_y] ==0:
                        cnt+=1
                if cnt !=0: # 번식할 수 있는 곳이 있을때
                    for k in range(4):
                        new_x, new_y = i + dx[k], j + dy[k]
                        if 0 <= new_x < N and 0 <= new_y < N and grid[new_x][new_y] == 0:
                            temp[new_x][new_y] += grid[i][j] // cnt
    # temp 배열결과를 옮기기
    for i in range(N):
        for j in range(N):
            grid[i][j] += temp[i][j]
    # print(grid)
def find_kill():
    global trees
    max_value = 0
    answer_i, answer_j = 0,0
    for i in range(N):
        for j in range(N):
            if grid[i][j] >0:
                sum_value = 0
                for h in range(K+1):
                    new_x, new_y = i + h, j+h
                    if 0<=new_x<N and 0<=new_y<N:
                        if grid[new_x][new_y] <=0 :
                            break
                        sum_value +=grid[new_x][new_y]
                for h in range(-1, -K-1, -1):
                    new_x, new_y = i + h, j + h
                    if 0 <= new_x < N and 0 <= new_y < N:
                        if grid[new_x][new_y] <=0:
                            break
                        sum_value += grid[new_x][new_y]
                for h in range(1, K+1):
                    new_x, new_y = i + h, j-h
                    if 0<=new_x<N and 0<=new_y<N:
                        if grid[new_x][new_y] <=0:
                            break
                        sum_value +=grid[new_x][new_y]
                for h in range(-1, -K-1, -1):
                    new_x, new_y = i + h, j - h
                    if 0 <= new_x < N and 0 <= new_y < N:
                        if grid[new_x][new_y] <=0:
                            break
                        sum_value += grid[new_x][new_y]
                if sum_value > max_value:
                    max_value = sum_value
                    answer_i, answer_j = i,j

    # print(temp)
    # print(answer_i, answer_j, max_value)
    # 제초제 뿌리기
    # 박멸한 나무의 수 업데이트
    trees += max_value

    # print('max_del', max_value)
    for h in range(K + 1):
        new_x, new_y = answer_i + h, answer_j + h
        if 0 <= new_x < N and 0 <= new_y < N:
            if grid[new_x][new_y] == 0 :
                # 벽이있거나 나무가 없는 그곳까지는 제초제가 들어감, 그 이후는 안함
                grid[new_x][new_y] = -2
                # 제초제 유지기간 기록하기
                timetable[new_x][new_y] = C
                break
            if grid[new_x][new_y] == -1:
                break
            grid[new_x][new_y] =-2
            # 제초제 유지기간 기록하기
            timetable[new_x][new_y] = C

    for h in range(-1, -K - 1, -1):
        new_x, new_y = answer_i + h, answer_j + h
        if 0 <= new_x < N and 0 <= new_y < N:
            if grid[new_x][new_y] == 0 :
                grid[new_x][new_y] = -2
                # 제초제 유지기간 기록하기
                timetable[new_x][new_y] = C
                break
            if grid[new_x][new_y] == -1:
                break
            grid[new_x][new_y] = -2
            # 제초제 유지기간 기록하기
            timetable[new_x][new_y] = C
    for h in range(1, K + 1):
        new_x, new_y = answer_i + h, answer_j - h
        if 0 <= new_x < N and 0 <= new_y < N:
            if grid[new_x][new_y] == 0 :
                grid[new_x][new_y] = -2
                # 제초제 유지기간 기록하기
                timetable[new_x][new_y] = C
                break
            if grid[new_x][new_y] == -1:
                break
            grid[new_x][new_y] = -2
            # 제초제 유지기간 기록하기
            timetable[new_x][new_y] = C
    for h in range(-1, -K - 1, -1):
        new_x, new_y = answer_i + h, answer_j - h
        if 0 <= new_x < N and 0 <= new_y < N:
            if grid[new_x][new_y] == 0 :
                grid[new_x][new_y] = -2
                # 제초제 유지기간 기록하기
                timetable[new_x][new_y] = C
                break
            if grid[new_x][new_y] == -1:
                break
            grid[new_x][new_y] = -2
            # 제초제 유지기간 기록하기
            timetable[new_x][new_y] = C
    # print('herb', timetable)
    # print('trees', grid)

def update():
    for i in range(N):
        for j in range(N):
            if timetable[i][j] >0:
                timetable[i][j] -=1
                if timetable[i][j] ==0 : #깎아서 0이되면
                    grid[i][j] = 0 #원상복구
    # print('herb', timetable)
# grow()
# print(grid)
# duplicate()
# print(grid)
# find_kill()

    
for year in range(M):
    # print(f'--------------새로운 { year+1 } 년도 시작 ---------------')
    grow()
    duplicate()
    update()  # 제초제 업데이트
    find_kill()

print(trees)