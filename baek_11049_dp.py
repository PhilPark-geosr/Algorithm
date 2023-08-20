import sys
sys.stdin = open('input_11049.txt', 'r')

N = int(input())

matrix = [] #matrix 배열생성
for _ in range(N):
    a,b = map(int, input().split())
    matrix.append([a,b])

# dp 선언
# dp[i][j] : i~j 까지 행렬곱의 연산 최솟값
max_value = 2**31 -1
dp = [[0]*N for _ in range(N)]

for i in range(1, N):
    for j in range(N-i):
        dp[j][j+i] = min([dp[j][k] + dp[k+1][j+i] + matrix[j][0]*matrix[k+1][0]*matrix[j+i][1] for k in range(j, j+i)])



# 답 계산
answer = dp[0][N-1]
print(answer)
