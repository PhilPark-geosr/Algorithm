import sys, math    
from fractions import Fraction
sys.stdin = open('input_1413.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[0]*(21) for _ in range(21)]
dp[1][1] =1

for i in range(2, N+1):
    for j in range(1, i+1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]*(i-1)

# 모든 경우의 수 계산
div = 1
for i in range(1, N+1):
    div =  div*i


numertaor = 0
for j in range(1, M+1):
    numertaor += dp[N][j]


# print(Fraction(numertaor,div))


print('%d/%d' % (numertaor // math.gcd(numertaor, div), div // math.gcd(numertaor, div)))
