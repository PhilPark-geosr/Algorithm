import sys
sys.stdin = open('input_11066.txt','r')
# T: number of testcase
T = int(input())

for _ in range(1): #testcase동안
    n = int(input())
    # print(n)
    pagelist = list(map(int, input().split()))
    # print(pagelist)
    # 누적합 구해놓기
    s = [0]*(n+1) # s[i] : 1~i까지의 누적합
    for i in range(1, n+1):
        s[i] = s[i-1] + pagelist[i-1]
    # print(s)

    # dp[i][j] i ~ j번째 까지 합치는데 드는 최소비용!
    dp = [[0]*(n+1) for _ in range(n+1)]

    
    for i in range(1, n):
        dp[i][i+1] = s[i+1] - s[i-1]

    for i in range(2, n+1): # 부분 파일의 길이
        for j in range(1, n+2-i):   # 시작점
            dp[j][j+i-1] = min([dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)]) + (s[j+i-1] - s[j-1])
            print(j, j+i-1, [dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)] )

    print(dp[1][n])

# def solve():
#     N, A = int(input()), [0] + list(map(int, input().split()))
#     # S[i]는 1번부터 i번까지의 누적합
#     S = [0 for _ in range(N+1)]
#     for i in range(1, N+1):
#         S[i] = S[i-1] + A[i]
 
#     # DP[i][j] : i에서 j까지 합하는데 필요한 최소 비용
#     # DP[i][k] + DP[k+1][j] + sum(A[i]~A[j])
#     DP = [[0 for i in range(N+1)] for _ in range(N+1)]
#     for i in range(2, N+1): # 부분 파일의 길이
#         for j in range(1, N+2-i):   # 시작점
#             DP[j][j+i-1] = min([DP[j][j+k] + DP[j+k+1][j+i-1] for k in range(i-1)]) + (S[j+i-1] - S[j-1])
 
#     print(DP[1][N])
 
# for _ in range(int(input())):
#     solve()
