import sys
import heapq
sys.stdin=open('input_16398.txt', 'r')

input = sys.stdin.readline
N = int(input())




parent = [i for i in range(N)]

def find(x):
    if parent[x] == x:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y
    
def union(a, b):
    a = find(a)
    b = find(b)
    if a< b:
        parent[b] = a
    else:
        parent[a] = b


graph = []
for _ in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

q = []
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        heapq.heappush(q, (graph[i][j], i, j))



answer =0
while q:
    cost, a,b = heapq.heappop(q)
    if find(a) == find(b): #부모가 같으면 싸이클이 발생하므로 제외
        continue

    union(a,b) #둘이 합친다
    answer +=cost


# 정답
print(answer)

