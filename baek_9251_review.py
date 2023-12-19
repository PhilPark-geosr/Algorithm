import sys
sys.stdin = open('input_9251.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

A = input()
B = input()
n = len(A)
m = len(B)
dp = [[-1]*(m+1) for _ in range(n+1)]
def dfs(i,j):
    if i == 0 or j == 0:
        return 0
    if dp[i][j] !=-1:
        return dp[i][j]
    if A[i-1] == B[j-1]:
        dp[i][j] = dfs(i-1,j-1) +1
    else:
        dp[i][j] = max(dfs(i-1,j), dfs(i,j-1))
    return dp[i][j]



print(dfs(n,m))