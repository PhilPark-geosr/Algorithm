import sys
sys.stdin = open('input_15486.txt', 'r')
# input = sys.stdin.readline

# input
N = int(input()) #일할수 있는 날짜
T = [0]
P = [0]
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
# print("T, P", T,P)

# define dp
# dp[i] i번째 날짜까지 일했을때 얻을 수 있는 최대 수익
dp = [0]*(N+1) 

# do dp 
for i in range(1, N+1):
    if T[i] ==1: #당일날 할수 있는 경우
        dp[i] = max(dp[i-1]+ P[i], dp[i])
    else: #당일날 배정받은 일이 기간이 하루를 넘기는 경우 
        dp[i] = max(dp[i-1], dp[i])
        endDay = i + T[i]-1 # 상담이 끝나는 날짜
        if endDay <= N:
            dp[endDay] = max(dp[endDay], dp[i-1] + P[i]) # i-1날짜까지 걸린 최대수익 + 당일날 일해서 벌어드릴 수 있는 최대수익
# print(dp)

# 정답 도출
answer = dp[N]
print(answer)
