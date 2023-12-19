import sys
import collections
import heapq
import math
sys.stdin = open('input_산타의 선물공장.txt', 'r')
input = sys.stdin.readline
q = int(input())
# 벨트
belt = collections.defaultdict(dict)
gift_pos = collections.defaultdict(dict)

def setup(N, M, product):

    # 초기값 세팅
    for i in range(1, N+1):
        belt[i]['first'] =-1
        belt[i]['last'] = -1
        belt[i]['cnt'] = 0

    for i in range(1, M+1):
        if belt[product[i]]['first'] ==-1:
            gift_pos[i]['prev'] =-1
            gift_pos[i]['next'] =-1
            belt[product[i]]['first'] = i
            belt[product[i]]['last'] = i
            
        else:
            prev = belt[product[i]]['last']
            gift_pos[i]['prev'] =prev
            gift_pos[i]['next'] =-1
            gift_pos[prev]['next'] =i
            belt[product[i]]['last'] = i
        
        # 벨트안에 있는 원소 갯수 업데이트
        belt[product[i]]['cnt'] = belt[product[i]].get('cnt', 0) +1 
    # 선물위치 업데이트
    # print('belt', belt)
    # print(len(belt[3]))
    # print('gift_pos', gift_pos)
    return


def trans_all(src, dst): #목적지로 다 옮기기
    # print('200 tranall src, dst', src, dst)
    # src에 데이터 있는지 조회
    # print('src_list', src_list)
    if belt[src].get('cnt', 0) == 0: #아무것도 없으면
        print(belt[dst].get('cnt', 0))
        return
    else: #있으면 다 옮기기
        # 선물위치 업데이트
        # 옮기려는 곳의 맨끝
        src_elem = belt[src]['last'] # 맨끝
        src_first = belt[src]['first'] # 맨앞
        src_cnt = belt[src].get('cnt', 0)

        if belt[dst].get('first', -1) ==-1:
            dst_elem =-1
            #위치 업뎃
            gift_pos[src_elem]['next'] = dst_elem
            belt[src]['first'] = -1
            belt[src]['last'] = -1
            belt[src]['cnt'] = 0

            belt[dst]['first'] = src_first
            belt[dst]['last'] = src_elem
            belt[dst]['cnt'] = belt[dst].get('cnt', 0) + src_cnt
        else:
            dst_elem = belt[dst]['first'] # 맨앞
            # 연결하기
            gift_pos[src_elem]['next'] = dst_elem
            gift_pos[dst_elem]['prev'] = src_elem

            #벨트 업뎃
            belt[src]['first'] = -1
            belt[src]['last'] = -1
            belt[src]['cnt'] = 0

            belt[dst]['first'] = src_first
            belt[dst]['cnt'] = belt[dst].get('cnt', 0) + src_cnt

    
    # print("belt", belt)
    # print('gift_pos', gift_pos)
    # print('belt', belt)
    # dst 선물들 개수 출력
    print(belt[dst].get('cnt', 0))
    return

def trans_first(src, dst):
    # 맨 앞에 있는것들 확인
    src_list = belt[src]
    dst_list = belt[dst]

    if belt[src].get('cnt', 0) !=0 and belt[dst].get('cnt',0) !=0: # 둘다 있는 경우
        # src -> dst
        #위치 바꾸기
        src_elem = belt[src].get('first',-1)
        src_next = gift_pos[src_elem].get('next', -1)

        dst_elem = belt[dst].get('first',-1)
        dst_next = gift_pos[dst_elem].get('next', -1)

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
        if belt[src].get('cnt', 0) ==1 and belt[dst].get('cnt',0) !=1:
            belt[src]['first'] = dst_elem
            belt[src]['last'] = dst_elem
            belt[dst]['first'] = src_elem
        elif belt[src].get('cnt', 0) !=1 and belt[dst].get('cnt',0) ==1:
            belt[src]['first'] = dst_elem
            belt[dst]['first'] = src_elem
            belt[dst]['last'] = src_elem
        elif belt[src].get('cnt', 0) ==1 and belt[dst].get('cnt',0) ==1: #둘다 1인경우
            belt[src]['first'] = dst_elem
            belt[src]['last'] = dst_elem
            belt[dst]['first'] = src_elem
            belt[dst]['last'] = src_elem
        else: #둘다 1보다 큰경우
            belt[src]['first'] = dst_elem
            belt[dst]['first'] = src_elem
           
            

    elif belt[src].get('cnt', 0) !=0 and belt[dst].get('cnt',0) ==0:
        
        elem =belt[src].get('first', -1)
        elem_next = gift_pos[elem].get('next', -1)
        #위치 바꾸기
        gift_pos[elem]['next'] =-1
        gift_pos[elem]['prev'] =-1
        if elem_next != -1:
            gift_pos[elem_next]['prev'] =-1

        # 벨트에 추가
        belt[dst]['first'] = elem
        belt[dst]['last'] = elem
        belt[dst]['cnt'] = belt[dst].get('cnt', 0) +1
        belt[src]['cnt'] = belt[src]['cnt'] -1
        
        belt[src]['first'] = elem_next
        if elem_next ==-1:
            belt[src]['last'] = -1
        
    elif belt[src].get('cnt', 0) ==0 and belt[dst].get('cnt',0) !=0:
        elem =belt[dst].get('first', -1)
        elem_next = gift_pos[elem].get('next', -1)
        #위치 바꾸기
        gift_pos[elem]['next'] =-1
        gift_pos[elem]['prev'] =-1
        if elem_next != -1:
            gift_pos[elem_next]['prev'] =-1


        # 벨트에 추가
        belt[src]['first'] = elem
        belt[src]['last'] = elem
        belt[src]['cnt'] = belt[src].get('cnt', 0) +1

        belt[dst]['first'] = elem_next
        if elem_next ==-1:
            belt[dst]['last'] = -1
        belt[dst]['cnt'] = belt[dst]['cnt'] -1
    else:
        pass
    # print("belt", belt)
    # print("gift_pos", gift_pos)
    # 출력
    print(belt[dst].get('cnt', 0))

def divide(src, dst):
    n = belt[src].get('cnt', 0)
    # 어디까지 옮길건지..
    if n <=1:#벨트에 선물이 1개 이하면 옮기지 않음
        print(belt[dst].get('cnt', 0))
        return 
    limit = math.floor(n/2)

    # 위치 옮기기
    src_first = belt[src]['first']

    # 맨끝 포인터 이동
    src_elem = src_first
    t = math.floor(n/2)
    while t-1>0:
        next = gift_pos[src_elem]['next']
        src_elem = next
        t -=1

    # print("옮겨야될 마지막 번호", src_elem)
   
    # src_elem = belt[src][limit-1] #옮기고자 하는 물체의 맨끝
    src_next = gift_pos[src_elem].get('next', -1)
    # # print('src_elem', src_elem)

    # # 대상이 비어있을 경우 처리
    dst_elem =  belt[dst].get('first', -1) #대상의 맨앞
    # # print('dst_elem', dst_elem)


    # 위치처리
    if dst_elem !=-1: # 옮기고자 하는 곳에 있다면
        gift_pos[src_elem]['next'] = dst_elem
        gift_pos[src_next]['prev'] = -1
        gift_pos[dst_elem]['prev'] = src_elem
        belt[src]['cnt'] = belt[src]['cnt'] - limit 
        belt[src]['first'] = src_next

        belt[dst]['cnt'] = belt[dst].get('cnt', 0) + limit
        belt[dst]['first'] = src_first
    else:
        gift_pos[src_elem]['next'] = dst_elem
        gift_pos[src_next]['prev'] = -1
        belt[src]['cnt'] = belt[src]['cnt'] - limit 
        belt[src]['first'] = src_next

        belt[dst]['cnt'] = belt[dst].get('cnt', 0) + limit
        belt[dst]['first'] = src_first
        belt[dst]['last'] = src_elem

    # 벨트 처리
    
   
    print(belt[dst].get('cnt', 0))

def get_gift_info(num):
    prev = gift_pos[num]['prev']
    next = gift_pos[num]['next']
    print(prev + 2*next)
        
def get_belt_info(num):
    first = belt[num].get('first', -1)
    last = belt[num].get('last', -1)
    cnt = belt[num].get('cnt', 0)
    print(first + 2*last + 3*cnt)


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
    