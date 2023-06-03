import sys
import collections
sys.stdin = open('input_1456.txt', 'r')

# input
N, M = map(int, input().split())

# make a degree and graph
graph = collections.defaultdict(list)
degree = [0]*(N+1)
for _ in range(M): # O(M)
    a, b= map(int, input().split())
    graph[a].append(b)
    degree[b] +=1

# topological sort
term_table = [0]*(N+1)
q = collections.deque()
for i in range(1, N+1):
    if degree[i] ==0:
        q.append((i, 1))
        term_table[i] = 1

while q: #O(N+M)
    course, term = q.popleft()
    for v in graph[course]:
        degree[v] -=1
        if degree[v] ==0:
            q.append((v, term+1))
            term_table[v] = term+1

for k in range(1, N+1):
    print(term_table[k])
