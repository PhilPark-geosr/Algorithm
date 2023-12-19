import sys
import collections
import heapq
sys.setrecursionlimit(10**9)
sys.stdin= open('input_싸움땅.txt', 'r')
input = sys.stdin.readline
N, M ,K = map(int, input().split())

grid = [[0]*(N+1)]
for _ in range(N):
    line = [0]+list(map(int, input().split()))
    grid.append(line)

# direction
direction = {
    0 : (-1, 0),
    1 : (0, 1),
    2 : (1, 0),
    3 : (0, -1)
}

# pos_dic
pos = collections.defaultdict(dict)
for i in range(1, N+1):
    for j in range(1, N+1):
        pos[(i,j)]['gun'] = []
        pos[(i,j)]['man'] = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        gun = grid[i][j]
        if gun:
            heapq.heappush(pos[(i,j)]['gun'], -gun)
        
# state_dic
state = collections.defaultdict(dict)
for i in range(1, M+1):
    x,y, d, s = map(int, input().split())
    state[i]['pos'] = (x,y)
    # position 업데이트
    pos[(x,y)]['man'] = i
    state[i]['d'] = d
    state[i]['s'] =s
    state[i]['gun'] = 0
    state[i]['score'] = 0


# print(state)
# print(pos)
def move_up(num):
    x, y = state[num]['pos']
    new_x, new_y = x-1, y
    if new_x < 1:
        new_x = x+1 #반대로 이동
        state[num]['d'] = 2 #방향 바꾸기
    # print(new_x, new_y)
    return new_x, new_y
    
def move_down(num):
    x, y = state[num]['pos']
    new_x, new_y = x+1, y
    if new_x > N:
        new_x = x-1 #반대로 이동
        state[num]['d'] = 0 #방향 바꾸기
    # print(new_x, new_y)
    return new_x, new_y
    
def move_left(num):
    x, y = state[num]['pos']
    new_x, new_y = x, y-1
    if new_y < 1:
        new_y = y+1 #반대로 이동
        state[num]['d'] = 1 #방향 바꾸기
    # print(new_x, new_y)
    return new_x, new_y
    
def move_right(num):
    x, y = state[num]['pos']
    new_x, new_y = x, y+1
    if new_y > N:
        new_y = y-1 #반대로 이동
        state[num]['d'] = 3 #방향 바꾸기
    # print(new_x, new_y)
    return new_x, new_y


def get_next_pos(num):
    dir = state[num]['d']
    # print('방향', dir)
    if dir ==0:
        return move_up(num)
    elif dir ==1:
        return move_right(num)

    elif dir ==2:
        return move_down(num)
    else: #dir ==3:
        return move_left(num)

# 총 얻기
def get_gun(num, org_x, org_y, x, y):
    # print('총 얻을게', i)
    gun_list = pos[(x,y)]['gun']
    # print('gun_list', gun_list)

    if gun_list: # 총이 있을때만 
        if -gun_list[0] > state[i]['gun']: #총 교체
            a = -gun_list[0]
            b = state[i]['gun']
            state[i]['gun'] = a
            heapq.heappop(pos[(x,y)]['gun'])
            if b !=0: #총 가지고 있는 경우만
                heapq.heappush(pos[(x,y)]['gun'], -b)
    
    # 위치 업데이트

    # 원래 위치 없애기
    # print(f"여기서{org_x, org_y} 위치 바꿈, {num} 으로")
    pos[(org_x, org_y)]['man'] = 0
    # print(f"{x,y} 위치 바꿈, {num} 으로")
    pos[(x,y)]['man'] = num
    state[num]['pos'] = (x,y)
    # print(pos[(x,y)])
    # print(state)

def fight(num, org_x, org_y, x, y):

    # print('싸우자, 공격자, 거기 있던 사람', num, pos[(x,y)], )
    # 움직이는 사람 공격력
    attacker = state[num]['s'] + state[num]['gun']
    
    # 그 자리에 있던 사람 
    comp_num = pos[(x,y)]['man']
    # print("두 사람 공격력", num, comp_num, x, y)
    comp = state[comp_num]['s'] + state[comp_num]['gun']
    
    def proceed(num, comp_num, score, org_x, org_y, x,y):


        
        #진 플레이어 총 버리기
        gun = state[comp_num]['gun']
        if gun !=0:
            heapq.heappush(pos[(x,y)]['gun'], -gun) #총 삽입
        state[comp_num]['gun'] = 0 #총 없어짐

        # 이긴 플레이어 총 획득하기
        get_gun(num, org_x, org_y, x, y)

        # 진 플레이어 이동시도
        dir = state[comp_num]['d']
        new_x, new_y, new_dir = get_next_lose_player(x,y, dir)
        # print('움직이는 곳',comp_num, new_x, new_y, new_dir)

        # 점수 업데이트
        state[num]['score'] += score
        
        

        # 방향 업데이트
        state[comp_num]['d']= new_dir
        # 이동

        if len(pos[(new_x, new_y)]['gun']) !=0: #총이 있는 경우
            get_gun(comp_num, state[comp_num]['pos'][0],state[comp_num]['pos'][1], new_x, new_y)
        else:
            just_move(comp_num, state[comp_num]['pos'][0],state[comp_num]['pos'][1],new_x, new_y)

        # 이긴 애들 위치 이동
        pos[(state[num]['pos'][0],state[num]['pos'][1])]['man'] = 0
        state[num]['pos'] = (x,y)
        # print(f'이긴애들위치이동{x,y, num}')
        pos[(x,y)]['man'] = num
        # print(f'이긴애들위치이동{x,y, num}')
        


    # 공격력 비교
    if attacker > comp: #공격자가 높으면
        num, comp_num = num, comp_num
        score = attacker - comp 

        org_x, org_y = state[num]['pos']
        x, y = x,y
        proceed(num, comp_num, score, org_x, org_y, x,y)
        # # 점수 상승
        # state[num]['score'] += score
        # # 이긴 플레이어 위치 이동
        # state[num]['pos'] = (x,y) 
        # pos[(x,y)]['man'] = num

        # #진 플레이어 총 버리기
        # gun = state[comp_num]['gun']
        # heapq.heappush(pos[(x,y)]['gun'], -gun) #총 삽입
        # state[comp_num]['gun'] = 0 #총 없어짐

        # # 진 플레이어 이동시도
        # dir = state[comp_num]['d']
        # new_x, new_y, new_dir = get_next_lose_player(x,y, dir)
        # print('움직이는 곳', new_x, new_y, new_dir)

        # # 방향 업데이트
        # state[comp_num]['d']= new_dir
        # # 이동

        # if len(pos[(new_x, new_y)]['gun']) !=0: #총이 있는 경우
        #     get_gun(comp_num, new_x, new_y)
        # else:
        #     just_move(comp_num, x,y)

    elif attacker == comp: #두 공격력이 같으면
        s_attack = state[num]['s']
        s_comp = state[comp_num]['s']

        if s_attack > s_comp: #공격자가 초기 공격력이 높으면
            num, comp_num = num, comp_num
            score = attacker - comp 
            org_x, org_y = state[num]['pos']
            x, y = x,y
            proceed(num, comp_num, score, org_x, org_y, x,y)
            # # 점수 상승
            # state[num]['score'] += score
            # # 이긴 플레이어 위치 이동
            # state[num]['pos'] = (x,y) 
            # pos[(x,y)]['man'] = num

            # #진 플레이어 총 버리기
            # gun = state[comp_num]['gun']
            # heapq.heappush(pos[(x,y)]['gun'], -gun) #총 삽입
            # state[comp_num]['gun'] = 0 #총 없어짐

            # # 진 플레이어 이동시도
            # dir = state[comp_num]['d']
            # new_x, new_y, new_dir = get_next_lose_player(x,y, dir)
            # print('움직이는 곳', new_x, new_y, new_dir)

            # # 방향 업데이트
            # state[comp_num]['d']= new_dir
            # # 이동

            # if len(pos[(new_x, new_y)]['gun']) !=0: #총이 있는 경우
            #     get_gun(comp_num, new_x, new_y)
            # else:
            #     just_move(comp_num, new_x, new_y)


        else: #s_attack < s_comp
            num, comp_num = comp_num, num
            score = comp - attacker 
            org_x, org_y = state[num]['pos']
            x, y = x,y
            proceed(num, comp_num, score, org_x, org_y, x,y)
            # proceed(num, comp_num, score)
            # # 점수 상승
            # state[num]['score'] += score
            # # 이긴 플레이어 위치 이동
            # state[num]['pos'] = (x,y) 
            # pos[(x,y)]['man'] = num

            # #진 플레이어 총 버리기
            # gun = state[comp_num]['gun']
            # heapq.heappush(pos[(x,y)]['gun'], -gun) #총 삽입
            # state[comp_num]['gun'] = 0 #총 없어짐

            # # 진 플레이어 이동시도
            # dir = state[comp_num]['d']
            # new_x, new_y, new_dir = get_next_lose_player(x,y, dir)
            # print('움직이는 곳', new_x, new_y, new_dir)

            # # 방향 업데이트
            # state[comp_num]['d']= new_dir
            # # 이동

            # if len(pos[(new_x, new_y)]['gun']) !=0: #총이 있는 경우
            #     get_gun(comp_num, new_x, new_y)
            # else:
            #     just_move(comp_num, new_x, new_y)

    else : # comp > attacker
        num, comp_num = comp_num, num
        score = comp - attacker 

        org_x, org_y = state[num]['pos']
        x, y = x,y
        proceed(num, comp_num, score, org_x, org_y, x,y)
        # # 점수 상승
        # state[num]['score'] += score
        # # 이긴 플레이어 위치 이동
        # state[num]['pos'] = (x,y) 
        # pos[(x,y)]['man'] = num

        # #진 플레이어 총 버리기
        # gun = state[comp_num]['gun']
        # heapq.heappush(pos[(x,y)]['gun'], -gun) #총 삽입
        # state[comp_num]['gun'] = 0 #총 없어짐

        # # 진 플레이어 이동시도
        # dir = state[comp_num]['d']
        # new_x, new_y, new_dir = get_next_lose_player(x,y, dir)
        # print('움직이는 곳', new_x, new_y, new_dir)

        # # 방향 업데이트
        # state[comp_num]['d']= new_dir
        # # 이동

        # if len(pos[(new_x, new_y)]['gun']) !=0: #총이 있는 경우
        #     get_gun(comp_num, new_x, new_y)
        # else:
        #     just_move(comp_num, new_x, new_y)


def get_next_lose_player(x,y, dir):
    # print('x,y,dir', x,y,dir)
    base_dir = dir
    new_x, new_y = x + direction[dir][0], y +direction[dir][1]
    if 1<=new_x<=N and 1<=new_y<=N and  pos[(new_x, new_y)]['man'] ==0:
        return new_x, new_y, dir

    n = 0
    while (new_x > N or new_x <1 or new_y >  N or new_y <1) or (pos[(new_x, new_y)]['man'] !=0):
        if n>=3:
            break
        # print("new_x, new_y", new_x, new_y)
        if dir ==3:
            dir = 0
        else:
            dir +=1
        n+=1
        new_x, new_y = x + direction[dir][0], y +direction[dir][1]
        if 1<=new_x<=N and 1<=new_y<=N and  pos[(new_x, new_y)]['man'] ==0:
            return new_x, new_y, dir
    # print("n", n)
    if n ==3:
        return x,y, base_dir
    
        
        


# 그냥 이동할때
def just_move(num, org_x, org_y, x,y):
    # print(f"org{org_x, org_y} 위치 바꿈, {num} 으로")
    pos[(org_x, org_y)]['man'] = 0
    #위치 업데이트
    state[num]['pos'] = (x,y)
    # print(f"{x,y} 위치 바꿈, {num} 으로")
    pos[(x,y)]['man'] = num

# print(state)
# print(pos)
for _ in range(K):
    for i in range(1, M+1):
        # print(f'-------------------------{i}-----------------------',)
        # print(pos)
        org_x, org_y = state[i]['pos']
        new_x, new_y = get_next_pos(i)
        
        if len(pos[(new_x,new_y)]['gun']) !=0 and pos[(new_x,new_y)]['man'] ==0: #총 있고, 사람 없으면
            # print('총 획득', i,org_x, org_y, new_x,new_y)
            get_gun(i, org_x, org_y, new_x, new_y)
        elif len(pos[(new_x,new_y)]['gun']) !=0 and pos[(new_x,new_y)]['man'] !=0: #총 있고 사람 있으면
            # print('싸우자', i, org_x, org_y,new_x,new_y)
            fight(i,org_x, org_y, new_x, new_y)
        elif len(pos[(new_x,new_y)]['gun']) ==0 and pos[(new_x,new_y)]['man'] !=0: # 총 없고 사람 있으면
            # print('싸우자', i, org_x, org_y, new_x,new_y)
            fight(i, org_x, org_y, new_x, new_y)
        else:
            # print('그냥 움직여', i, org_x, org_y, new_x,new_y)
            just_move(i, org_x, org_y, new_x, new_y)


        # for i in range(1, M+1):
        #     x, y = state[i]['pos']
        #     pos[(x,y)]['man'] =i
        # print(state)
        # print(pos)
    # 다하고 점수출력
print(state)
for i in range(1, M+1):
    print(state[i]['score'], end  = " ")
