import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input_13392.txt', 'r')
input = sys.stdin.readline

N = int(input())
base = input()
target = input()

base = '0' + base
target = '0' + target



dp = [[-1]*10 for _ in range(N+1)]

def dfs(i, left): # 왼쪽을 left번 돌려서 i번째 까지 맞추는데 드는 최소 비용
    # print(f"dfs{i, left}")
    if i ==0 :
        return 0
    if dp[i][left] !=-1:
        return dp[i][left]

    dp[i][left] = float('inf')
    # 마지막을 오른쪽으로만 돌릴때
    if i!=1:
        cur = (int(base[i]) + left)%10
        dp[i][left] = min(dp[i][left], dfs(i-1, left) + (cur-int(target[i]) +10)%10)
    else:
        cur = int(base[i])
        if left ==0:
            dp[i][left] = min(dp[i][left], (cur - int(target[i]) + 10) % 10)


    if i !=1:
        for k in range(10):
            # 마지막에 왼쯕으로 k번 회전해야 하므로, 직전까진 left-k번 회전했을것이다
            cur = (int(base[i]) + (left-k+10)%10)%10

            if (cur+k)%10 == int(target[i]):
                dp[i][left] = min(dp[i][left], dfs(i-1, (left-k+10)%10) + k)

    else:# i ==1:
        cur = int(base[i])
        if (int(target[i])-cur+10)%10 == left:
            dp[i][left] = min(dp[i][left], left)

    return dp[i][left]

min_value = float('inf')
for i in range(10):
    # print(f"dfs{2,i}", dfs(2, i))
    min_value = min(min_value, dfs(N, i))
print(min_value)