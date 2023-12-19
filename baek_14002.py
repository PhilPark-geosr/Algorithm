import sys
sys.stdin = open('input_14002.txt', 'r')
input = sys.stdin.readline

N = int(input())
numbers = [0] + list(map(int, input().split()))

dp = [[-1]*(N+1) for _ in range(N+1)]
path = [-1]*(N+1)

def dfs(i, j):
    if i==j:
        return 1
    if dp[i][j] !=-1:
        return dp[i][j]

    dp[i][j] =1 #최소길이는 1이므로
    if numbers[j] > numbers[j-1]:
        dp[i][j] = max(dp[i][j], dfs(i, j-1) +1)
        path[j] = j-1
    else:
        dp[i][j] = max(dp[i][j], dfs(i, j - 1))

    if numbers[i+1] > numbers[i]:
        dp[i][j] = max(dp[i][j], dfs(i+1, j) + 1)
        path[i+1] = i
    else:
        dp[i][j] = max(dp[i][j], dfs(i + 1, j))

    return dp[i][j]

print(dfs(1, N))
print(path)

# 끝에점 찾기
node = -1
for i in range(len(path)-1, -1, -1):
    if path[i] != -1:
        node = i
        break
print(node)

answer = []
while node > 0:
    answer.append(node)
    node = path[node]

print(answer)