import sys
import heapq
import collections
sys.stdin = open('input_22865.txt', 'r')
input = sys.stdin.readline

N = int(input())
A, B, C = map(int, input().split())
M = int(input())

graph = collections.defaultdict(list)

for _ in range(M):
    D,E,L = map(int, input().split())
    graph[D].append((E, L))
    graph[E].append((D, L))

def dijkstra(start):
    q = []
    distance = [float('inf')]*(N+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # print(dist, now)
        if dist > distance[now]:
            continue
        for node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[node]:
                distance[node] = new_cost
                heapq.heappush(q, (new_cost, node))

    return distance

case_A = dijkstra(A)
case_B = dijkstra(B)
case_C = dijkstra(C)

answer_node = 0
answer = 0

for i in range(1, N+1):
    dist = min(case_A[i], case_B[i], case_C[i])
    if dist > answer:
        answer = dist
        answer_node = i

#정답 출력
print(answer_node)