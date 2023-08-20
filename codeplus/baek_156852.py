#하나만잘하면된다..
import sys
sys.setrecursionlimit(10**9)
sys.stdin= open('input_15685.txt', 'r')

N= int(input())
# print(N)

dp = [[0]*101 for _ in range(101)]

dir = [(1,0), (0,-1), (-1,0), (0,1)]
def make_dragon_curve(x,y,d,g, result):

    print(f"x,y, result{x,y,g, result}" )

    
    # 끝낼 지 여부 판단
    
        
    
    # 끝점찾기
    center_x, center_y = result[-1]
    # max_dist = 0
    # end_x, end_y = x, y 
    # for temp_x, temp_y in result:
    #     dist = (x-temp_x)**2 + (y-temp_y)**2
    #     if dist > max_dist:
    #         max_dist = dist
    #         end_x, end_y = temp_x, temp_y

    # print('끝점', end_x, end_y)
    

    center_x, center_y = end_x, end_y #중심 좌표 설정

    new_result = set()
    for temp_x, temp_y in result: #모든점 회전이동
        temp_x, temp_y  = temp_x-center_x, temp_y-center_y
        temp_x, temp_y = -temp_y, temp_x #90도 회전
        temp_x, temp_y = temp_x+center_x, temp_y+center_y
        new_result.add((temp_x,temp_y))
    # print(new_result)
    flag = False
    for temp_x, temp_y in new_result:
        if temp_x <0 or temp_x > 100 or temp_y <0 or temp_y > 100:
            # 지금까지 해놓은 것들 다 기록하고 끝냄
            flag = True
            break
    if flag == True:
        for temp_x, temp_y in result:
            dp[temp_x][temp_y] =1
        return
    
    new_result = new_result | result
    


    make_dragon_curve(x,y, d, g-1, new_result)

# make_dragon_curve(3,3,0,1, {(3,3),(4,3)})

# # print("dp", dp)

for _ in range(N):
    x,y,d,g = map(int, input().split())
    # print(x,y,d,g)
    # 드래곤 커브 생성
    end_x, end_y = x + dir[d][0], y + dir[d][1]
    make_dragon_curve(x,y,d,g, {(x,y), (end_x, end_y)})
    
    
    

# # print(dp)

answer = 0
for i in range(100):
    for j in range(100):
        if dp[i][j] == 1 and dp[i + 1][j] == 1 and dp[i][j + 1] == 1 and dp[i + 1][j + 1] == 1:
            answer += 1
print(answer)




