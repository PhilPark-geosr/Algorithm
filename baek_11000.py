import sys
import heapq
sys.stdin = open('input_11000.txt', 'r')

n = int(input())

#make q1
q1 = []
q2 = []

for _ in range(n):
    a,b = map(int, input().split())
    heapq.heappush(q1, (a,b)) #start, end

# 시간초과풀이
# cnt = 0
# while q1:
#     # print(q1, q2)
#     S, T = heapq.heappop(q1)

#     while q1:
#         new_S, new_T = heapq.heappop(q1)
#         # print((S,T), (new_S, new_T))
#         if new_S < T:
#             heapq.heappush(q2, (new_S, new_T))
#         else:
#             S, T = new_S, new_T
    
#     cnt +=1
#     q1 = q2
#     q2 = []

# 끝나는 시간 푸쉬
q2 = []
_, T = heapq.heappop(q1)
heapq.heappush(q2, T)

while q1:
    # print(q1, q2)
    S, T = heapq.heappop(q1)
    if S >= q2[0]:
        heapq.heappop(q2)
        heapq.heappush(q2, T)
    else:
        heapq.heappush(q2, T)

print(len(q2))