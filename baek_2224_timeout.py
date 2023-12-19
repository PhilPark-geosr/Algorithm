import sys
import heapq
import collections
import itertools
sys.setrecursionlimit(10**8)
sys.stdin = open('input_2224.txt', 'r')

N = int(input()) # 명제의 갯수

node_list = set()
graph = collections.defaultdict(list)
visited = collections.defaultdict(int)

for _ in range(N):
    a, _, b = input().split()
    graph[a].append(b)
    node_list.add(a)
    node_list.add(b)

node_list = sorted(list(node_list)) #정렬
#print("node_list", node_list)


def dfs(v, path):
    # print(f"dfs{v, path}")
    visited[v] = 1
    if len(graph[v]) == 0 and len(path) >1:
        result.add(path)
        return
    for node in graph[v]:
        # if visited[node]==0:
        dfs(node, path + node)


result = set()
for v in node_list:
    if visited[v] ==0:
        dfs(v, v)

# print(result)

q =set()
for elem in result:
    case_list = itertools.combinations(elem, 2)
    for case in case_list:
        q.add(case)

# print(q)
q = sorted(list(q))
print(len(q)) # 가짓수 출력

for x, y in q:
    print(f"{x} => {y}")
# while q:
#     x, y = heapq.heappop(q)




    

