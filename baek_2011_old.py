import sys
sys.stdin = open('input_2011.txt', 'r')
sys.setrecursionlimit(10**8)

secret = input()
N = len(secret)

dp = [[-1]*(N) for _ in range(N)]

def dfs(i,j):
    print(f"dfs{i,j}, 단어, {secret[i:j+1]}")
    if i == j:
        return 1
    if j-i == 1:
        # print(int(secret[i:j+1]))
        if int(secret[i:j+1]) > 26:
            return 0
        else:
            return 1
    # memoization
    if dp[i][j] != -1:
        return dp[i][j]

    # dp[i][j] = 0

    dp[i][j] = dfs(i, j-1)*dfs(j,j) + dfs(i, j-2)*dfs(j-1, j) \
                + dfs(i, i)*dfs(i+1, j) + dfs(i, i+1)*dfs(i+2, j)
    dp[i][j] %= 10**6
    return dp[i][j]




# ------------------- main ---------------------- #

answer = dfs(0, N-1)

if answer == -1:
    print(0)
else:
    print(answer)