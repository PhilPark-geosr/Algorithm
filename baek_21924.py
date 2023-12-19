import sys
import heapq
sys.stdin = open('input_21924.txt', 'r')
input = sys.stdin.readline



def find(x):
    if parent[x] == x:#자기 사진이 부모노드이면
        return x
    else:
        y = find(parent[x]) #계속 부모를 찾아라
        # 찾았으면
        parent[x] = y #기록해두고
        return y

def union(a,b):
    a, b = find(a), find(b)
    if a <b:
        parent[b] = a
    else:
        parent[a] = b


N,M = map(int, input().split())

parent = [i for i in range(N+1)]
q = []
for _ in range(M):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, a, b))

answer = 0 # 최소비용
total_cost = 0
while q:
    # print(q)
    dist, a, b = heapq.heappop(q)

    if find(a) == find(b): #사이클 발생
        total_cost += dist
        continue
    union(a,b)
    answer += dist
    total_cost += dist


print(total_cost - answer)