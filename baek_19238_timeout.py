import sys
import heapq
import collections
sys.stdin = open('input_19238.txt', 'r')
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

N, M, gage = map(int, input().split())
grid = [[0]*(N+1)]
for _ in range(N):
    line = [0] + list(map(int, input().split()))
    grid.append(line)
# print("grid", grid)

taxi_x, taxi_y = map(int, input().split())
destination = dict()
des_list  = []
for _ in range(M):
    x,y,a,b = map(int, input().split())
    destination[(x,y)] = (a,b)
    des_list.append((x,y))

# des_list정렬
des_list.sort()
def is_range(x, y):
    if 1<=x<=N and 1<=y<=N:
        return True
    return False

# 최단거리 재는 함수
def bfs(s_x,s_y, des_x, des_y): #최단거리 찾기
    q = collections.deque()
    visited =[[0]*(N+1) for _ in range(N+1)]
    visited[s_x][s_y] = 1
    q.append((0, s_x, s_y))

    while q:
        d, x, y = q.popleft()
        if (x,y) == (des_x, des_y):
            return d

        for k in range(4):
            new_x, new_y = x + dx[k], y+ dy[k]
            if is_range(new_x, new_y) == True and grid[new_x][new_y] !=1 and visited[new_x][new_y] == 0:
                visited[new_x][new_y] = 1 #방문처리
                q.append((d+1,new_x, new_y))

def find_nearest_people():
    global taxi_x, taxi_y, gage

    s_x, s_y = taxi_x, taxi_y #출발위치 받아놓는다
    q = []

    min_dist = float('inf')
    min_des_x, min_des_y = -1,-1
    # des_list = sorted(list(destination.keys()))
    # print(des_list)
    for start in des_list:
        des_x, des_y = start
        dist = bfs(s_x,s_y, des_x, des_y)
        if dist < min_dist:
            min_dist = dist
            min_des_x, min_des_y = des_x, des_y

        # heapq.heappush(q, (dist, des_x, des_y))
    # print(q)
    #최소거리 추출
    # dist, des_x, des_y = heapq.heappop(q)
    gage -= min_dist #게이지 감소
    taxi_x, taxi_y = min_des_x, min_des_y #택시위치 업데이트
    # print("gage", gage)

    return min_des_x, min_des_y

def move_to(x,y):
    global taxi_x, taxi_y, gage
    des_x, des_y = destination[(x,y)] #목적지 추출
    d = bfs(x,y, des_x, des_y)

    # 이동
    taxi_x, taxi_y = des_x, des_y
    #연료감소
    gage -=d
    # 사용량 측정
    use = d

    #목적지 제거
    destination.pop((x,y), None)
    des_list.remove((x,y))
    return use

def charge(use):
    global gage
    gage += 2*use




# test
# print(find_nearest_people())



# ---------------------- main -----------------------#
while M >0:
    # print("gage", gage)
    # 가장 거리 가까운애 찾기
    x,y = find_nearest_people()
    if gage <0:
        print(-1)
        break

    # 이동
    use = move_to(x,y)
    # print('연료 사용량', use)
    if gage < 0:
        print(-1)
        break
    # 연료 충전
    charge(use)
    # print("충전후 gage", gage)
    # 승객 이동완료
    M-=1

print(gage)









