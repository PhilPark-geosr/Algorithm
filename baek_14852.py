import sys
sys.stdin = open('input_14852.txt', 'r')

N = int(input())

dp = [0]*(N+1) # dp[N] 2*N칸을 채울 수 있는 경우의 수
dp[0] = 1
dp[1] = 2
S = [0]*(N+1) #dp의 0~ i번째까의합
S[0] = 1
S[1] = S[0] + dp[1]

# dp[N] = 2*dp[N-1] + 3*dp[N-2] + 2*dp[N-3] + 2*dp[N-4] + ... + 2*dp[0]
#       = 2*S[N-1] + dp[N-2]

# dp계산
for i in range(2, N+1):
    dp[i] = (2*S[i-1] + dp[i-2])%1000000007
    S[i] = (S[i-1] + dp[i])%1000000007

# ------------------- main -----------------#
print(dp[N])