import collections
import sys
import heapq
sys.stdin = open('input_11779.txt', 'r')
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input()) #정점
M = int(input()) #간선

graph = collections.defaultdict(list)
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    # graph[b].append((a,c))

# 역추적할 경로, 최단 거리 갱신할때 어디서 왔는지 기록
parent = collections.defaultdict(int)

S, E = map(int, input().split()) #출발, 도착

def dijkstra(start):
    q = []
    distance = [float('inf')]*(N+1)
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[node]:
                distance[node] = new_cost
                # 이전노드 기록
                parent[node] = now
                heapq.heappush(q, (new_cost, node))
    return distance

result = dijkstra(S)
# print("result", result)
min_distance = result[E]


# print(parent)

#역추적 시작
path = []
node = E
while node:
    path.append(node)
    node = parent[node]

# print(path)
print(min_distance)
print(len(path))
for i in range(len(path)-1, -1, -1):
    print(path[i], end = " ")