import sys
sys.stdin = open('input_11066.txt', 'r')


def solution(N, filelist):

    # 누적합 선언
    # S[i] : filelist의 1~i번째까지의 합
    S = [0]*(N+1) 
    for i in range(1,N+1):
        S[i] = S[i-1] + filelist[i-1]
    # print(S)

    # dp[i][j] i번째 file ~ j번째 파일까지 합치는데 드는 비용의 최소
    dp = [[0]*(N+1) for _ in range(N+1)]

    for i in range(1, N):
        for j in range(1, N-i+1):
            # S[j+i] - S[j-1] = j ~ j+i 까지의 부분합
            dp[j][j+i] = min([dp[j][k] + dp[k+1][j+i] for k in range(j, j+i)]) + (S[j+i] - S[j-1])
    return dp[1][N]

#  정답 계산
T = int(input()) # case갯수
for _ in range(T):
    N = int(input())
    filelist = list(map(int, input().split()))
    answer = solution(N, filelist)
    print(answer)
