import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input_4811.txt', 'r')

N = 30
dp = [[-1]*(N+1) for _ in range(N+1)]
def dfs(w, h):
    if w ==0:
        return 1
    if dp[w][h] !=-1:
        return dp[w][h]
    
    dp[w][h] = 0
    if w-1 >=0:
        dp[w][h] += dfs(w-1, h+1)
    if h-1>=0:
        dp[w][h] += dfs(w, h-1)
    
    return dp[w][h]


flag = True
while flag:
    i = int(input())
    if i == 0:
        flag = False
    else:
        print(dfs(i,0))