import sys
sys.stdin = open('input_11570.txt', 'r')

# input
N= int(input())
numlist= list(map(int, input().split()))
numlist.insert(0,0)

# dp 구성
# dp = [[float('inf')]*(N+1) for _ in range(N+1)]

dp = [[float('inf')]*(N+1) for _ in range(N+1)]

# dp 초기화
dp[1][0] = 0
dp[0][1] = 0

for i in range(N):
    for j in range(N):
        if i ==j : # 둘다 똑같은 음을 부르는 경우는 없으므로
            continue
        next = max(i,j) + 1 # 다음 음 계산
        if i == 0 or j ==0: #둘중에 하나가 안부르면
            numlist[0] = numlist[next]
        
        dp[next][j] = min(dp[next][j],dp[i][j] + abs(numlist[next]-numlist[i]))
        dp[i][next] = min(dp[i][next], dp[i][j] +abs(numlist[next] - numlist[j]))

            
# 정답 추출
answer = float('inf')
for i in range(N):
    answer = min(answer, dp[i][N])
    answer = min(answer, dp[N][i])
print(answer)
    
