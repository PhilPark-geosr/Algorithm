import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input_1970.txt', 'r')

N = int(input())
brand = list(map(int, input().split()))


dp = [[-1]*(N+1) for _ in range(N+1)]
def dfs(i, j): #i~j번째 까지 악수횟수 최대
    # print(f"dfs{i,j}")
    if i >= j:
        return 0
    if j - i ==1:
        if brand[i] == brand[j]:
            return 1
        return 0
    
    if dp[i][j] !=-1:
        return dp[i][j]
    
    dp[i][j] = dfs(i+1, j)
    for k in range(i+1, j+1):
        if brand[i] == brand[k]:
            dp[i][j] = max(dp[i][j], dfs(i+1, k-1) + dfs(k+1, j)+1)

    # dp[i][j] = max([dfs(i+1, k-1) + dfs(k+1, j) for k in range(i+1, j) if brand[i]== brand[k]])
    # dp[i][j] = max(dp[i][j], dfs(i+1, j))
    return dp[i][j]


# answer
print(dfs(0,N-1))