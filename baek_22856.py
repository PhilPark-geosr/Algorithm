import sys
import collections
sys.stdin = open('input_22856.txt', 'r')
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
N = int(input())
graph = collections.defaultdict()
for _ in range(N):
    a, b, c = map(int, input().split())
    graph[a] = (b,c)

# print(graph)

visited = collections.defaultdict(int)

result = []
global cnt
cnt = 0
def dfs(v):
    global cnt
    # print(f"dfs{v}")
    if v ==-1:
        return
    visited[v] = 1
    # print(v)
    left, right = graph[v][0], graph[v][1]
    if left != -1 and right !=-1:
        cnt +=1
        dfs(left)
        cnt+=1
        # print(v)
        result.append(v)
        cnt += 1
        dfs(right)
        if len(visited) !=N:
            cnt += 1
        # print(v)
    elif left == -1 and right !=-1:
        cnt += 1
        dfs(right)
        result.append(v)
    elif left !=-1 and right ==-1:
        cnt += 1
        dfs(left)
        result.append(v)
    else:
        # cnt += 1
        dfs(left)
        result.append(v)

if N == 1:
    print(0)
else:
    dfs(1)
    # print(result)
    print(cnt)