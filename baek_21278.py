import sys
import heapq
import collections
import itertools
sys.stdin = open('input_21278.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

# 양방향 그래프 생성
graph = collections.defaultdict(list)
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dijkstra(a, b):
    q = []
    distance = [float('inf')]*(N+1)
    
    # 초기화
    distance[a] = 0
    distance[b] = 0
    heapq.heappush(q, (0, a))
    heapq.heappush(q, (0, b))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for node in graph[now]:
            new_cost = dist +1
            if new_cost < distance[node]:
                distance[node] = new_cost
                heapq.heappush(q, (new_cost, node))

    return distance


# 후보들 생성
candidates = [i for i in range(1, N+1)]
case_list = list(itertools.combinations(candidates, 2))
# print(case_list)

answer = float('inf')
answer_a, answer_b = -1, -1

for a, b in case_list:
    result = dijkstra(a,b)
    distance = 2*sum(result[1:])

    if distance < answer:
        answer= distance
        answer_a = a
        answer_b = b

print(answer_a, answer_b, answer)
