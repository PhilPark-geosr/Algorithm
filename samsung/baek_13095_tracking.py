import sys
import collections
import heapq
sys.stdin = open('input_13095.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
start, end = map(int, input().split())
graph = collections.defaultdict(list)
path = [-1]*(N+1) #경로 추적

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(strat):
    q = []
    distance = [0]*(N+1)
    distance[start] =float('inf')
    heapq.heappush(q, (-float('inf'), start))

    while q:
        dist, now = heapq.heappop(q)

        dist = -dist
        # print("dist, now", dist, now)
        if distance[now] > dist:
            continue

        for node, cost in graph[now]:
            min_dist = min(dist, cost)
            # print(min_dist)
            if min_dist > distance[node]:
                distance[node] = min_dist
                path[node] = now #경로 추적
                heapq.heappush(q, (-min_dist, node))
    return distance



result = dijkstra(start)
print(result[end])
print(path)

node = end
answer = []
while node >0:
    answer.append(node)
    node = path[node]
# 경로 출력
for i in range(len(answer)-1, -1, -1):
    print(answer[i])