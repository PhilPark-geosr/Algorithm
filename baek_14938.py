import sys
import collections
import heapq
sys.stdin = open('input_14938.txt', 'r')

n, m, r = map(int, input().split())

items = list(map(int, input().split()))

items.insert(0,0)

graph = collections.defaultdict(list)
for _ in range(r):
    a,b,c =map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a, c))


def dijkstra(start):
    q = []
    distance = [float('inf')]*(n+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

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

answer = 0
for i in range(1, n+1):
    sum_value = 0
    result = dijkstra(i)
    # print(result)
    for j in range(1, n+1):
        if result[j] <= m:
            sum_value += items[j]
    # print('sum_value', sum_value)
    # 답 갱신
    answer = max(answer, sum_value)

print(answer)
