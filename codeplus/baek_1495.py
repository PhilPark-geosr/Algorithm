import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input_1495.txt', 'r')

N, S, M= map(int, input().split())
V = list(map(int, input().split()))
V.insert(0,0)

dp = [[-1]*(M+1) for _ in range(N+1)]
#dp[i][target] : i번째까지연주했을때, target을 연주할 수 있어?

def dfs(i, target):
    # print(f"dfs{i, target}")

    if target <0 or target >M:
        return 0

    if i == 0:
        if target == S:
            return 1
        else:
            return 0

    if dp[i][target] !=-1:
        return dp[i][target]

    if dfs(i-1, target - V[i]) == 1 or dfs(i-1, target + V[i]) == 1:
        dp[i][target] = 1

    else:
        dp[i][target] = 0 #연주할 수 없음

    return dp[i][target]

    



# answer
answer = -1
for i in range(M, -1,-1):
    if dfs(N, i) == 1:
        answer  = i
        break

print(answer)