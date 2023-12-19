import sys
import itertools
import heapq
import math
sys.stdin = open('input_1774.txt', 'r')
N,M = map(int, input().split())
parent = [i for i in range(N+1)]

def find(x):
    if parent[x] == x:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] =b

def get_distance(x1,y1,x2,y2):

    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
arr = [(0,0)]*(N+1)

for i in range(1, N+1):
    x,y = map(int, input().split())
    arr[i] = (x,y)




candidates = [i for i in range(1, N+1)]
case_list = list(map(list, itertools.combinations(candidates, 2)))
q = []
for case in case_list:
    x1,y1 = arr[case[0]]
    x2,y2 = arr[case[1]]
    distance = get_distance(x1,y1,x2,y2)
    heapq.heappush(q, (distance, case[0], case[1]))

# print("q", q)

# 이미 연결되어 있는 애들 연결하자

for _ in range(M):
    a, b = map(int, input().split())
    x1,y1 = arr[a]
    x2,y2 = arr[b]
    distance = get_distance(x1,y1,x2,y2)
    union(a, b) #둘이 합침
     # answer += distance

# 나머지 연결
answer = 0
while q:
    cost, a,b = heapq.heappop(q)
    if find(a) == find(b):
        continue
    union(a,b)
    answer += cost
# print(f'{n:.3f}')
print(f'{answer:.2f}')

