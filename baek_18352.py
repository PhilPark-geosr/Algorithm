import sys
import collections
import heapq

sys.stdin = open("input_18352.txt", "r")
N, M, K, X = map(int, input().split())

# make a graph, heap
graph = collections.defaultdict(list)
for _ in range(M):
    a, b= map(int, input().split())
    graph[a].append((b,1))

# dijkstra
def dijkstra(start): ## O(MlogN)
    distance = [float('inf')]*(N+1)
    q = []

    distance[start] =0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: #이미 처리 되었으면.
            continue
        # 그렇지 않으면 처리
        for elem in graph[now]: #인접 노드 방문
            node, cost = elem
            new_cost = cost + dist # dist: start ~ now까지 최소비용
            if new_cost < distance[node]: #거쳐가는 비용이 작으면 갱신, 아니면 원래 게 나음
                distance[node] = new_cost
                heapq.heappush(q, (new_cost, node))
    return distance

# find k distance
result = dijkstra(X)
flag = False
for i in range(1, N+1): #O(N)
    if result[i] ==K:
        flag = True
        print(i)

if flag == False:
    print(-1)