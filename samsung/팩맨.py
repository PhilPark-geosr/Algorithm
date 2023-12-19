import sys
sys.stdin = open('팩맨.txt', 'r')
input = sys.stdin.readline

m, t = map(int, input().split())
global pack_x, pack_y
global time #현재 시간
global num_of_eat
global lived #살아남은 애들
num_of_eat = 0 #먹은 수
time = 0 #시간 초기화
pack_x, pack_y = map(int, input().split())
grid = [ [[] for _ in range(5)] for _ in range(5)] # 몬스터위치
dead = [ [[] for _ in range(5)] for _ in range(5)] # 시체 위치
baby = [ [[] for _ in range(5)] for _ in range(5)] # 알의 위치
dirs = [(0,0), (-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)]
for _ in range(m):
    x,y,d = map(int, input().split())
    grid[x][y].append(d)

def copy():
    for i in range(1, 5):
        for j in range(1, 5):
            if len(grid[i][j]) >0: #몬스터들 있으면
                make_baby(i,j)
def make_baby(x,y):
    monsters = grid[x][y]
    for d in monsters:
        baby[x][y].append(d) # 같은 방향을 같는 알을 낳음

def move_monster():
    temp = [[[] for _ in range(5)] for _ in range(5)]  # 임시 저장소

    def move(x, y):
        monsters = grid[x][y]
       # print(f"{x,y} 에 있는 걸 처리하겠습니다", monsters)
        for d in monsters:
            # 각 몬스터마다 8번 돈다
            flag = False  # 처리되었는지 체크
            new_d = d  # 임시 저장
            for _ in range(8):
                new_x, new_y = x + dirs[new_d][0], y + dirs[new_d][1]
                if is_range(new_x, new_y) == False:
                    new_d = new_d +1 if new_d < 8 else 1
                    continue
                if is_dead(new_x, new_y) == True or is_pack(new_x, new_y) == True:  # 팩맨이 있거나, 시체가 있거나, 범위를 벗어나는 경우
                    new_d = new_d +1 if new_d < 8 else 1 # 방향 45도 바꾸기
                    continue
                else:  # 움직일 수 있는 경우
                    flag = True  # 처리되었음을 표시
                    temp[new_x][new_y].append(new_d)
                    break
            # 처리 안된 애들 담기
            if flag == False:
                temp[x][y].append(d)  # 움직이지 않는다
        # 다 처리하고 나서 다시 담아주기

        
    # 이동시켜라
    for i in range(1, 5):
        for j in range(1, 5):
            if len(grid[i][j]) >0: #몬스터들이 있으면
                move(i,j) #몬스터들 이동시켜라
    # 정보 복사
    for i in range(1, 5):
        for j in range(1,5):
            grid[i][j] = temp[i][j]

#판단하는 함수
def is_pack(x,y):
    global pack_x, pack_y
    if (x,y) == (pack_x, pack_y):
        return True
    else:
        return False
def is_dead(x,y):
    if len(dead[x][y]) >0: #시체가 한마리라도 있으면
        return True
    else:
        return False
def is_range(x,y):
    if 1<=x<=4 and 1<=y<=4:
        return True
    else:
        return False
# # 카피 진행
# copy()
# # print('grid', grid)
# # print('baby', baby)
# # 몬스터 이동
# move_monster()
# # print('grid', grid)
# # print('baby', baby)

# 팩맨 이동경로 만들기
caselist =[]
pack_dirs = [(-1,0), (0,-1), (1,0), (0,1)]
def dfs(v, result):
    if v == 3:
        caselist.append(result)
        return
    dfs(v+1, result +[0])
    dfs(v + 1, result + [1])
    dfs(v + 1, result + [2])
    dfs(v + 1, result + [3])
dfs(0,[])
# print(caselist)

def is_monster(x,y):
    if len(grid[x][y])>0:
        return True
    return False

def delete_monster(x,y):
    global time
    dead[x][y].append(time) #몇초에 죽었는지 추가
    grid[x][y] = []

def eat(answer_case):
    # print('answer_case', answer_case)
    global pack_x, pack_y
    for d in answer_case:
        new_x, new_y = pack_x + pack_dirs[d][0], pack_y + pack_dirs[d][1]
        if is_monster(new_x, new_y) ==True:
            delete_monster(new_x, new_y) # 해당 칸의 몬스터를 다 지우기
        # 팩맨 위치 이동
        pack_x, pack_y = new_x, new_y

def test_eat(case):
    global pack_x, pack_y
    #temp = #이전에 있던 grid정보 다 복사한다
    temp = [ [[] for _ in range(5)] for _ in range(5)]
    for i in range(1,5):
        for j in range(1,5):
            temp[i][j] = grid[i][j].copy()
    org_x, org_y = pack_x, pack_y # 위치 정보 받아온다

    def delete_test(x,y):
        monsters = temp[x][y]
        num = len(monsters)
        temp[x][y] = []
        return num

    cnt = 0 #먹을 수 있는 갯수
    for d in case:# 모든 방향으로 가보면서 탐색
        new_x, new_y = org_x + pack_dirs[d][0], org_y + pack_dirs[d][1]
        if is_range(new_x, new_y) == False: #범위 밖으로 벗어나면
            return -1 #바로 -1리턴
        # 벗어나지 않으면 먹어본다
        if is_monster(new_x, new_y) == True:
            cnt += delete_test(new_x, new_y) #몬스터 갯수 추가
        # 성공했으면 좌표 이동
        org_x, org_y = new_x, new_y
    return cnt

def move_pack():
    global num_of_eat
    max_value = -1 #최대 먹은 몬스터 수
    answer_case = []# 그때의 정답 케이스
    # 최대 먹은 몬스터 케이스 찾기
    for case in caselist:
        cnt = test_eat(case)
        if cnt ==-1: # 이동중간에 범위 벗어남
            continue
        if cnt > max_value:
            # print('case', case, cnt)
            max_value = cnt
            answer_case = case
    # 실제로 먹기
    # print('먹은갯수', max_value)
    eat(answer_case)
    num_of_eat += max_value
# 팩맨 이동해보기
# move_pack()
# print('pack_x, pack_y', pack_x, pack_y)
# print('grid', grid)
# print('baby', baby)
# print('dead', dead)
# print("num_of_eat", num_of_eat)

# 죽은애들 갱신
def delete_dead():
    for i in range(1, 5):
        for j in range(1, 5):
            if len(dead[i][j]) >0:
                del_dead(i,j)
def del_dead(x,y):
    global time
    dead_list = dead[x][y]
    new = []
    for dead_time in dead_list:
        if time - dead_time <2 :# 2보다 작은애들만 살려놓는다
            new.append(dead_time)
    # 다시 담는다
    dead[x][y] = new

#5. 부화
def birth():
    for i in range(1, 5):
        for j in range(1, 5):
            if len(baby[i][j]) > 0:
                create(i, j)
def create(x,y):
    monsters = baby[x][y]
    for d in monsters:
        grid[x][y].append(d) #다 옮겨담는다
    # 초기화
    baby[x][y] = []

def check_lived():
    global lived
    lived = 0 #초기화
    for i in range(1, 5):
        for j in range(1, 5):
            if len(grid[i][j]) > 0:
                lived += len(grid[i][j])

lived = m
for _ in range(t): #턴만큼 수행
    # 카피 진행
    copy()
    # print('grid', grid)
    # print('baby', baby)
    # 몬스터 이동
    move_monster()
    # print('grid', grid)
    # print('baby', baby)
    # 팩맨 이동해보기
    move_pack()
    # 죽은애들 갱신
    delete_dead()
    # 애기들 탄생
    birth()
    # print("grid", grid)
    # print('pack_x, pack_y', pack_x, pack_y)
    # print('dead', dead)
    check_lived() #살아남은 애들 체크
    time +=1
# 결과 출력
print(lived)