import sys
import collections
sys.stdin = open('input_꼬리잡기놀이.txt', 'r')
input = sys.stdin.readline
N, M, K = map(int, input().split()) # 격자수, 팀 수 , 라운드 수
grid = [[-1]*(N+1)]
for _ in range(N):
    line = [-1] + list(map(int, input().split()))
    grid.append(line)
# print('grid', grid)
dx = [1,-1, 0,0]
dy = [0,0, 1, -1]
# 팀 추가하기
def dfs(i, j, visited):
    # print(f'dfs{i,j}')
    visited.add((i, j))
    team.append((i, j))
    candidates = []  # 갈 수 있는 곳 리스트
    for k in range(4):
        new_x, new_y = i + dx[k], j + dy[k]
        # print('new_x, new_y', new_x, new_y)

        if 1<=new_x<=N and 1<=new_y<=N and 1<= grid[new_x][new_y] <=3 and (new_x, new_y) not in visited:
            candidates.append((grid[new_x][new_y], new_x, new_y))
    candidates.sort(key = lambda x: x[0]) #2먼저
    for value, new_x, new_y in candidates :
        if (new_x, new_y) not in visited:
            dfs(new_x, new_y, visited)


# 팀 찾기
total_team = []
for i in range(1, N+1):
    for j in range(1, N+1):
        if grid[i][j] == 1:
            # print(f'{i,j} 검사합니다')
            team = collections.deque()
            visited = set()
            dfs(i,j, visited)
            # print(team)
            total_team.append(team)

# print(total_team)

def move(): # 팀별로 한칸씩 이동
    for team in total_team:
        # 새로운 head 찾기
        new_hx, new_hy = 0,0
        h_x, h_y = team[0]
        # print("h_x, h_y, value", h_x, h_y) #head 맞는지 검증

        for k in range(4):
            new_x, new_y = h_x + dx[k], h_y + dy[k]
            if 1<=new_x<=N and 1<=new_y<=N and grid[new_x][new_y] ==4: #새로운 방향 찾았으면
                new_hx, new_hy = new_x, new_y
                break

        # 꼬리에 꼬리를 무는 경우
        if (new_hx, new_hy) == (0,0):
            new_hx, new_hy = team[-1] #꼬리가 맨앞
        # print('new_hx, new_hy',new_hx, new_hy)
        # 일단 grid 초기화
        for x, y in team:
            grid[x][y] = 4


        # 팀 움직이기
        team.appendleft((new_hx, new_hy))
        team.pop()

        # 위치 업데이트
        for i in range(len(team)):
            x, y = team[i]
            if i == 0:
                grid[x][y] =1
            elif i == len(team)-1:
                grid[x][y] =3
            else:
                grid[x][y] =2


        # print(team)
    # print("total_team", total_team)

# move()
# print(total_team)

# 공 맞추기
global score

def get_score(round):
    global score
    round = round%(4*N)
    # print('round', round)
    row = round % N
    if row == 0:
        row = N
    # print('round, row', round, row)
    if 1<=round<=N:
        target_x, target_y = 0,0
        for j in range(1, N+1):
            if 1<=grid[row][j]<=3: #총을 맞으면
                target_x, target_y = row, j
                break


    elif N+1 <= round <= 2*N:
        target_x, target_y = 0, 0
        for j in range(N, 0, -1):
            if 1 <= grid[j][row] <= 3:  # 총을 맞으면
                target_x, target_y = j, row
                break

    elif 2*N+1 <= round <= 3*N:
        row = N-row +1
        # print('row', row)
        target_x, target_y = 0, 0
        for j in range(N, 0, -1):
            if 1 <= grid[row][j] <= 3:  # 총을 맞으면
                target_x, target_y = row, j
                break

    else: # 3*N+1 <=round <= 4*N
        row = N - row + 1
        # print('row', row)
        target_x, target_y = 0, 0
        for j in range(1, N+1):
            if 1 <= grid[j][row] <= 3:  # 총을 맞으면
                target_x, target_y = j, row
                break
    # print('target_x, target_y', target_x, target_y)
    if (target_x, target_y) != (0, 0):  # 총을 맞은 경우만
        for team in total_team:
            if (target_x, target_y) in team:
                idx = team.index((target_x, target_y))
                score += (idx + 1) ** 2
                team.reverse()
                break
    # print("score", score)

# test
# score = 0
# get_score(1)

score = 0
for round in range(1, K+1):
    # print(f'--------------------{round}-----------------------')
    move()
    get_score(round)

print(score)