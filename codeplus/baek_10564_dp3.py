import sys
# sys.stdin = open('input_10564.txt', 'r')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    scorelist = list(map(int, input().split()))

    dp = [[False] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = True

    
    for score in range(N + 1):
        for work in range(N + 1):
            if dp[score][work]:
                for i in range(M):
                    new_score = score + scorelist[i]
                    new_work = work + score + scorelist[i]
                    if new_work <= N:
                        dp[new_score][new_work] = True

    answer = -1
    for i in range(N + 1):
        if dp[i][N]:
            answer = i

    print(answer)
