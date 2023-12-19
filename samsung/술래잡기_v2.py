import sys
sys.stdin = open('술래잡기.txt', 'r')
# sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, h, k = map(int, input().split()) #격자, 도망자 수 , 나무 수, 턴 수
dirs = [(-1,0), (0,1), (1,0), (0,-1)]
q = []
trees = [[0]*(n+1) for _ in range(n+1)] #나무위치 기록
global score #점수 기록
score = 0
# 초기 도망자 정보 입력
for _ in range(m):
    x,y,direction = map(int, input().split())
    q.append((x,y, direction))
# print("q", q)
# 트리 위치 기록
for _ in range(h):
    x, y = map(int, input().split())
    trees[x][y] = 1
# 술래 위치
#TODO: 술래위치 업데이트 로직
global seeker_x, seeker_y, seeker_d
seeker_x, seeker_y = (n+1)//2, (n+1)//2
seeker_d = 0
# 거리 구하는 함수
def distance(x,y, seeker_x, seeker_y):
    return abs(x-seeker_x) + abs(y-seeker_y)
# 다음 갈곳 구하는 함수

def is_range(x, y):
    if 1<=x<=n and 1<=y<=n:
        return True
    else:
        return False
def get_next(x,y,d):
    # 바라보고 있는 칸으로 이동
    new_x, new_y = x + dirs[d][0], y+dirs[d][1]
    # print('new_x, new_y',x, y, new_x, new_y, d)
    if is_range(new_x, new_y) ==True: # 범위 내에 있으면
        # print('범위내에 있습니다', x,y)
        if (new_x, new_y) == (seeker_x, seeker_y):#술래가 있는 경우
            return x,y, d #움직이지 않고 리턴
        else:
            return new_x, new_y, d #움직임
    else: #범위 안에 없으면
        if d == 1: #오른쪽 -> 왼쪽
            new_d = 3
        elif d== 3: #왼쪽 -> 오른쪽
            new_d = 1
        elif d == 0: #위쪽 -> 아래쪽
            new_d = 2
        else: #아래 -> 위
            new_d = 0
        temp_x, temp_y = x + dirs[new_d][0], y + dirs[new_d][1] #새로운 좌표
        if (temp_x, temp_y) == (seeker_x, seeker_y):
            return x, y, new_d #방향만 바꿔주고 리턴
        else: #술래가 없을때
            return temp_x, temp_y, new_d


def move(q):
    new_q = []
    for x, y, d in q:
        # print(distance(x,y, seeker_x, seeker_y))
        if distance(x,y, seeker_x, seeker_y) <=3:
            # print('처리합니다')
            new_x, new_y, new_d = get_next(x,y,d)
            # print(new_x, new_y, new_d)
            new_q.append((new_x, new_y, new_d))
        else:
            new_q.append((x,y,d))
    return new_q

board = [[0] * (n+1) for _ in range(n+1)]
board2 = [[0] * (n+1) for _ in range(n+1)]
forward_dic = dict() #다음 방향 좌표 알려주는
def init_grid():
    x,y = int((n+1 )// 2), int((n+1) // 2)  # 배열의 중앙 좌표
    # print('초기', x,y)
    d = 0
    dist = 1
    #초기세팅
    forward_dic[0] = (x,y,d)
    value = 1
    while True:
        # 두번씩 움직인다
        for _ in range(2):
            # 거리만큼 간다
            for _ in range(dist):
                new_x, new_y = x + dirs[d][0], y+ dirs[d][1] #이동
                # print(new_x, new_y)
                if is_range(new_x, new_y) == False: #밖 벗어나면 종료
                    return
                # 아니면 기록
                board[new_x][new_y] = value
                forward_dic[value] = (new_x, new_y, d) #기록
                value +=1
                x,y = new_x, new_y
            # 끝까지 갔으면 방향 전환
            d = (d+1)%4
            forward_dic[value-1] = (new_x, new_y, d)  # 기록
        # 다 갔으면 거리 증가
        dist +=1
reverse_dic = dict()
def init_revsere_grid():
    x,y = 1,1  # 배열의 중앙 좌표
    # print('초기', x,y)
    d = 2
    dist = n-1
    #초기세팅
    reverse_dic[0] = (x,y,d)
    value = 1
    while True:
        if dist ==-1:
            return
        # 두번씩 움직인다
        if dist == n-1:
            for _ in range(3):
                # 거리만큼 간다
                for _ in range(dist):
                    new_x, new_y = x + dirs[d][0], y+ dirs[d][1] #이동
                    # print(new_x, new_y)
                    # 아니면 기록
                    board2[new_x][new_y] = value
                    reverse_dic[value] = (new_x, new_y, d) #기록
                    value +=1
                    x,y = new_x, new_y
                # 끝까지 갔으면 방향 전환
                d = d-1 if d>0 else 3
                reverse_dic[value-1] = (new_x, new_y, d)  # 기록
        else:
            for _ in range(2):
                # 거리만큼 간다
                for _ in range(dist):
                    new_x, new_y = x + dirs[d][0], y+ dirs[d][1] #이동
                    # print(new_x, new_y)
                    # 아니면 기록
                    board2[new_x][new_y] = value
                    reverse_dic[value] = (new_x, new_y, d) #기록
                    value +=1
                    x,y = new_x, new_y
                # 끝까지 갔으면 방향 전환
                d = d-1 if d>0 else 3
                reverse_dic[value-1] = (new_x, new_y, d)  # 기록
        # 다 갔으면 거리 증가
        dist -=1
init_grid()
# print(board)
# print(forward_dic)
init_revsere_grid()
# print(board2)
# print(reverse_dic)
def seeker_move(k, q):
    global seeker_x, seeker_y,seeker_d
    global score  # 점수 기록
    # 다음 포지션과 방향 구하기
    div, mod = divmod(k, n**2-1)
    if div%2 ==1:
        new_num = mod
        seeker_x, seeker_y, seeker_d = reverse_dic[new_num]
    else:
        new_num = mod
        seeker_x, seeker_y, seeker_d = forward_dic[new_num]
    # print(f'{k}초 후 seeker_x, seeker_y, seeker_d', seeker_x, seeker_y, seeker_d)

    #방향대로 잡기
    # 세칸 만들기
    caselist = [(seeker_x, seeker_y), (seeker_x + dirs[seeker_d][0], seeker_y + dirs[seeker_d][1]),\
                (seeker_x + 2*dirs[seeker_d][0], seeker_y + 2*dirs[seeker_d][1])]
    new_q = [] #살아 남는놈 담는 배열

    dead = 0 #죽은자 수
    for x, y, d in q:
        if (x,y) in caselist: # 사정거리 안에 있음
            if trees[x][y] ==1: #트리에 가려질경우
                new_q.append((x,y,d))
            else:
                dead +=1  # 죽은자 수
                continue
        else: #사정거리 안에 없음
            new_q.append((x,y,d))

    # 점수 구하기
    # print('몇명 잡음', dead)
    score += k*dead

    return new_q
# print('pos_dic', pos_dic)
for i in range(1, k+1):

    q = move(q)
    # print(q)
    q = seeker_move(i,q)
    # print('술래방향', seeker_d)
    # print(f'{i} seeker_pos', (seeker_x, seeker_y))
    # print('술재잡고 난 q', q)
    # print("score", score)
print(score)

