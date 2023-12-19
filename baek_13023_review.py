import sys
import collections
sys.setrecursionlimit(10**9)
sys.stdin = open('input_13023.txt','r')
input = sys.stdin.readline

N, M = map(int, input().split())
graph = collections.defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

global flag

def dfs(v, cnt):
    global flag
    if cnt > 5:
        return
    if cnt == 5:
        flag = True
        return
    visited[v] = 1
    for node in graph[v]:
        if visited[node] == 0:
            dfs(node, cnt+1)
    visited[v] = 0



# 정답
for i in range(N):
    visited = [0]*N
    flag = False
    dfs(i, 1)
    if flag == True:
        break

if flag ==True:
    print(1)
else:
    print(0)



