import sys
#sys.setrecursionlimit(10**9)
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
dp = [[0]*(100001) for _ in range(N+1)]

for i in range(N):
    for weight in range(K+1):
        dp[i+1][weight] = max(dp[i+1][weight], dp[i][weight])
        if weight + W[i+1] <= K:
            dp[i+1][weight + W[i+1]] = max(dp[i+1][weight + W[i+1]], dp[i][weight] + V[i+1])
            
print(dp[N][K])