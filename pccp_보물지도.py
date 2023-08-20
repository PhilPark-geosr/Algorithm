def solution(n, m, hole):
    import collections
    # make a grid
    grid = [[0]*m for _ in range(n)]

    # hole 위치 입력
    for a, b in hole:
        grid[a-1][b-1] =1

    # visited 구성
    # visited[i][j][0] : i, j를 아이템 안쓰고 방문했어? 
    # visited[i][j][1] : i, j를 아이템 쓰고 방문했니?
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    distance = [[[float('inf')]*2 for _ in range(m)] for _ in range(n)]

    
    q = collections.deque()
    q.append((0,0, 0)) #(i, j, 아이템썻는지 유무)
    visited[0][0][0] =1 # 아이템 안쓰고 (0,0 방문)
    distance[0][0][0] = 0
    dx = [1,-1, 0, 0]
    dy = [0, 0, 1,-1]
    while q:
        # print(q)
        x, y, used = q.popleft()

        if used == 0: # 아이템 써서 방문한 곳이면, 나머지는 그냥 가야됨
            for k in range(4):
                new_x, new_y = x + 2*dx[k], y + 2*dy[k] #두칸씩
                if 0<=new_x < n and 0<=new_y<m and visited[new_x][new_y][1] == 0 and grid[new_x][new_y] ==0:
                    visited[new_x][new_y][1] = 1 #방문처리
                    distance[new_x][new_y][1] = min(distance[new_x][new_y][1], distance[x][y][0] + 1)
                    q.append((new_x, new_y, 1)) #아이템 썻으니까 처리해주자

            for k in range(4):
                new_x, new_y = x + dx[k], y + dy[k]
                # 일단 한번 간거는 그냥 체크해주고
                if 0<=new_x < n and 0<=new_y<m and visited[new_x][new_y][used] == 0 and grid[new_x][new_y] ==0:
                    visited[new_x][new_y][0] = 1 #방문처리
                    distance[new_x][new_y][0] = min(distance[new_x][new_y][0], distance[x][y][0] + 1)
                    q.append((new_x, new_y, used))
        else: #used == 1 즉 신발 쓴 좌표들.. 한칸씩 밖에 못간다
            for k in range(4):
                new_x, new_y = x + dx[k], y + dy[k]
                # 일단 한번 간거는 그냥 체크해주고
                if 0<=new_x < n and 0<=new_y<m and visited[new_x][new_y][1] == 0 and grid[new_x][new_y] ==0:
                    visited[new_x][new_y][1] = 1 #방문처리
                    distance[new_x][new_y][1] = min(distance[new_x][new_y][1], distance[x][y][1] + 1)
                    q.append((new_x, new_y, 1))
            

    if distance[n-1][m-1][1] != float('inf'):
        return distance[n-1][m-1][1]
    
    else:
        return -1
    
    


    
   