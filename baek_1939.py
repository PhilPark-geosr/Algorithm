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

global flag

def dfs(v, end, w, limit):
    # print(f"dfs{v, w, visited}")
    global flag
    if v != end and w < limit:
        return
    if v == end:

        if w >=limit:
            flag = True
        return
    visited[v] = 1
    for node, cost in graph[v]:
        new_cost = cost
        if visited[node] ==0:
            dfs(node, end, new_cost, limit)
    #visited[v] = 0
visited = [0] * (N + 1)
#dfs(start, 3, 10**9, 50)
l = 0
r = 10**9
answer =-1
while l<=r:
    mid = (l+r)//2
    flag = False
    visited = [0] * (N + 1)
    dfs(start, end, 10**9, mid)
    if flag ==True:
        answer =mid
        l = mid + 1
    else:
        r = mid -1

print(answer)