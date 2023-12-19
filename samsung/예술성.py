import sys
import itertools
import collections
sys.stdin = open('예술성.txt', 'r')
input = sys.stdin.readline

N = int(input())
grid = []
for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)

global myanswer


def process():
    global myanswer
    def dfs(i, j, cnt, value):

        group[i][j] = cnt
        visited[i][j] = 1
        for k in range(4):
            new_x, new_y = i + dx[k], j + dy[k]
            if 0 <= new_x < N and 0 <= new_y < N and visited[new_x][new_y] == 0 and grid[new_x][new_y] == value:
                dfs(new_x, new_y, cnt, value)
        visited[i][j] = 0

    visited = [[0]*N for _ in range(N)]
    group = [[0]*N for _ in range(N)] #무슨 그룹인지 체크
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    value_dic = dict() #해당값이 어느 그룹에 속하는지
    group_list = [] #첫 시작
    cnt = 1
    for i in range(N):
        for j in range(N):
            if group[i][j] ==0:
                dfs(i, j, cnt, grid[i][j])
                value_dic[cnt] = grid[i][j]
                group_list.append((i,j,cnt))
                cnt+=1
    # print(group)
    num_of_groups = cnt-1 #그룹의 수

# candidates = [i for i in range(1, num_of_groups+1)]
# print(candidates)

    def bfs(i,j, num):
        q = collections.deque()
        q.append((i, j))
        while q:
            x, y = q.popleft()
            for k in range(4):
                new_x, new_y = x + dx[k], y+dy[k]
                if 0<=new_x<N and 0<=new_y<N and visited2[new_x][new_y] == 0:
                    if group[new_x][new_y] != num: #서로 그룹이 다르다 == 맞닿는다
                        match[group[new_x][new_y]][num] += 1
                        match[num][group[new_x][new_y]] += 1
                    else:
                        visited2[new_x][new_y] = 1
                        blocks[num] += 1
                        q.append((new_x, new_y))

    # def find_idx(num):
    #     for i in range(N):
    #         for j in range(N):
    #             if group[i][j] == num:
    #                 return (i ,j, num)

    # for i in range(1, num_of_groups+1):
    #     group_list.append(find_idx(i))
# print(group_list)

# 각 그룹간에 맞닿는 변의 개수 판별
    match = [[0]*(num_of_groups+1) for  _ in range(num_of_groups+1)]
    visited2 = [[0]*N for _ in range(N)]

    blocks = collections.defaultdict(int)
    for i,j, num in group_list:
        visited2[i][j] = 1
        blocks[num] +=1
        bfs(i, j, num)

#그룹 별 block 갯수
# print(blocks)

    # 조화로움 계산
    candidates = [i for i in range(1, num_of_groups+1)]
    caselist = list(itertools.combinations(candidates,2))
    # print(caselist)
    def score(a, b): #a,b 그룹간의 스코어 계산

        result = (blocks[a] + blocks[b])*value_dic[a]*value_dic[b]*match[a][b]
        # print(f"{blocks[a] + blocks[b]}X{a}X{b}X{match[a][b]}")
        return result
    def get_total_score(caselist):
        answer = 0
        for a, b in caselist:
            answer += score(a,b)
            # print(f"{a,b}, {score(a, b)}")
        return answer

    # print(get_total_score(caselist))
    myanswer += get_total_score(caselist)

def process2():
    temp = [[0]*N for _ in range(N)]
    # 가운데 돌리기
    for i in range(N//2, -1, -1):
        temp[N//2][i] = grid[i][N//2]
    for i in range(N//2, -1, -1):
        temp[N-1-i][N//2] = grid[N//2][i]

    for i in range(N//2 , N, 1):
        temp[N//2][i] = grid[i][N//2]
    for i in range(N//2 , N, 1):
        temp[N-1-i][N//2] = grid[N//2][i]

    for i in range(N):
        for j in range(N):
            if temp[i][j] !=0:
                grid[i][j] = temp[i][j]
    # print("grid", grid)

    # 사등분해서 rotate 시키기
    def rotate(x, y):
        # print(f'rotate{x,y}')
        m = (N-1)//2
        # print(m)
        temp = [[0]*m for _ in range(m)]

        # 복사
        for i in range(m):
            for j in range(m):
                temp[i][j] = grid[i+x][j+y]

        temp2 = [[0]*m for _ in range(m)]
        #90되 회전시키기
        for i in range(m):
            for j in range(m):
                temp2[j][m-1-i] = temp[i][j]

        # 다시 옮김
        for i in range(m):
            for j in range(m):
                grid[i+x][j+y] = temp2[i][j]



    rotate(0,0)
    rotate(0, (N-1)//2 +1)
    rotate((N-1)//2 +1, 0)
    rotate((N-1)//2 +1,(N-1)//2 +1)
    # print("grid", grid)

myanswer =0
process()
process2()
process()
process2()
process()
process2()
process()
print(myanswer)