import sys
import heapq

sys.stdin = open('input_1202.txt','r')
input = sys.stdin.readline
N, K = map(int, input().split())

jem_list = []
for _ in range(N):
    w,v = map(int, input().split())
    heapq.heappush(jem_list, (w, v))
    
bag_list = []
for _ in range(K):
    c = int(input())
    bag_list.append(c)

# 가방 작은순으로 정렬
bag_list.sort()
# print("jem_list, bag_list", jem_list, bag_list)

total_value = 0
cand = [] #담을수 있는 애들 리스트
for bag in bag_list:

    while jem_list:
        if jem_list[0][0] <= bag: #담을 수 있는 애들이면..
            w, v = heapq.heappop(jem_list)
            heapq.heappush(cand, (-v, w))
        else:
            break

    # 담을 수 있는 애들 중에 가장 가치가 큰 것 담기
    if cand:
        v, _ = heapq.heappop(cand)
        total_value += -v

print(total_value)