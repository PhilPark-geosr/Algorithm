import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input_12685.txt', 'r')
N, K = map(int, input().split())

W = []
V = []
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)
W.insert(0,0)
V.insert(0,0)
# print(W,V)
# dfs
def dfs(i, weight):
    # print(f"dfs{i,weight}")
    if weight ==0:
        return 0
    if i ==0:
        return 0
    if dp[i][weight] !=-1:
        return dp[i][weight]

    if weight- W[i]>=0:
        dp[i][weight] = max(dfs(i-1, weight), dfs(i-1, weight-W[i])+ V[i])
    else:
        dp[i][weight] =dfs(i-1, weight)
    return dp[i][weight]
# dp
# dp[i][weight] # i번째까지 사용했을때 weight를 만들 수 있는 비용의 최대
dp = [[-1]*(100001) for _ in range(N+1)]

print(dfs(N, K))