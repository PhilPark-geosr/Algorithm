import sys
sys.stdin = open('input_1939.txt', 'r')
import collections

sys.setrecursionlimit(1000000)
# input
N, M = map(int, input().split())
graph = collections.defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

start, end = map(int, input().split())
# 그래프 들어오는 것 중 큰 값 처리(그래프만들기)

# dfs
# 중량제한내로 건너갈수 있는지 체크
global flag
def dfs(v, end, w, limit):
    global flag
    #print(f'dfs{v, end, w, limit, visited}')
    if v == end: #도착지점에 도달했을경우
        #중량제한 내로 갈수 있음
        flag = True
        return
    else:
        # 그래프 순회
        for node, cost in graph[v]:
            new_w = min(w, cost) #둘중 작은거
            #print("new_w", new_w )
            if new_w >= limit and visited[node] ==0:
                visited[node] =1
                dfs(node, end, new_w, limit)
                # visited[node] =0



# 결과값 처리
l = 0
r = 10**9
answer = 10**9

while l<=r:
    visited = [0]*(N+1)
    visited[start] =1
    mid = (l+r)//2
    flag = False
    dfs(start, end, 10**9, mid)
    if flag ==True:
        # print('mid', mid)
        l = mid +1
        answer = mid
        
    else:
        r = mid -1

# test
# flag = False
# visited = [0]*(N+1)
# visited[start] =1
# dfs(start, end, 10**9, 3)
# print('flag', flag)
print(answer)