import sys
sys.stdin = open('input_9251.txt', 'r')

word1 = input()
word2 = input()
n = len(word1)
m = len(word2)


dp = [[0]*(m+1) for _ in range(n+1)]

# dp[i][j] : word의 i번째항이 마지막인 수열 과 word의 j번째까지로 만든 수열 중 공통 부분수열의 최대 길이
for i in range(1, n+1):
    for j in range(1, m+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            # dp[i-1][j-1]가 빠지는 이유 기록
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
# print(dp)
print(dp[n][m])
            

