#하나만잘하면된다..
import sys
sys.setrecursionlimit(10**9)
# sys.stdin= open('input_15685.txt', 'r')

N= int(input())
# print(N)

dp = [[0]*101 for _ in range(101)]

dir = [(1,0), (0,-1), (-1,0), (0,1)]
def make_dragon_curve(x,y,d,g, result):

    # print(f"x,y, result{x,y,g, result}" )

    
    # 끝낼 지 여부 판단
    if g == 0:
        for temp_x, temp_y in result:
            if 0<=temp_x<=100 and 0<=temp_y<=100:
                dp[temp_x][temp_y] =1
        return
    
    # 끝점찾기
    center_x, center_y = result[-1]
    # print("center",center_x, center_y )

    new_result = []
    for i in range(len(result)-2, -1, -1):
        temp_x, temp_y = result[i]
        temp_x, temp_y  = temp_x-center_x, temp_y-center_y #중심좌표 이동
        temp_x, temp_y = -temp_y, temp_x # 90도 회전
        temp_x, temp_y = temp_x+center_x, temp_y+center_y #원상복구
        new_result.append((temp_x, temp_y))

    new_result =  result +new_result
    
    make_dragon_curve(x,y, d, g-1, new_result)

# make_dragon_curve(0,0,0,3, [(0,0),(1,0)])

# # print("dp", dp)

for _ in range(N):
    x,y,d,g = map(int, input().split())
    # print(x,y,d,g)
    # 드래곤 커브 생성
    end_x, end_y = x + dir[d][0], y + dir[d][1]
    make_dragon_curve(x,y,d,g, [(x,y), (end_x, end_y)])
    
# # print(dp)

answer = 0
for i in range(100):
    for j in range(100):
        if dp[i][j] == 1 and dp[i + 1][j] == 1 and dp[i][j + 1] == 1 and dp[i + 1][j + 1] == 1:
            answer += 1
print(answer)




