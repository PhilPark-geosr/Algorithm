n = 5
grid = [[0]*(n+1) for _ in range(n+1)]
dirs = [(-1,0), (0,1), (1,0), (0,-1)]
f_dirs = [[0]*(n+1) for _ in range(n+1)] # 정방향 기록
r_dirs = [[0]*(n+1) for _ in range(n+1)] # 역방향 기록

def is_range(x,y):
    if 1<=x<=n and 1<=y<=n:
        return True
    return False

def make_forward():
    x,y = (n+1)//2, (n+1)//2
    d = 0
    cnt = 0
    grid[x][y] = cnt # 값 기록
    f_dirs[x][y] = 0 # 방향 기록
    dist = 1
    while True:
        for _ in range(2):
            for _ in range(dist):
                cnt+=1
                new_x, new_y = x + dirs[d][0], y + dirs[d][1]
                if is_range(new_x, new_y) == False:
                    return
                grid[new_x][new_y] = cnt
                f_dirs[new_x][new_y] = d
                x, y = new_x, new_y #좌표 이동
            #꺽기 전에 방향 기록
            d = d+1 if d<3 else 0
            f_dirs[x][y] = d
        dist += 1

make_forward()
print(grid)
print(f_dirs)

grid2 = [[0]*(n+1) for _ in range(n+1)]
visited =  [[0]*(n+1) for _ in range(n+1)]
def make_reverse():
    x,y = 1,1
    d = 2
    cnt = 0
    grid2[x][y] = cnt
    visited[x][y] = 1 #방문 기록
    r_dirs[x][y] = d #방향 기록

    while True:
        if (x,y) ==((n+1)//2, (n+1)//2):
            return
        new_x, new_y = x + dirs[d][0], y + dirs[d][1]
        if is_range(new_x, new_y) == False: # 방향 바꾼다
            d = d-1 if d>0 else 3
            r_dirs[x][y] = d #방향 바꾼거 기록해둔다
            continue
        if visited[new_x][new_y] ==1:
            d = d - 1 if d > 0 else 3
            r_dirs[x][y] = d  # 방향 바꾼거 기록해둔다
            continue
        # 방문 안한곳은 갈 수 있다
        cnt+=1
        visited[new_x][new_y] =1 #방문기록
        grid2[new_x][new_y] = cnt
        r_dirs[new_x][new_y] = d
        x, y = new_x, new_y

make_reverse()
print("grid2", grid2)
print("r_dirs", r_dirs)



