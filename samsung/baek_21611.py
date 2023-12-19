import sys
import collections
sys.stdin = open('input_21611.txt','r')
input = sys.stdin.readline
N, M = map(int, input().split())
grid = [[0]*(N+1)]
for _ in range(N):
    line = [0] + list(map(int, input().split()))
    grid.append(line)

global s_x, s_y #상어위치
s_x, s_y = (N+1)//2, (N+1)//2
# print(grid)
dirs = {
    1: (-1,0),
    2: (1, 0),
    3: (0,-1),
    4: (0, 1)
}

temp = [[0]*(N+1) for _ in range(N+1)] #토네이도 기록
pos = [((N+1)//2,(N+1)//2)]*(N**2)
exploded = {
    1 : 0,
    2 : 0,
    3 : 0
} #폭팔한 갯수

def is_range(x, y):
    if 1<=x<=N and 1<=y<=N:
        return True
    return False
def show_grid(arr):
    for line in arr:
        print(line)
def fill_temp():
    global d, cnt, x, y
    x, y = (N + 1) // 2, (N + 1) // 2  # 초기위치

    l = 1
    d = 0
    cnt = 1
    def go(l):  # l만큼 기록 및 이동
        global d, cnt, x,y
        to_dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        dx, dy = to_dirs[d][0], to_dirs[d][1]
        for k in range(1, l+1):
            new_x, new_y = x+dx, y+dy
            if is_range(new_x, new_y) == False:
                return 0
            temp[new_x][new_y] = cnt
            pos[cnt] = (new_x, new_y)
            cnt+=1
            x, y = new_x, new_y
        d = d+1 if d<3 else 0

    while True:
        for _ in range(2):
            flag = go(l)
            if flag == 0:
                return
        l +=1

#test
# fill_temp()
# show_grid(temp)
# print(pos)

def destroy(d,s):
    global s_x, s_y
    dx, dy = dirs[d][0], dirs[d][1]
    for i in range(1, s+1):
        new_x, new_y = s_x+ i*dx, s_y + i*dy
        if is_range(new_x, new_y) == False:
            break
        grid[new_x][new_y] = 0
    
    # test 출력
    # show_grid(grid)
# test
# destroy(2, 5)

def move(x,y):
    cur_x, cur_y = x, y
    cur_v = grid[x][y] #번호 가져오기
    num = temp[x][y] # x,y 위치의 번호
    if cur_v == 0:
        return #번호가 0이면 아예 안움직인다

    while True:
        new_num = num-1
        if new_num == 0: #상어위치 가면 스탑
            return
        new_x, new_y = pos[new_num]
        if grid[new_x][new_y] !=0:
            return #갈수 없을때

        # 값 바꿔주기
        grid[new_x][new_y] = cur_v
        grid[cur_x][cur_y] = 0

        cur_x, cur_y = new_x, new_y
        num = new_num

def shift():
    # 모든 칸 번호에 대해서 검사
    for i in range(1, N**2):
        x, y = pos[i]
        if grid[x][y] !=0:
            move(x,y)
    # print()
    # show_grid(grid)
#test
# fill_temp()
# shift()

def remove(arr):
    temp_x, temp_y = arr[0][0], arr[0][1]
    num = grid[temp_x][temp_y]

    # 깬것 체크
    exploded[num] = exploded[num] + len(arr)
    for x,y in arr:
        grid[x][y] = 0

def explode():
    cur_num = 1
    cur_x, cur_y = pos[cur_num] #1번위치부터 시작
    cnt = 1
    remove_list = []

    check = 0
    while True:
        remove_list.append((cur_x, cur_y)) #제거 리스트에 추가
        new_num = cur_num +1
        # print(cur_x, cur_y)
        if new_num >= N**2:
            break
        new_x, new_y = pos[new_num]
        # print('현재 좌표', (cur_x, cur_y))
        if grid[new_x][new_y] == grid[cur_x][cur_y]:
            cnt+=1
            cur_x, cur_y = new_x, new_y
            cur_num = new_num
        else:
            cur_x, cur_y = new_x, new_y
            cur_num = new_num
            # print(cnt)
            if cnt >=4:
                # print(remove_list)
                remove(remove_list)
                check +=1
            remove_list = []
            cnt = 1
    # print()
    # show_grid(grid)
    #아무런 변화 없다면
    if check == 0:
        return False
    return True
    #출력
    


# test
# fill_temp()
# destroy(2,2)
# shift()
# explode()
# shift()

def rebuild():
    cur_num = 1
    cur_x, cur_y = pos[cur_num]  # 1번위치부터 시작
    cnt = 1
    result = collections.deque()
    while True:
        new_num = cur_num + 1
        if new_num >= N ** 2:
            break
        new_x, new_y = pos[new_num]
        # print('현재 좌표', (cur_x, cur_y))
        if grid[new_x][new_y] == grid[cur_x][cur_y]:
            cnt += 1
            cur_x, cur_y = new_x, new_y
            cur_num = new_num
        else:
            result.append((cnt, grid[cur_x][cur_y]))
            cur_x, cur_y = new_x, new_y
            cur_num = new_num
            cnt = 1

    # print(result)
    # 순회하며 다시 기록
    new_grid = [[0]*(N+1) for _ in range(N+1)]
    count_num = 1
    while count_num < N**2 and result:
        num_of_value, value = result.popleft()
        cur_x, cur_y = pos[count_num]
        new_grid[cur_x][cur_y] = num_of_value
        count_num +=1
        cur_x, cur_y = pos[count_num]
        new_grid[cur_x][cur_y] = value
        count_num +=1

    # 복사
    for i in range(1, N+1):
        for j in range(1, N+1):
            grid[i][j] = new_grid[i][j]
    # print()
    # show_grid(grid)





def blizard(d,s):
    destroy(d,s)
    shift()

    while True:
        if explode() == False: #더이상 폭파될게 없을경우
            break
        shift() #폭파되었으면 이동
    return
# ----------------- main ------------------#
fill_temp() # 토네이도 채우기
for _ in range(M):
    d, s = map(int, input().split())
    blizard(d,s) #블리자드 마법 수행
    rebuild() #다시 구슬 배치


#정답 출력
# print(exploded)
answer = 1*exploded[1] + 2*exploded[2] + 3*exploded[3]
print(answer)