import sys
import collections
import heapq
sys.stdin = open('input_1600.txt', 'r')

K = int(input())
W, H = map(int, input().split())

grid = []
for _ in range(H):
    line = list(map(int, input().split()))
    grid.append(line)

h_dirs = [(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)]
m_dirs = [(-1,0), (0,1), (1,0), (0,-1)]

def is_range(x,y):
    if 0<=x<H and 0<=y<W:
        return True
    return False
def dijkstra(start_x, start_y):
    distance = [[[float('inf') for _ in range(K+1)] for _ in range(W)]for _ in range(H)]
    q = []
    for i in range(K+1):
        distance[start_x][start_y][i] = 0

    heapq.heappush(q, (0, start_x, start_y, 0))

    while q:
        # print(q)
        dist, x, y, k = heapq.heappop(q)
        # print(x, y)
        if distance[x][y][k] < dist:
            continue

        # 원숭이 처리
        for h in range(4):
            new_x, new_y = x + m_dirs[h][0], y + m_dirs[h][1]
            if is_range(new_x, new_y) == True and grid[new_x][new_y] == 0:
                new_cost = dist +1
                if new_cost < distance[new_x][new_y][k]:
                    distance[new_x][new_y][k] = new_cost
                    heapq.heappush(q, (new_cost, new_x, new_y, k))

        #말 처리
        if k < K:
            for h in range(8):
                new_x, new_y = x + h_dirs[h][0], y + h_dirs[h][1]
                if is_range(new_x, new_y) == True and grid[new_x][new_y] == 0:
                    new_cost = dist + 1
                    if new_cost < distance[new_x][new_y][k+1]:
                        distance[new_x][new_y][k+1] = new_cost
                        heapq.heappush(q, (new_cost, new_x, new_y, k+1))
    return distance


result = dijkstra(0,0)


answer = float('inf')
for k in range(K+1):
    answer = min(answer, result[H-1][W-1][k])


if answer == float('inf'):
    print(-1)
else:
    print(answer)

