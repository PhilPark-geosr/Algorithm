import sys
import collections
import heapq
sys.stdin = open('input_2109.txt', 'r')
#input = sys.stdin.readline
N = int(input())
request_list = []

for _ in range(N):
    p, d = map(int, input().split())
    request_list.append((d,p))
request_list.sort(reverse=True)
q = collections.deque(request_list)
# print(q)

total_value = 0
temp = []
for day in range(10**4, 0, -1):
    
    while q:
        if day <= q[0][0]:
            d, p = q.popleft()
            heapq.heappush(temp, -p)
        else:
            break
    # print('day, temp', day, temp)
    # 그날중 가장 큰거 고르기
    if temp:
        v = heapq.heappop(temp)
        total_value+=-v

print(total_value)
