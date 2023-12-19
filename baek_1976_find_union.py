import sys
sys.stdin = open('input_1976.txt', 'r')
input = sys.stdin.readline

# input
N = int(input())
M = int(input())
graph = []
for _ in range(N):
    line = list(map(int, input().split()))
    graph.append(line)
check_list = list(map(int, input().split()))

# parent
parent = [i for i in range(N)]
def find(x):
    if parent[x] ==x:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y
    
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(graph):

    # union 수행
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:
                continue
            if find(i) == find(j):
                continue
            union(i,j)

    flag = parent[check_list[0]-1]
    for i in range(1, M):
        
        if parent[check_list[i]-1] != flag:
            return 'NO'
    return "YES"
    

print(solution(graph))
