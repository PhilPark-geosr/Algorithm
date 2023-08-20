import sys
sys.stdin = open('input_7579.txt', 'r')

# input
N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

memory.insert(0,0)
cost.insert(0,0)

C = int(sum(cost)) # 메모리 합
# dp 선언
dp = [[0]*(C+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, C+1):
        if cost[i] > j: 
            dp[i][j] = dp[i-1][j]
        else: 
            dp[i][j] = max(dp[i-1][j], memory[i] + dp[i-1][j-cost[i]])


# 답구하기
answer = sum(cost)
for i in range(1,N+1):
    for j in range(1, C+1):
        if dp[i][j] >= M and j < answer: #기준치 넘으면
            answer = j

print(answer)
