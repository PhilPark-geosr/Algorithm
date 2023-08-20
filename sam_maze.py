import sys
sys.stdin = open('input_maze.txt')
input = sys.stdin.readline

N, M, K = map(int, input().split())
 
dx = [1,-1,0,0]
dy = [0,0, 1,-1]

grid = []
for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)

people = []
for _ in range(M):
    a, b = map(int, input().split())
    people.append([a-1, b-1])
    grid[a-1][b-1] += -1 #사람 위치 기록


a, b = map(int, input().split())
exit = [a-1, b-1] #출구위치

#출구위치 기록
grid[exit[0]][exit[1]] =10 
# print(grid)


global total_dist
def move(people, grid, exit): #움직이자
    global total_dist
    def go_next(x,y, exit): #다음 위치 결정
        cur_dist = abs(x-exit[0]) + abs(y-exit[1])
        result = []
        for k in range(4):
            if k ==2:
                if len(result)!=0: #이미 상하에서 갈수 있는 곳이 나왔으면
                    return [result[0][0], result[0][1]]
            new_x, new_y = x +dx[k], y +dy[k]
            new_dist = abs(new_x-exit[0]) + abs(new_y- exit[1])
            if 0<=new_x<N and 0<=new_y<N and (grid[new_x][new_y]<=0 or grid[new_x][new_y]==10) and new_dist< cur_dist:
                result.append((new_x, new_y))
        if len(result) ==0: #다 돌았는데 갈데가 없으면,
            return [x,y] #원래좌표 준다
        return [result[0][0], result[0][1]]

    # 이동하면서 출구위치인 애들 찾기
    new_people = []
    for i in range(len(people)):
        x,y = people[i]
        dist = -grid[x][y]
        grid[x][y] = 0 #원래 위치 -> 빈칸
        
        new_x, new_y = go_next(x,y, exit)
        if (new_x, new_y) ==(exit[0], exit[1]): #출구에 빠지면
            # print("출구에 빠졌습니다", (x, y, new_x, new_y))
            total_dist += dist
        else:
            if (x,y) == (new_x, new_y):# 이동 없는 애들은
                grid[new_x][new_y] = -dist    
            else: #이동한 애들은
                grid[new_x][new_y] += -dist #위치 바꿔기록
                total_dist += dist
            new_people.append([new_x, new_y])

    # 다시 people로 치환
    # people = new_people
    return new_people, grid, exit
    # print("new_people", people)
    # 탈출했는지 확인

        


# 가장 작은 정사각형 길이 찾기
def find_min_rect(people, exit):
    rect_len =  float('inf')
    # 사람들 좌표를 순회하며 가장 작은 길이 출력
    for x,y in people:
        if (x,y) == (exit[0], exit[1]):
            continue
        temp = max(abs(x-exit[0]), abs(y-exit[1]))
        if temp < rect_len:
            rect_len = temp
    if rect_len == float('inf'):
        return N-1
    return rect_len

def find_rect_pos(grid, people):
    rect_len = find_min_rect(people, exit)
    # print('rect_len', rect_len)
    def check(x, y , rect_len):
        exit_flag = False
        people_flag = False
        for i in range(x, x+rect_len+1):
            for j in range(y, y+rect_len+1):
                if grid[i][j] == 10:#출구 이면
                    exit_flag = True
                if grid[i][j] <0: #사람이면
                    people_flag = True
        
                if exit_flag == True and people_flag == True:
                    return True
        if exit_flag == True and people_flag == True:
            return True
        return False

    # 가장 작은 직사각형 중 좌상단 결정
    r_x, r_y = 0,0
    for i in range(N):
        for j in range(N):
            #아래나 위가 넘어가면 패스
            # print(f"check{i,j}", grid)
            if i+ rect_len > N-1 or j + rect_len > N-1:
                continue
            if check(i, j, rect_len) == True:
                # print('출구와 사람이 동시에 있습니다')
                r_x, r_y = i,j
                return r_x, r_y, rect_len

def rotate(grid, people): # 가장 작은 정사각형 만큼 90도 회전에서 바꿔서 돌려주기
    x,y, rect_len = find_rect_pos(grid, people)

    # 임시 배열에 옮겨서 돌리고 다시 옮기는 전략
    temp = [[0]*(rect_len+1) for _ in range(rect_len+1)]
    # 원래정보 옮기기
    for i in range(rect_len+1):
        for j in range(rect_len+1):
            temp[i][j] = grid[x+i][y+j]
    n = len(temp)
    temp2 = [[0]*(n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 내구도 1씩 깍으면서 
            if 0< temp[i][j] <10 :
                temp2[j][n-1-i] = temp[i][j]-1
            else: #나머진 스킵
                temp2[j][n-1-i] = temp[i][j]


    # 90도 회전한 행렬
    # print('temp2', temp2)

    # 원래grid에 옮기기
    for i in range(rect_len+1):
        for j in range(rect_len+1):
            grid[x+i][y+j] =  temp2[i][j]

    # print('옮겨진grid', grid)



    #출구 좌표 찾기, people 다시 업데이트
    new_people = []
   
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 10:
                exit = [i,j]
            if grid[i][j] <0:
                new_people.append([i,j])
                
    return grid, exit, new_people
    
        

    # 90도 회전하기
            


            

    


# test
# move(people)
# rotate()
total_dist =0
for time in range(K):
    # print("time", time)
    if len(people) ==0: #다 탈출했으면
        # print('모든사람 탈출', time)
        break
    people, grid,exit = move(people, grid, exit)
    # print('grid, people, exit',  people,total_dist,exit)
    
    grid, exit, people = rotate(grid, people)
    # print('grid, people',people, exit)
    
    

# if len(people) !=0: #모든 참가자들의 거리 기록
#     for x,y in people:
#         dist = -grid[x][y]
#         total_dist +=dist
print(total_dist)
print(exit[0]+1, exit[1]+1)


