import sys
import collections
sys.stdin = open('input_코드트리 빵.txt', 'r')
input = sys.stdin.readline

#input
n, m = map(int, input().split())
grid = []
for _ in range(n):
    line = list(map(int, input().split()))
    grid.append(line)
# 베이스 캠프 위치 기록
basecamp_list = []
for i in range(n):
    for j in range(n):
        if grid[i][j] ==1:
            basecamp_list.append((i,j))

# 편의점 위치 기록
want = dict()
store = []
for i in range(1, m+1):
    a,b = map(int, input().split())
    store.append((a-1,b-1))
    want[i] = (a-1,b-1)
# print('want', want)
# print('store', store)

# q 기록
q = []

def get_basecamp_list(t):
    # 편의점 위치
    store_x, store_y = want[t]
    # 최소거리 구하기
    dist = float('inf')
    for x,y in basecamp_list:
        new_dist, _, _ = bfs(store_x, store_y,x,y)
        dist = min(dist, new_dist)
    # 최소거리 해당하는 좌표 찾기
    result = []
    for x,y in basecamp_list:
        new_dist, _, _ =  bfs(store_x, store_y,x,y)
        if new_dist == dist:
            result.append((x,y))

    # TODO: 정렬 해야하나..?
    # DONE : 안해도됨(애초에 행 -> 열 순서로 추가했음) 
    return result




def step3(t):
    if t > m:
        return
    # 원하는 편의점
    store_x, store_y = want[t]
    # basecamp리스트 뽑기
    candidate_list = get_basecamp_list(t)
    for x, y in candidate_list:
        if grid[x][y] ==-1:
            continue
        grid[x][y] =-1 #갈수 없음 처리
        # 베이스캠프에서 없애기
        q.append((x,y, store_x, store_y))
        basecamp_list.remove((x,y))
        
        break

def move_up(x,y):
    new_x, new_y = x - 1, y
    if 0<=new_x<n and 0<=new_y<n and grid[new_x][new_y]!=-1: #갈 수 없으면 안간다
        return new_x, new_y
    return x,y
def move_left(x,y):
    new_x, new_y = x, y-1
    if 0<=new_x<n and 0<=new_y<n and grid[new_x][new_y]!=-1: #갈 수 없으면 안간다
        return new_x, new_y
    return x,y
def move_right(x,y):
    new_x, new_y = x, y+1
    if 0<=new_x<n and 0<=new_y<n and grid[new_x][new_y]!=-1: #갈 수 없으면 안간다
        return new_x, new_y
    return x,y
def move_down(x,y):
    new_x, new_y = x + 1, y
    if 0<=new_x<n and 0<=new_y<n and grid[new_x][new_y]!=-1: #갈 수 없으면 안간다
        return new_x, new_y
    return x,y

def bfs(x,y, store_x, store_y):
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    visited = [[0]*n for _ in range(n)]
    q2 = collections.deque()
    q2.append((0,x,y))
    visited[x][y] = 1
    while q2:
        dist, x, y = q2.popleft()
        if (x,y) == (store_x, store_y):
            return dist, x, y
        for k in range(4):
            new_x, new_y = x +dx[k], y+dy[k]
            if 0<=new_x<n and 0<=new_y<n and visited[new_x][new_y] ==0 and \
            grid[new_x][new_y] !=-1:
                visited[new_x][new_y] =1
                q2.append((dist+1, new_x, new_y))
    return float('inf'), x, y

def move(x,y, store_x, store_y):
    # 원래 최단 거리
    #dist = abs(store_x-x) + abs(store_y-y)
    #dist = abs(store_x-x) + abs(store_y-y)
    dist, _, _ = bfs(x, y, store_x, store_y)
    #
    # 위로 움직여본다
    new_x, new_y = move_up(x,y)
    new_dist, _, _ = bfs(new_x, new_y,store_x, store_y )
    if new_dist < dist: #거리가 가까워 지면 갈수 있다
        return new_x, new_y
    # 왼쪽
    new_x, new_y = move_left(x,y)
    new_dist, _, _ = bfs(new_x, new_y,store_x, store_y )
    if new_dist < dist: #거리가 가까워 지면 갈수 있다
        return new_x, new_y
    
    #오른쪽
    new_x, new_y = move_right(x,y)
    new_dist, _, _ = bfs(new_x, new_y,store_x, store_y )
    if new_dist < dist: #거리가 가까워 지면 갈수 있다
        return new_x, new_y
    
    # 아래
    new_x, new_y = move_down(x,y)
    new_dist, _, _ = bfs(new_x, new_y,store_x, store_y )
    if new_dist < dist: #거리가 가까워 지면 갈수 있다
        return new_x, new_y
    
    

def step1(t, q): #격자에 있는 사람들 한칸 씩 움직이기
    temp = []
    # 새로운 좌표
    for x, y, store_x, store_y in q:
        new_x, new_y = move(x,y, store_x, store_y)
        temp.append((new_x, new_y, store_x, store_y))
    temp2 = []
    # temp 돌면서 편의점 도착했는지 확인하기
    for x, y, store_x, store_y in temp:
        if (x,y) == (store_x, store_y):# 편의점에 있으면
            grid[x][y] = -1
        else:
            temp2.append((x,y, store_x, store_y))
    #바꿔치기
    q = temp2 
    return q
    
        




# test
# step3(1)
# print(q)
# q = step1(2, q)
# step3(2)
# print(q)
# q = step1(3, q)
# step3(3)
# print(q)
# q = step1(4, q)
# step3(4)
# print(q)
# main
t = 1
while True:
    if t ==1:
        step3(t)

    else:
        q= step1(t, q)
        step3(t)
    # print('basecamplist', basecamp_list)
    # print("q", q)
    # print(grid)

    # check
    if len(q) == 0:
        print(t)
        break
    else:
        t +=1