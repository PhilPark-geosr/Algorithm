import sys

sys.stdin = open('input_9251.txt', 'r')

str1 = input()
str2 = input()

# dp 정의
# dp[i][j] # str1의 1~ i번재까지 글자와 str2의 1~j까지 글자로 만들 수 있는 최장 공통 부분 수열 길이

n = len(str1)
m = len(str2)

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if str1[i-1] == str2[j-1] : #맨 마지막 글자가 같으면 최장 공통 부분 수열엔 하나 추가 됨
            dp[i][j] = dp[i-1][j-1] +1
        else:
            dp[i][j] = max(dp[i-1][j] ,dp[i][j-1])

print(dp[n][m])