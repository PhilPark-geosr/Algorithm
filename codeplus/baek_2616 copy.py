import sys
sys.stdin = open('input_2616.txt', 'r')
# 입력 받기
N = int(input())
numlist = [0] + list(map(int, input().split()))
K = int(input())

# 누적 합 계산
p_sum = [0] * (N + 1)
for i in range(1, N + 1):
    p_sum[i] = p_sum[i - 1] + numlist[i]

# DP 테이블 초기화
dp = [[0] * (N + 1) for _ in range(4)]

# DP 테이블 채우기
for i in range(1, 4):
    for j in range(K * i, N + 1):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - K] + p_sum[j] - p_sum[j - K])

# 결과 출력
print(dp[3][N])
