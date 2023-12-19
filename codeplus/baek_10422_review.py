import sys
sys.stdin = open('input_10422.txt', 'r')
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
T = int(input())

mod = 1000000007
dp = [-1]*(5001)
dp[2] =1
def dfs(L):
    # print(f"dfs{L}")
    if L ==0:
        return 1
    if L % 2 ==1:
        return 0
    if dp[L] !=-1:
        # print('이미 있습니다.')
        return dp[L]

    dp[L] =0


    for k in range(2, L+1):
        dp[L] += dfs(k)*dfs(L-k)

    dp[L] %= mod
    return dp[L]
#
for _ in range(T):
    num = int(input())
    print(dfs(num))