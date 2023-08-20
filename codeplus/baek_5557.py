import sys
sys.setrecursionlimit(10**9)

sys.stdin = open('input_5557.txt', 'r')
N = int(input())
nums = list(map(int, input().split()))
nums.insert(0,0)
sum_target = nums[N] # 구하고자 하는 답

dp = [[-1]*21 for _ in range(N)]


def dfs(i, target):
    # print(f"dfs{i,target}")
    if target <0 or target >20:
        return 0

    if i ==1:
        if nums[i] == target:
            return 1
        return 0
    if dp[i][target] !=-1:
        return dp[i][target]
    

    dp[i][target] = dfs(i-1, target-nums[i]) + dfs(i-1, target+nums[i])

    return dp[i][target]

print(dfs(N-1, sum_target))