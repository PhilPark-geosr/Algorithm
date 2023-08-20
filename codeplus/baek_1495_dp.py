import sys
sys.stdin = open('input_1495.txt', 'r')

N, S, M = map(int, input().split())
V = list(map(int, input().split()))
V.insert(0,0)

#dp[i][vol] # i번째 곡을 vol으로 연주할 수 있으면 1 , 없으면 -1
dp = [[-1]*(M+1) for _ in range(N+1)]

dp[0][S] = 1 #첫번째는 
for i in range(N):
    for vol in range(M+1):
        if dp[i][vol] == 1:
            if vol + V[i+1] <=M:
                dp[i+1][vol + V[i+1]] =1
            if vol - V[i+1] >=0:
                dp[i+1][vol - V[i+1]] =1

# 결과도출
answer =-1
for vol in range(M+1):
    # print(dp[N][vol])
    if dp[N][vol] ==1:
        answer = vol
print(answer)