import sys
sys.stdin = open('input_1106.txt','r')
input = sys.stdin.readline

C, N = map(int, input().split())
cost = []
customer = []
for _ in range(N):
    a, b = map(int, input().split())
    cost.append(a)
    customer.append(b)


dp = [float('inf')]*(C+1001)
dp[0] = 0

for j in range(1, C+1001):
    for i in range(N):
        if j - customer[i] >=0:
            dp[j] = min(dp[j], dp[j-customer[i]] + cost[i])
        else:
            continue

    # print('dp', dp)

answer = min(dp[C:])

print(answer)