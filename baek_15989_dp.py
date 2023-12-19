import sys
sys.stdin = open('input_15989.txt', 'r')


dp = [0]*(10**4+1)
dp[1] = 1
dp[2] = 2
dp[3] = 2
dp[4] = 4

for i in range(5, 10**4+1):
    dp[i] = 1   + dp[i-2] + dp[i-3]



T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])