import collections
import sys
sys.stdin = open('input_1939.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N, M = map(int, input().split())
graph = collections.defaultdict(list)

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

start, end = map(int, input().split())
def bfs(start, limit):
    visited = [0] * (N + 1)
    q = collections.deque()
    q.append((start, 0))
    visited[start]= 1
    while q:
        print(q)
        now, dist = q.popleft()

        for node, cost in graph[now]:
            print('node, cost',node, cost)
            if visited[node] == 0 and cost >=limit:
                visited[node] = 1
                q.append((node, cost))

    #visited[v] = 0
bfs(1, 50)
# dfs(start, 2, 10**9, 0)
# l = 0
# r = 10**9
# answer =-1
# while l<=r:
#     mid = (l+r)//2
#     flag = False
#     visited = [0] * (N + 1)
#     dfs(start, end, 10**9, mid)
#     if flag ==True:
#         answer =mid
#         l = mid + 1
#     else:
#         r = mid -1
#
# print(answer)