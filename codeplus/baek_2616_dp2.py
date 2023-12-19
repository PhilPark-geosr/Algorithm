import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input_2616.txt', 'r')
input = sys.stdin.readline
N = int(input())
numlist = list(map(int, input().split()))
numlist.insert(0,0)
K = int(input())

# 누적합 미리 구해놓기
p_sum = [0]*(N+1)
for i in range(1, N+1):
    p_sum[i] = p_sum[i-1] + numlist[i]
# print(p_sum)



dp = [[-1]*(N+1) for _ in range(4)] 
def dfs(i, j):
    # print(f"dfs{i,j, dp}")
    if i==0:
        return 0
    if j ==0:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    
    if j-K >=0:
        # print("psum", p_sum[j]- p_sum[j-K])
        dp[i][j] = max(dfs(i-1, j-K) + p_sum[j]- p_sum[j-K], dfs(i,j-1))
    else:
        dp[i][j] = dfs(i,j-1)


    return dp[i][j]


print(dfs(3, N))