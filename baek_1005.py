import sys 
import collections
sys.stdin = open("input_1005.txt", "r")
# define functionality
def topology_sort(_graph, _degree, _cost, target):
    
    q = collections.deque()
    n = len(_degree)-1
    dp = [0]*(n+1) #dp[i] : i번째까지 가는데 걸린 최대 시간
    
    for i in range(1, n+1):
        if _degree[i] ==0:
            q.append(i)
            dp[i] = _cost[i]
   
    while q:
        # print(_degree)
        # print(q)
        if _degree[target] ==0: #갈수 있으면 멈춤
            break
        now =  q.popleft()
        # print("now", now)
        
        for node in _graph[now]:
            _degree[node] -=1
            dp[node] = max(dp[node], dp[now] + _cost[node]) 
            if _degree[node] ==0:
                q.append(node)
            
        
       
    return dp[target]
        

T = int(input()) # 테스트 케이스 개수
for _ in range(T):
    N, K = map(int, input().split())
    # make a cost
    cost = list(map(int, input().split()))
    cost.insert(0,0)

    # make a graph and degree
    degree = [0]*(N+1)
    graph = collections.defaultdict(list)
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        degree[b]+=1
    # target
    W = int(input())
    result = topology_sort(graph, degree, cost, W)
    print(result)
    # print("-------------------------------")

        