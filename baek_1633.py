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
dp = [[[-1 for _ in range(16)] for _ in range(16)] for _ in range(N+1)]

def dfs(i, black, white, score):
  #  print(f"dfs{i, black, white, score}")
    # End condition
    if black > 15 or white > 15 or i >= N:
        return
    dp[i][black][white] = score #기록

    if black < 15 and white <=15:
        if i+1 <N:
            new_score = score + abilities[i+1][0]
            if new_score > dp[i+1][black+1][white]:
                dfs(i+1, black+1, white, new_score)
    if white < 15 and black <= 15:
        if i+1 <N:
            new_score = score + abilities[i+1][1]
            if new_score > dp[i+1][black][white+1]:
                dfs(i+1, black, white+1, new_score)

    # 아예 안하고 넘어가는 경우
    if i+1 < N:
        if score > dp[i+1][black][white]:
            dfs(i+1, black, white, score)





# 답 구하기
dfs(0, 0, 0, 0)
answer = 0
for i in range(1, N+1):
    answer = max(answer, dp[i][15][15])

print(answer)