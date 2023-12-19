import sys
sys.stdin = open('input_11265.txt', 'r')
input = sys.stdin.readline

N,M = map(int, input().split())

dp = []
for _ in range(N):
    line = list(map(int, input().split()))
    dp.append(line)


for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

# print(dp)

for _ in range(M):
    a, b, c = map(int, input().split())

    if dp[a-1][b-1] <=c:
        print("Enjoy other party")
    else:
        print('Stay here')


