import sys

sys.setrecursionlimit(10 ** 9)
sys.stdin = open('input_10422.txt', 'r')

T = int(input())

# dp
dp = [-1] * (5001)


def dfs(v):
    # print(f"dfs{v}")

    if v == 0:
        return 1
    if dp[v] != -1:
        return dp[v]

    dp[v] = 0  # 방문체크
    for k in range(2, v + 1, 2):
        dp[v] += dfs(k - 2) * dfs(v - k)
        dp[v] %= 1000000007
    return dp[v]


# Test
# L = 4
# dp = [-1]*(L+1)
# print(dfs(L))

for _ in range(T):
    L = int(input())
    if L % 2 != 0:
        print(0)
    else:
        print(dfs(L))


