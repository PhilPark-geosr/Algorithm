import sys
import collections
import heapq

sys.stdin = open('input_2412.txt','r')
input = sys.stdin.readline
N, T = map(int, input().split())
pos = dict()
pos[0] = (0, 0)
check_dic = dict()

# 위치와 번호기록
for i in range(1, N + 1):
    a, b = map(int, input().split())
    pos[i] = (a, b)
    check_dic[(a, b)] = i


def dijkstra(start):
    distance = [float('inf')] * (N + 1)
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        a, b = pos[now]
        if distance[now] < dist:
            continue

        ##
        for i in range(-2, 3):
            for j in range(-2, 3):
                new_a, new_b = a + i, b + j
                if (new_a, new_b) not in check_dic:
                    continue  # 범위 밖에 있으면 탐색 안함
                new_cost = dist + 1
                node = check_dic[(new_a, new_b)]
                if new_cost < distance[node]:
                    distance[node] = new_cost
                    heapq.heappush(q, (new_cost, node))

    return distance


result = dijkstra(0)

answer = float('inf')
for i in range(len(result)):
    if pos[i][1] == T:
        answer = min(answer, result[i])

if answer == float('inf'):
    print(-1)
else:
    print(answer)

