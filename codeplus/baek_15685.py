#하나만잘하면된다..
import sys
sys.setrecursionlimit(10**9)
sys.stdin= open('input_15685.txt', 'r')

N= int(input())
# print(N)


visited = [[[0]*4 for _ in range(101)] for _ in range(101)]
visited2 = [[[0]*4 for _ in range(101)] for _ in range(101)]
dp = [[0]*101 for _ in range(101)]

def make_dragon_curve(x,y,d,g):
    if x < 0 or x> 100 or y < 0 or y> 100 or visited[x][y][d] ==1:
        return 
    # 이후 세대 생성
    print(f"dfs{x,y, d,g}")
    if d ==0:
        end_x, end_y = x + 1, y
        new_x, new_y = end_x, end_y
        new_d= 1
        new_g = g+1
    elif d==1:
        end_x, end_y = x , y -1
        new_x, new_y = end_x, end_y
        new_d= 2
        new_g = g+1
    elif d==2:
        end_x, end_y = x-1 , y
        new_x, new_y = end_x, end_y
        new_d = 3
        new_g = g+1
    else: #d ==3:
        end_x, end_y = x , y + 1
        new_x, new_y = end_x, end_y
        new_d = 0
        new_g = g+1
    # 방문기록
    dp[x][y] = 1
    dp[end_x][end_y] =1
    visited[x][y][d] =1
    make_dragon_curve(new_x, new_y, new_d, new_g)


def make_prev_dragon_curve(x,y,d,g):
    if x < 0 or x> 100 or y < 0 or y> 100 or visited2[x][y][d] ==1 or g <0:
        return 
    # 이전 세대 생성
    print(f"make_prev_dragon_curve{x,y, d,g}")
    if d ==0:
        end_x, end_y = x + 1, y
        new_x, new_y = 1 + x, 1 + y
        new_d= 1
        new_g = g-1
    elif d==1:
        end_x, end_y = x , y -1
        new_x, new_y = -1 + x, 1 + y
        new_d= 2
        new_g = g-1
    elif d==2:
        end_x, end_y = x-1 , y
        new_x, new_y = -1 +x, -1+y
        new_d = 3
        new_g = g-1
    else: #d ==3:
        end_x, end_y = x , y + 1
        new_x, new_y = -1 +x, 1+y
        new_d = 0
        new_g = g-1
    # 방문기록
    dp[x][y] = 1
    dp[end_x][end_y] =1
    visited2[x][y][d] =1
    make_prev_dragon_curve(new_x, new_y, new_d, new_g)


# print("dp", dp)
make_dragon_curve(3,3,0,1)

# # print("dp", dp)

# for _ in range(N):
#     x,y,d,g = map(int, input().split())
#     print(x,y,d,g)
#     # 드래곤 커브 생성
#     make_prev_dragon_curve(x,y,d,g)
#     make_dragon_curve(x,y,d,g)
    
    
    

# # print(dp)
# answer = 0
# for i in range(100):
#     for j in range(100):
#         count = 0
#         if dp[i][j] ==1:
#             count+=1
#         if dp[i+1][j] ==1:
#             count+=1
#         if dp[i][j+1] ==1:
#             count+=1
#         if dp[i+1][j+1] ==1:
#             count+=1
#         if count ==4:
#             answer +=1
# print(answer)




