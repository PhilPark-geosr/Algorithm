import sys
import heapq
sys.stdin = open('input_13549.txt', 'r')
input = sys.stdin.readline
start, end = map(int, input().split())

def dijkstra(start):
    distance = [float('inf')]*(100001)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for new_node in [now+1, now-1, 2*now ]:
            if new_node == 2*now:
                new_cost = dist
            else:
                new_cost = dist +1
            if 0<=new_node<=100000 and new_cost < distance[new_node]:
                distance[new_node] = new_cost
                heapq.heappush(q, (new_cost, new_node))

    return distance



result = dijkstra(start)
# print(result[:20])
print(result[end])