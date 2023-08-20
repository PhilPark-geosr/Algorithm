import sys
sys.stdin = open('input_1005.txt', 'r')
# input = sys.stdin.readline 
T = int(input()) #테스트 케이스 갯수


import collections

def topology_sort(n, cost: list, degree: list, graph) : # node 갯수, 비용 테이블
    # dp , dp[i] : i번째 건물을 건설하는 데 드는 비용의 최소
    # print('graph', graph)
    # print('cost', cost)
    # 진입차수 0인거 넣고 시작
    q = collections.deque()
    for i in range(1, n+1):
        if degree[i] ==0:
            q.append(i)
    dp = cost.copy()
    # print(dp)
    # 큐 순회하며 기록
    while q:
        now = q.popleft()
        # print('now', now)
        for k in range(len(graph[now])):
            # 진입차수 감소
            degree[graph[now][k]] -=1

            # 비용 갱신
            dp[graph[now][k]] = max(dp[graph[now][k]], dp[now] + cost[graph[now][k]] )
            if degree[graph[now][k]] ==0:
                q.append(graph[now][k])

    return dp



for _ in range(T):
    N, K = map(int, input().split())

    # 비용 테이블 
    cost = list(map(int, input().split()))
    cost.insert(0,0)
    # degree # 진입차수
    degree = [0]*(N+1)

    graph = collections.defaultdict(list)
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        degree[b] +=1

    answer = topology_sort(N, cost, degree, graph)
    des = int(input())
    print(answer[des])
