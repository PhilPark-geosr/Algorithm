import sys
import collections
import heapq
sys.stdin = open('input_1162.txt', 'r')

N, M, K = map(int, input().split())

graph = collections.defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))


def dijkstra(start):
    # 거리 테이블, 우선순위 큐 생성
    distance = [[float('inf')]*(N+1) for _ in range(K+1)]
    # /print(distance)
    ## distance[i][k] 도로포장을 k개했을때 i번째로 가는 최소비용 
    q = []
    # 거리 테이블, 우선순위 큐 초기화
    distance[0][start] = 0
    cnt = 0
    heapq.heappush(q, (0, start, cnt))
    while q:
        dist, now, cnt = heapq.heappop(q)
        if distance[cnt][now] < dist: #이미 처리되었으면
            continue
       
        for cost, node in graph[now]: # 인접한 그래프연산
            
            new_cost = dist + cost
            # 같은cnt 내에서 처리 (즉, 도로포장 안했을 때)
            if new_cost < distance[cnt][node]: 
                distance[cnt][node] = new_cost
                heapq.heappush(q, (new_cost, node, cnt))

            # 도로 포장 했을때
            if cnt < K and dist < distance[cnt+1][node]: # 지금 연결된 노드를 도로포장 했을때
                distance[cnt+1][node] = dist
                heapq.heappush(q, (dist, node, cnt+1))
        
    return distance

result = dijkstra(1)
answer = float('inf')
for i in range(K+1):
    if result[i][N] < answer:
        answer = result[i][N]


# print(result)
print(answer)


    
