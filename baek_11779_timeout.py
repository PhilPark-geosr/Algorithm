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
                heapq.heappush(q, (new_cost, node))
    return distance

result = dijkstra(S)
# print("result", result)
min_distance = result[E]
# print("min_distance", min_distance)
# dfs

def dfs(v, E , cost, way):
   # print(f'dfs{v,cost, way}')
    if cost > min_distance:
        return
    if v == E: #도착점에 도착했을 경우
        if cost == min_distance:
            route.append(way)
        return
    visited[v] = 1
    for node, new_cost in graph[v]:
        if visited[node] ==0:
            dfs(node, E, cost+new_cost, way + [node])
    visited[v] = 0




# 최소경로추출
route = []
visited = [0]*(N+1)
dfs(S, E, 0,[S])
# print('route', route)



min_length = len(route[0])
print(min_distance)
print(min_length)
for elem in route[0]:
    print(elem, end =" ")
