import sys
import collections
import heapq
sys.stdin = open('input_1939.txt', 'r')
sys.setrecursionlimit(1000000)
N, M = map(int, input().split())

dic = collections.defaultdict(list)

q = []
for _ in range(M):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (-c, a, b))

while q:
    cost, x, y = heapq.heappop(q)
    dic[x].append((y, -cost))
    dic[y].append((x, -cost))

# print(dic)

def dfs(v, end, weight): # weight 제한으로 다리를 통과할 수 있는지
    print(f"{v} 방문")
    if v == end:
        return True
    else:
        for node, cost in dic[v]:
            print(node, cost)
            if visited[node] ==0 and cost >= weight: # 넘어갈수 있는경우
                visited[node] =1
                check = dfs(node, end, weight)
                # visited[node] =0
                if check == True:
                    return True
        return False

start, des = map(int, input().split())


# 이진탐색 수행
l = 0 
r = 10**9
answer = 0 
while l<=r:
    mid = (l+r)//2
    print("한계중량",  mid)
    visited = [0]*(N+1)
    visited[start] =1
    if dfs(start,des, mid) == True:
        answer = mid
        l = mid +1
    else:
        r = mid -1

print(answer)
