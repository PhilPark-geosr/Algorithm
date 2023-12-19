import sys
sys.stdin = open('input_dragon_cruve.txt', 'r')

N = int(input())
grid = [[0]*101 for _ in range(101)] #드래곤 커브 기록용

dir = [(1, 0), (0,-1), (-1,0), (0,1)]


def rotate(x, y, c_x, c_y):
    # 원점으로 맞춰준다
    new_x, new_y = x - c_x, y - c_y
    # 시계방향 90도 회전
    new_x, new_y = -new_y, new_x
    # 다시 돌려주기
    new_x, new_y = new_x + c_x, new_y + c_y
    return (new_x, new_y)
def make_dragon_curve(s_x, s_y, d, g):
    curve = []
    curve = [(s_x+dir[d][0], s_y + dir[d][1]), (s_x, s_y)]
    # print('초기 curve', curve)

    for _ in range(g): #g세대동안 진행
        new_curve = []
        c_x, c_y = curve[0]
        for x, y in curve[1:]:
            new_curve.append(rotate(x,y, c_x, c_y))
        # 커브 더해주기
        curve = new_curve[::-1] + curve
        # print('curve', curve)
    return curve

def record(curve):
    for x, y in curve:
        grid[x][y] = 1

# test
# make_dragon_curve(4, 2, 1, 3)

# main
for _ in range(N):
    x, y, d, g = map(int, input().split())
    curve = make_dragon_curve(x, y, d, g)
    record(curve)
    
# 정답세기
cnt = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] ==1 and grid[i+1][j] ==1 and grid[i][j+1] ==1 and grid[i+1][j+1] ==1:
            cnt +=1

print(cnt)
