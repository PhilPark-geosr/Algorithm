import sys
sys.stdin = open('input_10564.txt', 'r')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print("N,M", N,M)
    scorelist = list(map(int, input().split()))

    dp = [-1]*(N+1)
    
    def dfs(score):
        # print(f"dfs{score}")
        if score ==0:
            return 0

        if dp[score] !=-1:
            return dp[score]
        

        dp[score] = float('inf')
        for i in range(M):
            if score-scorelist[i] >=0:
                dp[score] = min(dp[score], dfs(score-scorelist[i])+ score)
        return dp[score]
    
    answer = -1
    for score in range(N+1):
        print(score, dfs(score))
        if dfs(score) == N:
            answer = score

    print(answer)