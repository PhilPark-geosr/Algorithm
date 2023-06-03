import sys
import heapq
sys.stdin = open('input_19598.txt','r')

N = int(input())

# 회의실 시작시간 빠른 순으로
conf_list = []
for _ in range(N):
    a, b = map(int, input().split())
    heapq.heappush(conf_list, (a, b))

q = [] #종료시간 담는 배열

# initialize q
_, T = heapq.heappop(conf_list)
heapq.heappush(q, T)

while conf_list:
    S, T = heapq.heappop(conf_list)
    if S >= q[0]:
        heapq.heappop(q) # 교체
        heapq.heappush(q, T)
    else:
        heapq.heappush(q, T)

print(len(q))