import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input_2668.txt', 'r')
input = sys.stdin.readline
N = int(input())
graph = dict()
for i in range(1, N+1):
    a = int(input())
    graph[i] = a

# print('graph', graph)

def dfs(v, start, route):
    # print(f"dfs{v, start}")
    if visited[v] >=2:# 중복방문 # 무한루프 방지
        return
    if v == start and visited[v] ==1: #사이클 발생
        answer.extend(route)
        return
    else:
        visited[v] +=1
        dfs(graph[v], start, route + [graph[v]])

answer = []
for i in range(1, N+1):
    visited = [0]*(N+1)
    dfs(i, i, [])

answer = set(answer)
answer = list(answer)
answer.sort()
# print(answer)

print(len(answer))
for elem in answer:
    print(elem)