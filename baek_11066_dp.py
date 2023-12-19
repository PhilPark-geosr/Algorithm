import sys
sys.setrecursionlimit(10**9)

sys.stdin = open('input_11066.txt','r')

def dfs(i, j):
    # print(f"dfs{i,j}")
    if i ==j :
        return 0

    if dp[i][j] !=-1:
        return dp[i][j]  
      
    dp[i][j] = float('inf')
    for k in range(i, j):
        dp[i][j] = min(dp[i][j], dfs(i, k) + dfs(k+1, j) + (p_sum[j+1] - p_sum[i]))
    
    return dp[i][j]

T = int(input())
for _ in range(T):
    
    N = int(input())
    # print(N)
    filelist = list(map(int, input().split()))

    # 누적합 계산
    p_sum = [0]*(N+1)
    
    for i in range(1, N+1):
        p_sum[i] = p_sum[i-1] + filelist[i-1]

    # print(p_sum)

    dp = [[-1]*N for _ in range(N)]

    

    print(dfs(0, N-1)) 