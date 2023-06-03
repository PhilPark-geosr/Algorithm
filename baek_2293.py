import sys
sys.stdin = open("input_2293.txt", "r")

n, k = map(int, input().split())
coinlist = []
for _ in range(n):
    elem = int(input())
    coinlist.append(elem)

#initialize dp
# dp[i] : i원 만드는 경우의 수
dp = [0]*(k+1) 
dp[0] = 1
for coin in coinlist:
    for i in range(coin, k+1):
        dp[i] = dp[i] + dp[i-coin]

print(dp[k])


