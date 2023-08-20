import sys
import heapq
import collections
sys.stdin = open('input_1162.txt', 'r')
input = sys.stdin.readline
#input
N, M, K = map(int, input().split())
graph = collections.defaultdict(list)
for _ in range(M):
    a,b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

#다익스트라 정의
def dijkstra(start):
    dp = [[float('inf')]*(K+1) for _ in range(N+1)]
    # 초기화
    for i in range(K+1):
        dp[1][i] = 0

    q = []
    heapq.heappush(q, (0, start, 0))

    while q:
        # print( dp)
        dist, now, k = heapq.heappop(q)
        if dp[now][k] < dist:
            continue
        for node, cost in graph[now]:
            new_cost = cost + dist # 새로운 비용
            if new_cost < dp[node][k]:
                dp[node][k] = new_cost # 업데이트
                heapq.heappush(q, (new_cost, node, k))
            # 포장 해서 큐에 넣기
            if k < K:
                new_cost = dist
                if new_cost < dp[node][k+1]:
                    dp[node][k+1] = new_cost
                    heapq.heappush(q, (new_cost, node, k+1))
    return dp



   

#결론 도출
start = 1
result = dijkstra(start)
# print(result)
answer = float('inf')
for t in range(K+1):
    if result[N][t] < answer:
        answer = result[N][t]
print(answer)