import sys
sys.stdin = open('input_1126.txt', 'r')

N = int(input())
block = list(map(int, input().split()))
block.insert(0,0)

# 높이의 합 이하로 차이가 나므로 dp 배열 높이는 그렇게 선언
total_height = sum(block)

# dp initialize
# dp[i][diff] i번째 블록까지 사용 가능할때 diff차이나는 최대 블록 높이
dp = [[-1]*(total_height+1) for _ in range(N+1)]

# 한개써서 되는 경우는 없음
dp[1][0] = 0
# 1번쨰 블록써서 나올수 있는 경우는 차이가 block[1]만큼 차이나는 경우밖에 없다
dp[1][block[1]] = block[1]

for i in range(2, N+1):
    for diff in range(total_height+1):
        # 원래 값이 없을때
        if dp[i-1][diff] == -1:
            continue

        # i번째 블록을 아무것도 사용하지 않았을때
        dp[i][diff] = max(dp[i][diff], dp[i-1][diff])
        
        # i번째 블록을 큰 쪽에 놓을때
        
        dp[i][diff+ block[i]] = max(dp[i][diff+block[i]], dp[i-1][diff] + block[i])
        
        # i번째 블록을 작은 쪽에 놓을 때
        if block[i] <= diff : #최대높이가 유지될때
            dp[i][diff-block[i]] = max(dp[i][diff-block[i]], dp[i-1][diff])
        else:
            dp[i][block[i]- diff] = max(dp[i][block[i]- diff], dp[i-1][diff] + block[i]- diff)

# 정답
answer = dp[N][0]
if answer > total_height/2 or answer ==0:
    print(-1)
else:
    print(answer)