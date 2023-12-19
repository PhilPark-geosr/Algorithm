import sys
import collections
import heapq
sys.stdin = open('input_1766.txt','r')
N, M =map(int, input().split())

# 그래프 만들기
indegree = [0]*(N+1)
graph = collections.defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    indegree[b] +=1
    graph[a].append(b)

def topology_sort():
    q = []
    # 초기값 설정
    for i in range(1, N+1):
        if indegree[i] == 0:
            heapq.heappush(q, i)

    result = []
    while q:
        now = heapq.heappop(q)
        result.append(now) #결과 추가
        for node in graph[now]:
            indegree[node] -=1
            if indegree[node] == 0:
                heapq.heappush(q, node)
    return result




answer = topology_sort()
for elem in answer:
    print(elem, end = " ")