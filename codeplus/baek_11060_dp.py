import sys
sys.setrecursionlimit(10**9)

sys.stdin = open('input_11060.txt','r')
input = sys.stdin.readline

N = int(input())
numlist = list(map(int, input().split()))

dp = [-1]*(N)

def dfs(i):
    if i==0:
        return 0
    if dp[i] !=-1:
        return dp[i]

    dp[i] = float('inf')
    for k in range(i):
        if k + numlist[k] >= i:
            dp[i] = min(dp[i], dfs(k)+1)

    return dp[i]


answer = dfs(N-1)

if answer == float('inf'):
    print( -1)
else:
    print(answer)