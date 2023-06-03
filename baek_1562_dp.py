import sys
sys.stdin = open('input_1562.txt','r')
n = int(input())
# define dp
dp = [[[0 for _ in range(1<<10)] for _ in range(10)] for _ in range(n+1)]

# dp[i][j][k] : i자리수의 끝나는수가 j이고, 현재까지 사용한 수의 정보가 k일때의 경우의 수
for k in range( 10):
    dp[1][k][1<<k] =1

for i in range(2,n+1):
    for j in range(10):
        for bit in range(1<<10):
            # print(bit)
            # bit : 사용한 넘버의 기록
            new_bit = bit | (1 << j) 
            if j == 0:
                dp[i][j][new_bit] += dp[i-1][j+1][bit]
            elif j ==9:
                dp[i][j][new_bit] += dp[i-1][j-1][bit]
            else:
                dp[i][j][new_bit] += dp[i-1][j-1][bit]
                dp[i][j][new_bit] += dp[i-1][j+1][bit]
            dp[i][j][new_bit] %= 1000000000
            #끝자리가 j이면서 bit의 숫자기록을 가지고 있는 수 --> 자릿수가 i-1인 수에서 
            # 끝자리가j-1과 j+1에서 올수 있으며 ,
## 0~9 다쓴 경우의 수 출력
answer = 0
for i in range(1, 10):
    # print(dp[n][i][(1<<10)-1])
    answer += dp[n][i][(1<<10)-1]
    answer %= 1000000000
print(answer)
