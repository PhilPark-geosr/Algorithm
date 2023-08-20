import sys
sys.stdin = open('input_15486.txt', 'r')
# input = sys.stdin.readline
N = int(input())
T = [0]
P = [0]

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
# print(T,P)

# dp
dp = [0]*(N+1)
for i in range(1, N+1):
    dp[i] = max(dp[i-1], dp[i])
    if i+T[i] <= N:
        dp[i+T[i]-1] = max(dp[i+T[i]-1], dp[i-1]+ P[i])

print(dp[N])