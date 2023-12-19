import collections
import sys
sys.stdin = open('input_13023.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
graph = collections.defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
global answer

def dfs(v, cnt, path):
    # print(f"dfs{v, cnt, result}")
    global answer
    if cnt ==5:
        answer = True
        return

    visited[v] = 1
    for node in graph[v]:
        if visited[node] ==0:
            dfs(node, cnt+1, path+[node])
    visited[v] = 0

answer = False
for v in range(N):
    if answer == True:
        break
    visited = [0]*(N)
    # print("v", v)
    dfs(v, 1, [v])

if answer == True:
    print(1)
else:
    print(0)
# print(answer)