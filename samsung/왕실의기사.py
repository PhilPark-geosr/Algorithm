import sys
import collections
sys.stdin = open('왕실의기사.txt', 'r')
input = sys.stdin.readline

L,N,Q = map(int, input().split())
grid = [[0]*(L+1)]
for _ in range(L):
    line = [0] + list(map(int, input().split()))
    grid.append(line)
# print('grid', grid)

dirs = [(-1,0), (0,1), (1,0), (0,-1)]
org = collections.defaultdict(list) #초기 상태
robots =collections.defaultdict(list)

for i in range(1, N+1):
    r,c, h,w, k= map(int, input().split())
    robots[i] = [r,c,h,w,k]
    org[i] = [r, c, h, w, k]
# print('robots', robots)


def is_range(x,y):
    if 1<=x<=L and 1<=y<=L:
        return True
    return False
def is_in_arr(r, c, h, w): #범위에 있는지
    for i in range(r, r+h):
        for j in range(c, c+w):
            if is_range(i, j) == False:
                return False
    return True
def can_go(r,c,h,w): #로봇안에 벽있는지 체크
    for i in range(r, r+h):
        for j in range(c, c+w):
            if grid[i][j] == 2: #벽이 하나라도 있으면
                # print('벽이 있어서 안됩니다')
                return False
    return True

def is_effected(new_r, new_c, new_h, new_w, i):
    r, c, h, w, k  = robots[i]
    if k <=0: #이미 죽은 애들일때
        return False
    # 아니면 체크해본다
    for x in range(new_r, new_r + new_h):
        for y in range(new_c, new_c + new_w):
            if r <= x <= r+h-1 and c <= y <= c+w -1: #하나라도 안에 들어가면
                return True
    return False

def move(i,d):
    r,c,h,w,k = robots[i]
    new_r, new_c = r + dirs[d][0], c + dirs[d][1]

    #점수 깎기
    cnt = 0
    for x in range(new_r, new_r + h):
        for y in range(new_c, new_c + w):
            if grid[x][y] ==1: #함정이면
                cnt +=1

    k -= cnt #점수깎기
    robots[i]= [new_r, new_c, h, w, k]
def just_move(i,d): #그냥옮기는 애들
    r, c, h, w, k = robots[i]
    new_r, new_c = r + dirs[d][0], c + dirs[d][1]
    robots[i] = [new_r, new_c, h, w, k]


def process(i,d):
    global flag
    def dfs(i,d):
        global flag
        # print(f"dfs{i,d}")
        r, c, h, w, k= robots[i]
        new_r, new_c = r + dirs[d][0], c + dirs[d][1]
        if is_in_arr(new_r, new_c, h,w) == False:
            flag = False
            return
        if can_go(new_r, new_c, h, w) ==False:
            flag = False
            return
        # 다 통과한 경우면
        for k in range(1, N+1):
            if k ==i:
                continue #자기 자신 제외
            if is_effected(new_r, new_c, h, w, k) == True:
                case_list.append(k) #케이스리스트에 넣는다
                dfs(k,d)

    r,c,h,w,k = robots[i]
    if k <=0 : #생명력 꺼진애들은 할 필요 없음
        return

    flag = True
    case_list = []

    dfs(i,d)
    # print('영향받는 애들', case_list, flag)
    if flag ==False: #하나라도 못가면
        # print('하나라도 못가기 때문에 종료합니다')
        return

    for num in case_list: #갈수 있는 애들은 이제 옮겨주자
        move(num, d)
    # 자기 자신도 옮긴다
    just_move(i,d)



# process(1, 2)
# print('robots', robots)
# process(2,1)
# print('robots', robots)

def get_score():
    # 체력 0보다 큰애들만 확인
    answer = 0
    for i in range(1,N+1):
        r, c,h,w,k = robots[i]
        if k <=0:
            continue
        answer += org[i][4] - k
    return answer


for _ in range(Q):
    i, d = map(int, input().split())
    process(i,d)

print(get_score())
#최종상태

