import sys
sys.stdin = open('input_2098.txt', 'r')
# input = sys.stdin.readline

# input
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
#print('graph',graph)

# test bit operation

# print(bin((1<<3)-1))
# print(bin(1 << 3 - 1))
# print(101 & (1 << 1))

# define dp
# -1로 하는 이유 : 방문하지 않은 부분에 대한 처리
dp = [[-1]*(1<<N) for _ in range(N)]

# # define dfs
def dfs(v, visited):
    # print(f"dfs{v, visited}")
    if dp[v][visited] != -1: #한번이라도 처리됐으면
        return dp[v][visited]
    if visited == (1<<N) -1: ## 모든 정점을 다 방문했으면..
        if graph[v][0]==0: # 경로가 없으면..
            return float('inf')
        else: #경로가 있으면
            return graph[v][0] # 이유 : start를 0으로 함
    
    min_value = float('inf')
    for i in range(1,N): # 3가지중 하나
        # 길이 없으면 스킵
        if graph[v][i] ==0:
            continue
        # 방문한 곳이면 스킵
        if visited & (1<<i):
            continue 
        min_value = min(min_value, dfs(i, visited|(1<<i))+ graph[v][i])
    dp[v][visited] = min_value
    
    return dp[v][visited] 


# answer
answer = dfs(0, 1)
print(answer)