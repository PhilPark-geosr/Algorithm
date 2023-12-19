import sys
import collections
sys.stdin = open('input_2056.txt', 'r')
input = sys.stdin.readline

N = int(input())
graph = collections.defaultdict(list)
time = [0 for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
for i in range(1, N+1):
    Q = list(map(int, input().split()))
    time[i] = Q[0] #걸리는 시간
    num_of_conn = Q[1] #연결되어 있는 애들 갯수
    for elem in Q[2:]:
        graph[elem].append(i)
        indegree[i] +=1

#
# print(graph)
# print(indegree)
# print(time)

# 위상정렬 수행
q = collections.deque()
dp = [0 for _ in range(N+1)]
for i in range(1, N+1):
    dp[i] = time[i]
    if indegree[i] ==0:
        q.append(i)

# print(q)


while q:
    now = q.popleft()
    for node in graph[now]:
        indegree[node] -=1

        dp[node] = max(dp[node], dp[now] + time[node])

        if indegree[node] ==0 :
            q.append(node)


# print(dp)

print(max(dp))





