import sys
sys.stdin= open('input_13164.txt', 'r')
import heapq
# input = sys.stdin.readline

# input
n, k = map(int, input().split())
number_list = list(map(int, input().split()))
# 차이 기록
q = []
for i in range(n-1):
    heapq.heappush(q, number_list[i+1]- number_list[i])
# print(q)

# 작은거 n-k 누적
sum = 0
for _ in range(n-k):
    sum += heapq.heappop(q)

print(sum)