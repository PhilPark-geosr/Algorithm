import sys
import collections
import itertools
sys.stdin = open("input_14502.txt", "r")
N, M = map(int, input().split())

grid = []
for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)
# print(grid)
# make caselist
def make_case(array): #O(n^2)
    # 0이 아닌 인덱스만 추출
    result =[]
    for i in range(N):
        for j in range(M):
            if array[i][j] == 0:
                result.append((i,j))
    len_result = len(result)
    idx_list = list(range(len_result))
    caselist = list(itertools.combinations(idx_list, 3))
    # print(caselist)
    return result, caselist

# bfs
def bfs(array):
    new_array = array #객체 복사
    n = len(new_array)
    m = len(new_array[0])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[0]*m for _ in range(n)]
    q = collections.deque()
    # 2인 부분 찾기
    viruslist = []
    for i in range(n):
        for j in range(m):
            if new_array[i][j] == 2:
                viruslist.append((i,j))
    for pos in viruslist:
        a, b = pos
        visited[a][b] = 1
        q.append(pos)

    while q:
        x,y = q.popleft()
        for k in range(4):
            new_x, new_y = x + dx[k], y + dy[k]
            if 0<=new_x<n and 0<=new_y<m and visited[new_x][new_y] ==0 \
                and new_array[new_x][new_y] ==0:
                visited[new_x][new_y] =1 # 방문기록
                new_array[new_x][new_y]=2 #바이러스 전염
                q.append((new_x, new_y)) 

    return new_array

# check 안전영역
def check(array):
    n = len(array)
    m = len(array[0])
    count=0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                count+=1
    return count

result, case_list = make_case(grid)

answer=0
for case in case_list:
    new_grid = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            new_grid[i][j] =grid[i][j]
    
    # 세개 대입
    new_grid[result[case[0]][0]][result[case[0]][1]] = 1 
    new_grid[result[case[1]][0]][result[case[1]][1]] = 1
    new_grid[result[case[2]][0]][result[case[2]][1]] = 1
    # print(new_grid)
    # bfs 수행
    new_grid2 = bfs(new_grid)
    # 안전영역 체크
    # print(new_grid2)
    safe_area = check(new_grid2)

    if safe_area > answer:
        answer = safe_area

print(answer)




