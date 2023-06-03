import sys
import collections
sys.stdin =open('input_15653.txt', 'r')

# make a grid
n, m = map(int, input().split())
# print(n, m)
grid = []
for _ in range(n):
    string = input()
    line = []
    for elem in string:
        line.append(elem)

    grid.append(line)
# print(grid)
# r_pos, b_pos intialize -> O(n^2)
for a in range(n):
    for b in range(m):
        if grid[a][b] =="R":
            r_pos = (a,b)
        elif grid[a][b] =="B":
            b_pos = (a,b)
        elif grid[a][b] == "O":
            h_pos = (a,b)
        else:
            continue
# print(r_pos, b_pos, h_pos)
#얼마나 갈수 있는지 측정      
def get_shift(i, j, grid):
    #오른쪽
    r_cnt = 0
    for k in range(j+1, m):
        if grid[i][k] == "#":
            break
        elif grid[i][k] =="O":
            r_cnt+=1
            break
        else:
            r_cnt+=1
    # 왼쪽
    l_cnt =0
    for k in range(j-1, -1, -1):
        if grid[i][k] == "#":
            break
        elif grid[i][k] =="O":
            l_cnt+=1
            break
        else:
            l_cnt+=1
    # 위
    u_cnt =0
    for k in range(i-1, -1, -1):
        if grid[k][j] == "#":
            break
        elif grid[k][j] =="O":
            u_cnt+=1
            break
        else:
            u_cnt+=1
    d_cnt =0
    for k in range(i+1, n):
        if grid[k][j] == "#":
            break
        elif grid[k][j] =="O":
            d_cnt+=1
            break
        else:
            d_cnt+=1
    return [d_cnt, -u_cnt, 0, 0], [0,0, -l_cnt, r_cnt]
    
def solution():
    q = collections.deque()
   
    #initialize q
    distance = [[float('inf')]*m for _ in range(n)]
    # visited_r = [[0]*m for _ in range(n)]
    # visited_b = [[0]*m for _ in range(n)]

    #visitied 배열 생성
    visited = [[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    q.append((r_pos[0], r_pos[1], b_pos[0], b_pos[1], 0))
    
    # visited_r[r_pos[0]][r_pos[1]] =1
    # visited_b[b_pos[0]][b_pos[1]] =1
    visited[r_pos[0]][r_pos[1]][b_pos[0]][b_pos[1]] =1
    # distance[r_pos[0]][r_pos[1]] = 0
    # distance[b_pos[0]][b_pos[1]] = 0
    
    while q:
        # print("얍",q)
        r_x, r_y, b_x, b_y, depth = q.popleft()
        # print('현재위치',r_x, r_y, b_x, b_y)
    
        # if (r_x, r_y) == h_pos and (b_x, b_y) == h_pos: ## 둘다 구멍에 들어가있을경우
        #     return -1
        # if (r_x, r_y) != h_pos and (b_x, b_y) == h_pos: #파란색만 들어가 있을 경우
        #     continue
        # if (r_x, r_y) == h_pos and (b_x, b_y) != h_pos: #빨간색만 들어가 있을 경우
        #     # print("탈출합니다")
        #     break


        dx_r, dy_r = get_shift(r_x, r_y, grid)
        dx_b, dy_b =  get_shift(b_x, b_y, grid)
        # print(dx_r, dy_r, dx_b, dy_b)

        for h in range(4):
            new_r_x, new_r_y = r_x + dx_r[h], r_y + dy_r[h]
            new_b_x, new_b_y = b_x + dx_b[h], b_y + dy_b[h]

            #기울이는 동작 그만
            # if (r_x, r_y) == (new_r_x, new_r_y) and (b_x, b_y) == (new_b_x, new_b_y) and (r_x, r_y)!=h_pos:
            #     return -1
            # print('목적지', new_r_x, new_r_y, new_b_x, new_b_y )
            if (new_r_x, new_r_y) == h_pos and (new_b_x, new_b_y) == h_pos: ## 둘다 구멍에 들어가있을경우
                continue
            if (new_r_x, new_r_y) != h_pos and (new_b_x, new_b_y) == h_pos: #파란색만 들어가 있을 경우
                continue
            if (new_r_x, new_r_y) == h_pos and (new_b_x, new_b_y) != h_pos: #빨간색만 들어가 있을 경우
                return depth+1 



            ## 목적지가 같을경우.. 먼저 굴린애가 앞에 있게
            if (new_r_x, new_r_y) == (new_b_x, new_b_y):
                # print(abs(dx_r[h]+dy_r[h]),abs(dx_b[h]+ dy_b[h]))
                # if (new_r_x, new_r_y) == h_pos: # 둘다 한번에 구멍에 들어가는 경우
                #     return -1
                if abs(dx_r[h]+dy_r[h]) < abs(dx_b[h]+ dy_b[h]): #빨간색이 이 더 앞에 있어야 함
                        diff_x = dx_b[h]//abs(dx_b[h]) if dx_b[h] !=0 else 0
                        diff_y = dy_b[h]//abs(dy_b[h]) if dy_b[h] !=0 else 0
                        new_b_x -= diff_x
                        new_b_y -= diff_y
                else:
                    diff_x = dx_r[h]//abs(dx_r[h]) if dx_r[h] !=0 else 0
                    diff_y = dy_r[h]//abs(dy_r[h]) if dy_r[h] !=0 else 0
                    new_r_x -= diff_x
                    new_r_y -= diff_y


            # print('수정된목적지', new_r_x, new_r_y, new_b_x, new_b_y )
            # print(new_r_x, new_r_y)
            if visited[new_r_x][new_r_y][new_b_x][new_b_y] ==0:
            #    and visited_r[new_r_x][new_r_y] ==0 or visited_b[new_b_x][new_b_y] ==0:
                # print('if문 진입')
                # visited_r[new_r_x][new_r_y] =1 
                # visited_b[new_b_x][new_b_y] =1
                visited[new_r_x][new_r_y][new_b_x][new_b_y] =1
                distance[new_r_x][new_r_y] = min(distance[new_r_x][new_r_y], distance[r_x][r_y] +1)
                distance[new_b_x][new_b_y] = min(distance[new_b_x][new_b_y],distance[b_x][b_y] +1)
                q.append((new_r_x, new_r_y, new_b_x, new_b_y, depth+1))
                
    return -1
    # return distance

answer = solution()
# print(answer)
if answer ==-1:
    print(-1)
else:
    print(answer)    