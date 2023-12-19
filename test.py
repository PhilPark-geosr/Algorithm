import collections
def solution(board):
    N = len(board)
    # bfs 
    visited = [[[[0]*N for _ in range(N)] for _ in range(N)] for _ in range(N)]
    q = collections.deque()
    dx = [1,-1,0,0]
    dy = [-0,0,1,-1]
    # 초기화
    visited[0][0][0][1] = 1
    # (dist, x1, y1, x2, y2)
    q.append((0, 0, 0, 0, 1))
    answer = 0
    while q:
        dist, x1,y1, x2, y2 = q.popleft()
        
        if (x1,y1) == (N-1, N-1) or (x2, y2) == (N-1, N-1):
            answer = dist
            break
        
        # 상하좌우 이동
        for k in range(4):
            new_x1, new_y1, new_x2, new_y2 = x1 + dx[k], y1 + dy[k], x2 + dx[k], y2+dy[k]
            if 0<=new_x1<N and 0<=new_y1<N and 0<=new_x2<N and 0<=new_y2<N \
            and visited[new_x1][new_y1][new_x2][new_y2] == 0 and board[new_x1][new_y1] == 0 and board[new_x2][new_y2] == 0:
                visited[new_x1][new_y1][new_x2][new_y2] =1
                q.append((dist+1, new_x1, new_y1, new_x2, new_y2))
                
        # 회전이동
        # x1,y1 
        vec_x, vec_y = x2-x1, y2-y1
        # 반시계
        if (vec_x, vec_y) ==(1,0):
            if board[x1+1][y1+1] ==0: #이때만 회전
                new_x1, new_y1 = x1, y1
                new_x2, new_y2 = 0+ x1,1 +y1                
                
        elif (vec_x, vec_y) ==(0,1):
            if board[x1-1][y1+1] ==0:
                new_x1, new_y1 = x1, y1
                new_x2, new_y2 = -1+ x1, 0 +y1
                
        elif (vec_x, vec_y) ==(-1,0):
            if board[x1-1][y1-1] ==0:
                new_x1, new_y1 = x1, y1
                new_x2, new_y2 = 0+ x1, -1 +y1
            
        else: #(vec_x, vec_y) ==(0,-1):
            if board[x1+1][y1-1] ==0:
                new_x1, new_y1 = x1, y1
                new_x2, new_y2 = 1 + x1, 0 +y1 
                
        if 0<=new_x1<N and 0<=new_y1<N and 0<=new_x2<N and 0<=new_y2<N \
            and visited[new_x1][new_y1][new_x2][new_y2] == 0 and board[new_x1][new_y1] == 0 and board[new_x2][new_y2] == 0:
                visited[new_x1][new_y1][new_x2][new_y2] =1
                q.append((dist+1, new_x1, new_y1, new_x2, new_y2))
                
        
        # vec_x, vec_y = x2-x1, y2-y1
        # 시계
        if (vec_x, vec_y) ==(1,0):
            if board[x1+1][y1-1] ==0: #이때만 회전
                new_x1, new_y1 = x1, y1
                new_x2, new_y2 = 0 + x1,-1+ y1
                
                
        elif (vec_x, vec_y) ==(0,1):
            if board[x1+1][y1+1] ==0:
                new_x1, new_y1 = x1, y1
                new_x2, new_y2 = 1 + x1,0 + y1
                
        elif (vec_x, vec_y) ==(-1,0):
            if board[x1-1][y1+1] ==0:
                new_x1, new_y1 = x1, y1
                new_x2, new_y2 = 0 + x1, 1 + y1
            
        else: #(vec_x, vec_y) ==(0,-1):
            if board[x1-1][y1-1] ==0:
                new_x1, new_y1 = x1, y1
                new_x2, new_y2 = -1 + x1, 0 + y1
                
        if 0<=new_x1<N and 0<=new_y1<N and 0<=new_x2<N and 0<=new_y2<N \
            and visited[new_x1][new_y1][new_x2][new_y2] == 0 and board[new_x1][new_y1] == 0 and board[new_x2][new_y2] == 0:
                visited[new_x1][new_y1][new_x2][new_y2] =1
                q.append((dist+1, new_x1, new_y1, new_x2, new_y2))
        
        # x1,y1, x2, y2 스왑
        x1,y1, x2,y2 = x2,y2, x1,y1
        vec_x, vec_y = x2-x1, y2-y1
        # 반시계
        if (vec_x, vec_y) ==(1,0):
            if board[x1+1][y1+1] ==0: #이때만 회전
                new_x1, new_y1 = x1, y1
                new_x2, new_y2 = 0+ x1,1 +y1                
                
        elif (vec_x, vec_y) ==(0,1):
            if board[x1-1][y1+1] ==0:
                new_x1, new_y1 = x1, y1
                new_x2, new_y2 = -1+ x1, 0 +y1
                
        elif (vec_x, vec_y) ==(-1,0):
            if board[x1-1][y1-1] ==0:
                new_x1, new_y1 = x1, y1
                new_x2, new_y2 = 0+ x1, -1 +y1
            
        else: #(vec_x, vec_y) ==(0,-1):
            if board[x1+1][y1-1] ==0:
                new_x1, new_y1 = x1, y1
                new_x2, new_y2 = 1 + x1, 0 +y1 
                
        if 0<=new_x1<N and 0<=new_y1<N and 0<=new_x2<N and 0<=new_y2<N \
            and visited[new_x1][new_y1][new_x2][new_y2] == 0 and board[new_x1][new_y1] == 0 and board[new_x2][new_y2] == 0:
                visited[new_x1][new_y1][new_x2][new_y2] =1
                q.append((dist+1, new_x1, new_y1, new_x2, new_y2))
                
        
        # vec_x, vec_y = x2-x1, y2-y1
        # 시계
        if (vec_x, vec_y) ==(1,0):
            if board[x1+1][y1-1] ==0: #이때만 회전
                new_x1, new_y1 = x1, y1
                new_x2, new_y2 = 0 + x1,-1+ y1
                
                
        elif (vec_x, vec_y) ==(0,1):
            if board[x1+1][y1+1] ==0:
                new_x1, new_y1 = x1, y1
                new_x2, new_y2 = 1 + x1,0 + y1
                
        elif (vec_x, vec_y) ==(-1,0):
            if board[x1-1][y1+1] ==0:
                new_x1, new_y1 = x1, y1
                new_x2, new_y2 = 0 + x1, 1 + y1
            
        else: #(vec_x, vec_y) ==(0,-1):
            if board[x1-1][y1-1] ==0:
                new_x1, new_y1 = x1, y1
                new_x2, new_y2 = -1 + x1, 0 + y1
                
        if 0<=new_x1<N and 0<=new_y1<N and 0<=new_x2<N and 0<=new_y2<N \
            and visited[new_x1][new_y1][new_x2][new_y2] == 0 and board[new_x1][new_y1] == 0 and board[new_x2][new_y2] == 0:
                visited[new_x1][new_y1][new_x2][new_y2] =1
                q.append((dist+1, new_x1, new_y1, new_x2, new_y2))
            
            
        
    
    return answer
            
        

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))