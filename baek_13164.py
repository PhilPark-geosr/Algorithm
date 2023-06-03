import sys
import heapq
sys.stdin  =open('input_13164.txt', 'r')

N, K = map(int, input().split())
height_list = list(map(int, input().split()))

# 우선순위 큐 선언
q = []
for i in range(len(height_list)-1):
    diff = height_list[i+1] - height_list[i]
    # print(diff)
    heapq.heappush(q, diff)

answer = 0
for _ in range((N-1)-(K-1)):
    elem = heapq.heappop(q)
    answer += elem

print(answer)


