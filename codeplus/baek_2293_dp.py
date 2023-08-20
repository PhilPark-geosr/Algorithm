import sys
sys.stdin = open('input_2293.txt','r')
#input=sys.stdin.readline

N, K = map(int, input().split())
money_list = []
for _ in range(N):
    money = int(input())
    money_list.append(money)

# print('money_list', money_list)

dp = [0]*(K+1)
dp[0] =1

for money in money_list:
    for i in range(1, K+1):
        if i-money >=0:
            dp[i] = dp[i] + dp[i-money]

print(dp[K])
    