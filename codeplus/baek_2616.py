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
global max_value
def dfs(i, last_idx, sum_value):
    # print(f"dfs{i, last_idx, sum_value}")
    global max_value
    if i ==3:
        if sum_value > max_value:
            max_value = sum_value
        dp[i][last_idx] = sum_value
        return
    
    if dp[i][last_idx] >= sum_value:
        return
    dp[i][last_idx] = sum_value

    for j in range(last_idx+1, N-K+1):
        # dfs(i+1, j, sum_value+ sum(numlist[j:j+K]))
        dfs(i+1, j, sum_value+ p_sum[j+K-1]- p_sum[j-1])
max_value = -1
# dfs(1, 1, sum(numlist[1:1+K]))
dfs(0, 0, 0)
print(max_value)
