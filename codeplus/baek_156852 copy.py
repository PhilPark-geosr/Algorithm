import sys
sys.setrecursionlimit(10**9)
sys.stdin= open('input_15685.txt', 'r')
N = int(input())

dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def make_dragon_curve(x, y, d, g):
    result = [(x, y)]
    curve = [d]
    for _ in range(g + 1):
        temp = []
        for px, py in result:
            nx = px + dir[curve[-1]][0]
            ny = py + dir[curve[-1]][1]
            temp.append((nx, ny))
            x, y = nx, ny
        result += temp[::-1]  # 역순으로 추가
        curve = [(c + 1) % 4 for c in curve]  # 방향 변경
    return result

dp = [[0] * 101 for _ in range(101)]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    curve = make_dragon_curve(x, y, d, g)
    
    # 드래곤 커브의 점들을 dp 배열에 표시
    for px, py in curve:
        dp[px][py] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if dp[i][j] == 1 and dp[i + 1][j] == 1 and dp[i][j + 1] == 1 and dp[i + 1][j + 1] == 1:
            answer += 1

print(answer)
