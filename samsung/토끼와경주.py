import sys
import heapq
import collections
sys.stdin = open('input_토끼와경주.txt', 'r')
input = sys.stdin.readline

q = []
score_dic = collections.defaultdict(int) 
dist_dic = collections.defaultdict(int)
pos_dic = dict()


def setup(rabbits, P):

    for i in range(0, 2*P, 2):
        heapq.heappush(q, (0, 2, 1,1, rabbits[i]))
        dist_dic[rabbits[i]] = rabbits[i+1]
        score_dic[rabbits[i]] = 0
        pos_dic[rabbits[i]] = (1,1)
    # print("q, score_dic, dist_dic")
    # print(q, score_dic, dist_dic)

def move_right(x,y,d):
    new_x = x + d
    if new_x > N:
        new_x = N
        d -= N-x
    else:
        d = 0

    return new_x, y, d

def move_left(x,y,d):
    new_x = x - d
    if new_x < 1:
        new_x = 1
        d -= x-1
    else:
        d = 0

    return new_x, y, d

def move_down(x,y,d):
    new_y = y + d
    if new_y > M:
        new_y = M
        d -= M-y
    else:
        d = 0

    return x, new_y, d

def move_up(x,y,d):
    new_y = y - d
    if new_y < 1:
        new_y = 1
        d -= y-1
    else:
        d = 0

    return x, new_y, d

def get_move_list(x, y, pid, N, M):
    d = dist_dic[pid]
    move_list = []
    
    dx = d%(2*(N-1))
    dy = d%(2*(M-1))
    #네방향 기록
    # 오른쪽
    new_x, new_y, d = move_right(x,y, dx)
    new_x, new_y, d = move_left(new_x,new_y, d)
    new_x, new_y, d = move_right(new_x,new_y, d)
    move_list.append((new_x + new_y, new_x, new_y))

    # 왼쪽
    new_x, new_y, d = move_left(x,y, dx)
    new_x, new_y, d = move_right(new_x,new_y, d)
    new_x, new_y, d = move_left(new_x,new_y, d)
    move_list.append((new_x + new_y, new_x, new_y))

    new_x, new_y, d = move_up(x,y, dy)
    new_x, new_y, d = move_down(new_x,new_y, d)
    new_x, new_y, d = move_up(new_x,new_y, d)
    move_list.append((new_x + new_y, new_x, new_y))

    new_x, new_y, d = move_down(x,y, dy)
    new_x, new_y, d = move_up(new_x,new_y, d)
    new_x, new_y, d = move_down(new_x,new_y, d)
    move_list.append((new_x + new_y, new_x, new_y))


    move_list.sort(key = lambda x: (-x[0], -x[1], -x[2]))
    return move_list
        
def proceed(K,S):
    score_q = set() #점수획득할 수 있는 후보들
    for _ in range(K):
        # print("q, score_dic, dist_dic")
        # print(q, score_dic, dist_dic)
        cnt, rc, r,c, pid = heapq.heappop(q)
        move_list = get_move_list(r,c, pid, N, M)
        # print(move_list)
        _, new_r, new_c = move_list[0]
        # print(new_r, new_c)

        # 위치 입력
        heapq.heappush(q, (cnt+1, new_r+new_c, new_r, new_c, pid))
        # 위치 업데이트
        pos_dic[pid] = (new_r, new_c)
        score_q.add(pid) # 뽑혔던 애들만 추가

        # heapq.heappush(score_q, (-(new_r+new_c), -new_r, -new_c, -pid))
        # 점수갱신
        for key in score_dic:
            if key == pid:
                continue
            score_dic[key]+=(new_r+new_c)
        
    # K 번 종료되고 난후

    # 뽑혔던 애들 상대로 추출
    candidates = []
    for pid in score_q:
        r, c = pos_dic[pid]
        candidates.append((r+c, r, c, pid))

    candidates.sort(key= lambda x : (-x[0], -x[1], -x[2], -x[3]))
    # print("candidates", candidates)
    _, _, _, pid = candidates[0]
    score_dic[pid] += S
    
# 점수 바꾸는 로직
def change_distance(pid, L):
    dist_dic[pid] *= L

# 최고점수 출력
def get_highest_score():
    max_value = 0
    for pid in score_dic:
        max_value = max(max_value, score_dic[pid])
    return max_value

qs = int(input())
for _ in range(qs):
    Q = list(map(int, input().split()))
    if Q[0] == 100:
        N, M, P = Q[1], Q[2], Q[3]
        # grid 생성
        # grid = [[0]*(M+1) for _ in range(N+1)]
        rabbits = Q[4:]
        setup(rabbits, P)

    elif Q[0] == 200:
        K, S = Q[1], Q[2]
        proceed(K,S)
    elif Q[0] == 300:
        pid, L = Q[1], Q[2]
        change_distance(pid, L)
    else: #Q[0] == 400:
        answer = get_highest_score()
        print(answer)
