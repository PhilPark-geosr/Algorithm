import sys
# sys.stdin = open('input_10564.txt', 'r')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    # print("N,M", N,M)
    scorelist = list(map(int, input().split()))

    dp = [[-1]*(N+1) for _ in range(N+1)]
    # global max_score
    def dfs(score, work):
        # global max_score
        # print(f"dfs{score, work}")

        # if work ==N:
        #     max_score = max(score, max_score)
        #     return

        if dp[score][work] !=-1:
            # print('이미존재')
            return
        
        dp[score][work] =1 #방문기록

        for i in range(M):
            if work+ score + scorelist[i] <=N:
                dfs(score + scorelist[i], work +score + scorelist[i])

    # max_score = -1
    dfs(0,0)
    # print(max_score)
    answer =-1
    for i in range(N+1):
        if dp[i][N] == 1:
            answer = i


    print(answer)