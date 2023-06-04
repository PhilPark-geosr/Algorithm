import sys
import collections
import heapq
sys.stdin = open('input_1162.txt', 'r')

N, M, K = map(int, input().split())
roads = []
for _ in range(M):
    a, b, c = map(int, input().split())
    roads.append([c, a,b])

# 큰 순으로 정렬
roads.sort(reverse=True)
# print(roads)

# for i in range(K):
#     roads[i][0] =0
# print(roads)
# graph 만들기
graph = collections.defaultdict(list)
for cost, a, b in roads:
    graph[a].append((cost, b))
    graph[b].append((cost, a))

def dijkstra(start):
    # 거리 테이블, 우선순위 큐 생성
    distance = [10**6]*(N+1)
    q = []
    # 거리 테이블, 우선순위 큐 초기화
    distance[start] =0
    heapq.heappush(q, (0, start))
    cnt = 0
    while q:

        dist, now = heapq.heappop(q)
        
        
        if distance[now] < dist: #이미 처리되었으면
            continue
       
        for cost, node in graph[now]: # 인접한 그래프연산
            
            new_cost = dist + cost
            if new_cost < distance[node]:
                distance[node] = new_cost
                heapq.heappush(q, (new_cost, node))
    return distance

result = dijkstra(1)
answer = result[N]

print(result)
print(answer)


    
