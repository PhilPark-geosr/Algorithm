# 입력 받기
import sys
sys.stdin = open('input_14499.txt', 'r')
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
map_data = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

# 주사위 모델 초기화
dice = [0] * 6
# 주사위의 각 면에 해당하는 방향을 표시
dx = [0, 0, -1, 1]  # 동, 서, 북, 남
dy = [1, -1, 0, 0]

for command in commands:
    nx, ny = x + dx[command - 1], y + dy[command - 1]
    
    # 주사위가 지도를 벗어나는 경우 해당 명령 무시
    if not (0 <= nx < n and 0 <= ny < m):
        continue
    
    if command == 1:  # 동쪽으로 굴릴 때
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif command == 2:  # 서쪽으로 굴릴 때
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif command == 3:  # 북쪽으로 굴릴 때
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    else:  # 남쪽으로 굴릴 때
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    
    if map_data[nx][ny] == 0:
        map_data[nx][ny] = dice[5]
    else:
        dice[5] = map_data[nx][ny]
        map_data[nx][ny] = 0
    
    x, y = nx, ny
    print(dice[0])
