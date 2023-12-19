import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input_13392.txt', 'r')
input = sys.stdin.readline

N = int(input())
base = input()
target = input()
# base = '0'+base
# target = '0' + target

# print('base, target', base, target)

dp = [[-1]*10 for _ in range(N+1)]

def dfs(i, left):
    # print(f"dfs{i, left}")
    if i == N:
        return 0
    if dp[i][left] !=-1:
        return dp[i][left]

    cur = (int(base[i]) + left) % 10
    # print('cur, target', cur, target[i])
    left_cost = (int(target[i])-cur+10)%10
    right_cost = (cur-int(target[i]) + 10)%10

    dp[i][left] = min(left_cost + dfs(i+1,(left+ left_cost)%10), right_cost + dfs(i+1, left))
    return dp[i][left]

print(dfs(0,0))
# print(dp)