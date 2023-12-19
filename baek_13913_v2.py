from collections import deque
import collections
import sys
sys.stdin = open('input_13913.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())  #출발 / 도착
dist = [0] * 100001  # 최대 0부터 100000까지의 지점까지 걸리는 횟수 기록
visited = [0]*(100001)
visited[N] =1
dist[N] = 0
parents = collections.defaultdict(int)  # 경로 추적

# BFS 탐색
queue = deque()
queue.append((N, 0))  # 시작점

# 큐가 빌 때까지 탐색
while queue:
    x, time = queue.popleft()
    # 도착지점이라면 탐색 종료
    if x == K:
        # print(dist[x])  # 최적 경로
        # path = []
        # for _ in range(dist[x]+1):
        #     path.append(x)
        #     x = parents[x]
        # print(" ".join(map(str, path[::-1])))
        break

    # x에서 -1 또는 +1 또는 *2 탐색
    for nextX in (x+1, x-1, 2*x):
        # 0~100000지점 내이고, 방문하지 않았거나 동일한 탐색횟수를 가졌으면 탐색
        if 0 <= nextX <= 100000 and visited[nextX]==0:
            visited[nextX] = 1
            dist[nextX] = time+ 1  # 방문하고 횟수 1늘림
            parents[nextX] = x
            queue.append((nextX, time+ 1))  # 큐에 추가

print(dist[K])
answer = []
node = K
for _ in range(dist[K]+1):
        #     path.append(x)
        #     x = parents[x]
    # print(node)
    answer.append(node)
    node = parents[node]
# print(answer)
for i in range(len(answer)-1, -1, -1):
    print(answer[i], end =" ")