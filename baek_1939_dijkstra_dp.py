import sys
sys.stdin = open('input_1939.txt', 'r')
import collections
import heapq
# input
N, M = map(int, input().split())
graph = collections.defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

start, end = map(int, input().split())
# 그래프 들어오는 것 중 큰 값 처리(그래프만들기)

# 다익스트라 정의
def dijkstra(start):
    dp = [-1]*(N+1) # i까지 오는데 가장 작은 옮길수 있는 무게 중 최대
    # 초기화
    dp[start] =10**9
    q = []
    heapq.heappush(q, (-10**9, start))
    while q:
        # print("q, dp", q, dp) # 확인
        dist, now = heapq.heappop(q)
        dist = -dist #양음 바꿈
        if dp[now] > dist: # 이미 처리 되었으면
            continue
        for node, cost in graph[now]:
            new_cost = min(dist, cost) #둘중 작은 걸로
            if new_cost > dp[node]: # 새로운 무게가 더 크면 갱신
                dp[node] = new_cost
                heapq.heappush(q, (-new_cost, node))
    return dp


# 결과값 처리
result = dijkstra(start)
# print("result", result)
print(result[end])