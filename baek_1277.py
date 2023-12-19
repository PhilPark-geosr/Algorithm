import sys
import collections
import heapq
import math
sys.stdin = open('input_1277.txt', 'r')
input = sys.stdin.readline


pos = dict()
connected = dict()
N, W = map(int, input().split())
M = float(input())
# print(M)
for i in range(1, N+1):
    a, b = map(int, input().split())
    pos[i] = (a,b)
    
#이미 연결되어있는 애들
for _ in range(W):
    a,b = map(int, input().split())
    connected[(a, b)] = True
    connected[(b, a)] = True

#print(connected)
def can_go(now, M):
    x, y = pos[now]
    can_go_list = []
    for i in range(1, N+1):
        if i == now: #자기자신이면 스킵
            continue
        x2, y2 = pos[i]
        dist = math.sqrt((x-x2)**2 + (y-y2)**2)
        if dist <= M:
            can_go_list.append((i, dist))
        if (now, i) in connected:
            can_go_list.append((i, dist))
    return can_go_list



def dijkstra(start):
    distance = [float('inf')]*(N+1)
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        go_list = can_go(now, M) # M기준으로 갈수 있는곳 추리기
        #print(go_list)

        for node, cost in go_list:
            if (node,now) in connected or (now, node) in connected:
                new_cost = dist
            else:
                new_cost = dist + cost

            if new_cost < distance[node]:
                distance[node] = new_cost
                heapq.heappush(q, (new_cost, node))

    return distance


# ---------------- main ----------------- #
result = dijkstra(1)
# print(result)
print(int(result[N]*1000))