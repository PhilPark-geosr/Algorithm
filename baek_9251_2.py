import sys

sys.stdin = open('input_9251.txt', 'r')

str1 = input()
str2 = input()

# dp 정의
# dp[i][j] # str1의 1~ i번재까지 글자와 str2의 1~j까지 글자로 만들 수 있는 최장 공통 부분 수열 길이

n = len(str1)
m = len(str2)

dp = [[0]*(m+1) for _ in range(n+1)]


for i in range(n+1):
    for j in range(m+1):
        if i == 0 and j==0:
            if i+1 <=n:
                dp[i+1][j] = 0
            if j+1<=m:
                dp[i][j+1] = 0
            continue
        if i ==0 and j!=0:
            if j+1 <=m:
                dp[i][j+1] = 0

            if i+1 <=n:
                if str1[i] == str2[j - 1]:
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + 1)
                else:
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

        elif i!=0 and j==0:
            if i+1<=n:
                dp[i+1][j] = 0

            if j+1 <=m:
                if str1[i-1] == str2[j]:
                    dp[i][j+1] = max( dp[i][j+1], dp[i][j] +1)
                else:
                    dp[i][j+1] = max( dp[i][j+1], dp[i][j])

        else:
            if i+1 <=n:
                if str1[i] == str2[j-1]:
                    dp[i+1][j] = max( dp[i+1][j], dp[i][j] +1)
                else:
                    dp[i+1][j] = max( dp[i+1][j], dp[i][j])

            if j+1 <=m:
                if str1[i-1] == str2[j]:
                    dp[i][j+1] = max( dp[i][j+1], dp[i][j] +1)
                else:
                    dp[i][j+1] = max( dp[i][j+1], dp[i][j])





print(dp[n][m])