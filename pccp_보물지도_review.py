# 아이템써서 갈수 있는 곳 만들기 
def make_case(x,y, grid, n, m):
    dx = [2,-2,0,0]
    dy = [0,0,2,-2]
    result = []
    for k in range(4):
        new_x, new_y = x + dx[k], y + dy[k]
        if 1<= new_x < n+1 and 1<= new_y < m+1 and grid[new_x][new_y] ==0:
            result.append((new_x, new_y))
    
    return result
    
def solution(n, m, hole):
    import collections
    
    # 초기 선언
    grid = [[0]*(m+1) for _ in range(n+1)]
    for x, y in hole:
        grid[x][y] =1 # 홀 위치 기록
    # print("grid", grid)
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = collections.deque()
    visited = [[[0]*2 for _ in range(m+1)] for _ in range(n+1)]
    x,y, dist, ch = 1,1,0,0
    q.append((x,y, dist, ch))

    # test
#     n = 4
#     m = 4
#     grid = [[0]*(m+1) for _ in range(n+1)]
#     hole = [[2,3], [3,3]]
#     for x, y in hole:
#         grid[x][y] =1 # 홀 위치 기록
    
#     case_list = make_case(1,3, grid,  4, 4) 
#     print("case_list", case_list)
    
    
    while q:
        # print("q", q)
        x,y, dist, ch = q.popleft()
        # print("x,y,dist, ch", x,y,dist, ch)
        
        # 결과 도출
        if (x,y) == (n, m) and ch ==1: # 아이템 쓰고 도착했을경우
            return dist

        
        for k in range(4): # 한칸 가는거 계산
            new_x, new_y = x + dx[k], y +dy[k]
            if 1<=new_x< n+1 and 1<=new_y< m+1 and grid[new_x][new_y] == 0 and visited[new_x][new_y][ch] == 0:
                visited[new_x][new_y][ch] =1
                q.append((new_x, new_y, dist+1, ch))
                    
        if ch == 0: #아이템 안쓴애들만 써보자
            caselist = make_case(x,y, grid, n, m) ## x,y에서 갈수 있는 곳 구현
            for new_x, new_y in caselist: #갈수 있는 리스트
                if 1<=new_x< n+1 and 1<=new_y< m+1 and visited[new_x][new_y][1] == 0:
                    visited[new_x][new_y][1] = 1
                    q.append((new_x, new_y, dist+1, 1))
                    
    return -1 # 아무리 돌려도 안됐을때 -1리턴
    