import sys
sys.setrecursionlimit(10**9)

sys.stdin = open('input_12996.txt', 'r')

S, a, b, c= map(int, input().split())
dp = [[[[0]*(S+1) for _ in range(c+1)] for _ in range(b+1)] for _ in range(a+1)]

dp[0][0][0][0] =1
for N in range(S):
    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):

                if i+1 <=a:
                    dp[i+1][j][k][N+1] += dp[i][j][k][N]
                if i+1 <=a and j+1 <=b:
                    dp[i+1][j+1][k][N+1] += dp[i][j][k][N]
                if i+1 <=a and k+1 <=c:
                    dp[i+1][j][k+1][N+1] += dp[i][j][k][N]
                if i+1 <=a and j+1 <=b and k+1 <=c:
                    dp[i+1][j+1][k+1][N+1] += dp[i][j][k][N]
                if j+1 <=b:
                    dp[i][j+1][k][N+1] += dp[i][j][k][N]
                if j+1 <=b and k+1<=c:
                    dp[i][j+1][k+1][N+1] += dp[i][j][k][N]
                if k+1 <=c:
                    dp[i][j][k+1][N+1] += dp[i][j][k][N]
    


print(dp[a][b][c][S]%1000000007)
