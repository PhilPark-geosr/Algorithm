import sys
import heapq
import collections
sys.stdin = open('input_7662.txt', 'r')
input = sys.stdin.readline


T = int(input())
for _ in range(T):

    N= int(input())
    check_dic = collections.defaultdict(int) # 지웠던 애들 체크
    max_heap = []
    min_heap = []
    for i in range(1, N+1):
        # print('check_dic', check_dic)
        # print('max_heap, min_heap', max_heap, min_heap)
        category, value = list(input().split())
        # print(category, value)
        # print("check_dic",check_dic)
        if category == "I": #삽입
            value = int(value)
            # 최소힙엔 그대로
            heapq.heappush(min_heap, (value, i))
            heapq.heappush(max_heap, (-value, -i))

        else:
            

            if int(value) ==1: #최대힙 삭제
                
                while max_heap and check_dic[(-max_heap[0][0], -max_heap[0][1])] == 1:
                    heapq.heappop(max_heap)

                if len(max_heap) ==0:
                    continue
                
                del_value, idx = heapq.heappop(max_heap)
                check_dic[(-del_value, -idx)] =1

                
            else: #최소힙 삭제
                while min_heap and check_dic[(min_heap[0][0], min_heap[0][1])] == 1:
                    heapq.heappop(min_heap)

                if len(min_heap) ==0:
                    continue                
                del_value, idx = heapq.heappop(min_heap)
                check_dic[(del_value, idx)] =1


    # 다 한후 max_heap, min_heap 비교
    # print("max_heap", max_heap)
    # print("min_heap", min_heap)

    # max_heap에서의 최댓값

    # 중복된값 일단 다 제거하자
    while max_heap and check_dic[(-max_heap[0][0], -max_heap[0][1])] == 1:
        heapq.heappop(max_heap)
        
    while min_heap and check_dic[(min_heap[0][0], min_heap[0][1])] == 1:
        heapq.heappop(min_heap)

    if max_heap and min_heap:

        max_value = -max_heap[0][0]

        # min_heap에서의 최솟값
        min_value = min_heap[0][0]

        print(max_value, min_value)
    else:
        print('EMPTY')