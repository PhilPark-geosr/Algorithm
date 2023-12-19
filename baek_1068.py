import sys
import collections
sys.setrecursionlimit(10**9)
sys.stdin = open('input_1068.txt', 'r')
N = int(input())
parent = list(map(int, input().split()))
target = int(input()) #제거대상
global cnt #리프노드의 갯수

graph = collections.defaultdict(list)
root = -1
# 그래프 생성
for i in range(N):
    if parent[i] == -1:
        root = i
        continue
    graph[parent[i]].append(i)

# print('graph', graph)

def dfs(v):
    global cnt
    if v == target:
        return
    if len(graph[v]) == 0:
        cnt +=1
        return
    if len(graph[v]) == 1 and target in graph[v]:
        cnt +=1
        return
    for node in graph[v]:
        dfs(node)


#결과 출력
cnt = 0
dfs(root)
print(cnt)