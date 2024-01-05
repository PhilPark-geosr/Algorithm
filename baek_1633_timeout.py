import sys
sys.setrecursionlimit(10**8)
sys.stdin = open('input_1633.txt', 'r')
input = sys.stdin.readline

## 능력치 리스트 만들기
abilities = []
while True:
    temp = input()
    if temp == "":
        break
    a,b = map(int, temp.split())
    abilities.append((a,b))
abilities.insert(0, (0,0))
#print(abilities)

N = len(abilities)

# dp 정의
dp = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(N+1)]

for i in range(N-1):
    for black in range(16):
        for white in range(16):
            if black < 15:
                new_score = dp[i][black][white] + abilities[i+1][0]
                dp[i+1][black+1][white] = max(dp[i+1][black+1][white], new_score)
            if white < 15:
                new_score = dp[i][black][white] + abilities[i + 1][1]
                dp[i + 1][black][white+1] = max(dp[i + 1][black][white+1], new_score)
            # 그냥
            dp[i+1][black][white] = max(dp[i+1][black][white], dp[i][black][white])


answer = 0
for i in range(1, N+1):
    answer = max(answer, dp[i][15][15])

print(answer)