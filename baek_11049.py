import sys
sys.stdin = open('input_11049.txt', 'r')

n = int(input())
# 행렬 크기 담은 dic 생성
dic =[[]]
for _ in range(n):
    a,b = map(int, input().split())
    dic.append([a,b])
# print(dic)
# dp initialize
# dp[i][j] = n개중 i번째 행렬 ~ j번째 행렬곱의 최솟값

dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(2, n+1):
    for j in range(1, n-i+2):
        # print(f"{j,j+i-1},{[dp[j][j+k]+dp[j+k+1][j+i-1] + dic[j][0]*dic[j+k][1]*dic[j+i-1][1] for k in range(i-1)]}")
        dp[j][j+i-1] = min([dp[j][j+k]+dp[j+k+1][j+i-1] + dic[j][0]*dic[j+k][1]*dic[j+i-1][1] for k in range(i-1)])


print(dp[1][n])
