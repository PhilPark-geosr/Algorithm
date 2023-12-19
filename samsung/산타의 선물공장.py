import sys
import collections
import heapq
import math
sys.stdin = open('input_산타의 선물공장.txt', 'r')
input = sys.stdin.readline
q = int(input())
# 벨트
belt = collections.defaultdict(collections.deque)
gift_pos = collections.defaultdict(dict)

def setup(N, M, product):
    for i in range(1, M+1):
        belt[product[i]].append(i)
        # 선물 위치업데이트
        # gift_pos[i] = product[i]

    # 선물위치 업데이트
    for belt_num in belt:
        for i, elem in enumerate(belt[belt_num]):
            gift_pos[elem] = {belt_num : i}
    print("belt, gift_pos", belt, gift_pos)
    return

def trans_all(src, dst): #목적지로 다 옮기기
    # print('200 tranall src, dst', src, dst)
    # src에 데이터 있는지 조회
    src_list = belt[src]
    # print('src_list', src_list)
    if len(src_list) ==0: #아무것도 없으면
        print(len(belt[dst]))
        return
    else: #있으면 다 옮기기
        n = len(belt)-1
        while belt[src]:
            elem = belt[src].pop()
            belt[dst].appendleft(elem)
            # 위치 업데이트
            # gift_pos[elem] = dst
            # gift_pos[elem] = {dst : n}
            n-=1
        # 선물 위치 업데이트
        for i, elem in enumerate(belt[dst]):
            gift_pos[elem] = {dst : i}
    print("belt, gift_pos", belt, gift_pos)
    # print('belt', belt)
    # dst 선물들 개수 출력
    print(len(belt[dst]))
    return

def trans_first(src, dst):
    # 맨 앞에 있는것들 확인
    src_list = belt[src]
    dst_list = belt[dst]

    if len(src_list) !=0 and len(dst_list)!=0: # 둘다 있는 경우
        # src -> dst
        #위치 바꾸기
        gift_pos[belt[src][0]] = {dst: 0}
        gift_pos[belt[dst][0]] = {src : 0}
        # gift_pos[belt[src][0]] = dst
        # gift_pos[belt[dst][0]] = src
        #벨트 업데이트
        belt[src][0], belt[dst][0] = belt[dst][0], belt[src][0]

    elif len(src_list) !=0 and len(dst_list)==0:
        
        elem =belt[src].popleft()
        #위치 바꾸기
        gift_pos[elem] = dst
        belt[dst].appendleft(elem)
    elif len(src_list) ==0 and len(dst_list)!=0:
        elem =belt[dst].popleft()
        gift_pos[elem] = src
        belt[src].appendleft(elem)
    else:
        pass
    print("belt, gift_pos", belt)
    # 출력
    print(len(belt[dst]))

def divide(src, dst):
    n = len(belt[src])
    # 어디까지 옮길건지..
    if n <=1:#벨트에 선물이 1개 이하면 옮기지 않음
        print(len(belt[dst]))
        return 
    limit = math.floor(n/2)
    # print(limit)
    temp = []
    while limit >0:
        elem = belt[src].popleft()
        #위치 업데이트
        gift_pos[elem] = dst
        temp.append(elem)
        # belt[dst].append(elem)
        limit -=1

    # 다 옮기기
    while temp:
        elem = temp.pop()
        belt[dst].appendleft(elem)
    print("belt, gift_pos", belt, gift_pos)
    print(len(belt[dst]))

def get_gift_info(num):
    # belt위치 찾기
    belt_num = gift_pos[num]
    # print('선물번호, 벨트번호', num,belt_num)
    idx = belt[belt_num].index(num)
    # print('선물 위치', idx)
    a = -1
    b = -1
    
    if 0< idx < len(belt[belt_num]) -1: # 앞뒤 둘다 있을경우
        a = belt[belt_num][idx -1]
        b = belt[belt_num][idx +1]
    elif idx >0 and idx == len(belt[belt_num]) -1: #앞엔 있고 뒤엔 없을경우
        a = belt[belt_num][idx -1]
        b =-1
    elif idx == 0 and idx < len(belt[belt_num]) -1: #앞엔 없고 뒤엔 있을경우
        a =-1
        b = belt[belt_num][idx +1]
    else:
        pass
    print(a+ 2*b)
        
def get_belt_info(num):
    a =-1
    b =-1
    c = 0
    # belt정보 출력
    # print(belt[num])
    if len(belt[num]) !=0: #맨앞 맨뒤 출력
        a = belt[num][0]
        b = belt[num][-1]
        c = len(belt[num])
    print(a + 2*b + 3*c)


for _ in range(q):
    Q = list(map(int, input().split()))
    if Q[0] == 100:
        N, M = Q[1], Q[2]
        product = [0] + Q[3:]
        # print(product)
        setup(N,M, product)
    # elif Q[0] == 200:
    #     #물건 모두 옮기기
    #     src, dst = Q[1], Q[2]
    #     trans_all(src, dst)
    # elif Q[0] == 300:
    #     src, dst = Q[1], Q[2]
    #     trans_first(src, dst)
    # elif Q[0] == 400:
    #     src, dst = Q[1], Q[2]
    #     divide(src, dst)
        
    # elif Q[0] == 500:
    #     num = Q[1]
    #     get_gift_info(num)
    # else: #Q[0] ==600
    #     num = Q[1]
    #     get_belt_info(num)
    