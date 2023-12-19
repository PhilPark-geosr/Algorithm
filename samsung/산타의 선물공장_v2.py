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
        if len(belt[product[i]]) ==0:
            gift_pos[i]['prev'] =-1
            gift_pos[i]['next'] =-1
            belt[product[i]].append(i)
        else:
            prev = belt[product[i]][-1]
            gift_pos[i]['prev'] =prev
            gift_pos[i]['next'] =-1
            gift_pos[prev]['next'] =i
            belt[product[i]].append(i)
    # 선물위치 업데이트
    # print('belt', belt)
    # print('gift_pos', gift_pos)
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
        # 선물위치 업데이트
        # 옮기려는 곳의 맨끝
        src_elem = belt[src][-1] # 맨끝

        if len(belt[dst]) ==0:
            dst_elem =-1
            gift_pos[src_elem]['next'] = dst_elem
        else:
            dst_elem = belt[dst][0] # 맨앞
            # 연결하기
            gift_pos[src_elem]['next'] = dst_elem
            gift_pos[dst_elem]['prev'] = src_elem

        # 벨트 옮기기
        n = len(belt)-1
        while belt[src]:
            elem = belt[src].pop()
            belt[dst].appendleft(elem)
            n-=1
        
    # print("belt", belt)
    # print('gift_pos', gift_pos)
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
        src_elem = belt[src][0]
        src_next = gift_pos[src_elem]['next']

        dst_elem = belt[dst][0] 
        dst_next = gift_pos[dst_elem]['next']

        if src_next !=-1 and dst_next !=-1: #둘다 연결관계가 있을때
            # src 옮기기
            gift_pos[src_elem]['next'] = dst_next
            gift_pos[dst_next]['prev'] = src_elem
            
            #dst 옮기기
            gift_pos[dst_elem]['next'] = src_next
            gift_pos[src_next]['prev'] = dst_elem
        elif src_next !=-1 and dst_next ==-1: 
            # src 옮기기
            gift_pos[src_elem]['next'] = dst_next
            # gift_pos[dst_next]['prev'] = src_elem
            
            #dst 옮기기
            gift_pos[dst_elem]['next'] = src_next
            gift_pos[src_next]['prev'] = dst_elem
        elif src_next ==-1 and dst_next !=-1: 
            # src 옮기기
            gift_pos[src_elem]['next'] = dst_next
            gift_pos[dst_next]['prev'] = src_elem
            
            #dst 옮기기
            gift_pos[dst_elem]['next'] = src_next
            # gift_pos[src_next]['prev'] = dst_elem
        else:
            pass #아무것도 안해도됨


        #벨트 업데이트
        belt[src][0], belt[dst][0] = belt[dst][0], belt[src][0]

    elif len(src_list) !=0 and len(dst_list)==0:
        
        elem =belt[src].popleft()
        elem_next = gift_pos[elem]['next']
        #위치 바꾸기
        gift_pos[elem]['next'] =-1
        gift_pos[elem]['prev'] =-1
        if elem_next != -1:
            gift_pos[elem_next]['prev'] =-1

        belt[dst].appendleft(elem)
    elif len(src_list) ==0 and len(dst_list)!=0:

        elem =belt[dst].popleft()
        elem_next = gift_pos[elem]['next']
        #위치 바꾸기
        gift_pos[elem]['next'] =-1
        gift_pos[elem]['prev'] =-1
        if elem_next != -1:
            gift_pos[elem_next]['prev'] =-1
        belt[src].appendleft(elem)
    else:
        pass
    # print("belt", belt)
    # print("gift_pos", gift_pos)
    # 출력
    print(len(belt[dst]))

def divide(src, dst):
    n = len(belt[src])
    # 어디까지 옮길건지..
    if n <=1:#벨트에 선물이 1개 이하면 옮기지 않음
        print(len(belt[dst]))
        return 
    limit = math.floor(n/2)

    # 위치 옮기기
    src_elem = belt[src][limit-1] #옮기고자 하는 물체의 맨끝
    src_next = gift_pos[src_elem]['next']
    # print('src_elem', src_elem)

    # 대상이 비어있을 경우 처리
    if len(belt[dst]) == 0:
        dst_elem =-1
    else:
        dst_elem =  belt[dst][0] #대상의 맨앞
    # print('dst_elem', dst_elem)

    if dst_elem !=-1: # 옮기고자 하는 곳에 있다면
        gift_pos[src_elem]['next'] = dst_elem
        gift_pos[src_next]['prev'] = -1
        gift_pos[dst_elem]['prev'] = src_elem
    else:
        gift_pos[src_elem]['next'] = dst_elem
        gift_pos[src_next]['prev'] = -1

    # print(limit)
    temp = []
    while limit >0:
        elem = belt[src].popleft()
        temp.append(elem)
        # belt[dst].append(elem)
        limit -=1

    # 다 옮기기
    while temp:
        elem = temp.pop()
        belt[dst].appendleft(elem)
    # print("belt", belt)
    # print("gift_pos", gift_pos)
    print(len(belt[dst]))

def get_gift_info(num):
    prev = gift_pos[num]['prev']
    next = gift_pos[num]['next']
    print(prev + 2*next)
        
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
    elif Q[0] == 200:
        #물건 모두 옮기기
        src, dst = Q[1], Q[2]
        trans_all(src, dst)
    elif Q[0] == 300:
        src, dst = Q[1], Q[2]
        trans_first(src, dst)
    elif Q[0] == 400:
        src, dst = Q[1], Q[2]
        divide(src, dst)
        
    elif Q[0] == 500:
        num = Q[1]
        get_gift_info(num)
    else: #Q[0] ==600
        num = Q[1]
        get_belt_info(num)
    