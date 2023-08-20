import sys
sys.stdin =open('input_11060.txt', 'r')

# input
N = int(input())
A = list(map(int, input().split()))
A.insert(0,0)
# dp
dp = [float('inf')]*(N+1)
dp[1] = 0
# dp[i] : i 번째 칸에 도달하기 위한 최소 점프 횟수
for i in range(1, N+1):
    if A[i] == 0:
        continue
    for j in range(1, A[i]+1):
        if i+j <=N:
            dp[i+j] = min(dp[i+j], dp[i]+1)

# print("dp", dp)

if dp[N] == float('inf'):
    print(-1)
else:
    print(dp[N])
