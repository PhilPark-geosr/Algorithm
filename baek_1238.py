import sys
import collections
import heapq
sys.stdin = open('input_1238.txt', 'r')

N, M, X = map(int, input().split())

# make a graph 
graph = collections.defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# dijkstra 
def dijkstra(start):
    # initialize distance table
    distance = [float('inf')]*(N+1)
    distance[start] = 0
    # intialize q
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 처리된 노드라면
            continue

        for elem in graph[now]:
            node, cost = elem
            new_cost = dist+ cost
            if new_cost < distance[node]:
                distance[node] =new_cost
                heapq.heappush(q, (new_cost, node))
    return distance

# work
distance_x = dijkstra(X)

answer = 0
for i in range(1, N+1):
    if i == X:
        continue
    result = dijkstra(i)
    if result[X] + distance_x[i] > answer:
        answer = result[X] + distance_x[i]

print(answer)


