import sys
import heapq
sys.stdin = open('input_14621.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

sex = ["empty"] + list(input().split())
# print(sex)

q = []
for _ in range(M):
    a, b, c = map(int, input().split())
    if sex[a] == sex[b]:
        continue
    heapq.heappush(q, (c, a, b))

# find union
parent = [i for i in range(N+1)]

def find(x):
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] =b

answer = 0
while q:
    cost, a, b = heapq.heappop(q)
    if find(a) == find(b):
        continue
    union(a,b)
    answer += cost

# 다 연결된건지 검사
root = find(1)
for i in range(2, N+1):
    if find(i) != root:
        answer =-1
        break

print(answer)