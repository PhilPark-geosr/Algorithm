import sys
import collections
sys.stdin = open('input_9376.txt', 'r')


dx = [1,-1,0,0]
dy = [0,0, 1,-1]





T = int(input())
for t in range(T):
    
    
    N, M = map(int, input().split())
    # make grid
    grid = []
    for _ in range(N):
        line = input()
        temp = []
        for elem in line:
            temp.append(elem)
        grid.append(temp) 
       
    # print('grid', grid)
    # 맨 끝의 문 찾기

    def bfs(a, b):
        visited = [[0]*M for _ in range(N)]
        q = collections.deque()
        q.append((a,b, 0, 0, 0)) #(x,y, distance, count)
        visited[a][b] = 1

        while q:
            x, y, dist, count, prison = q.popleft()
            print(f"x,y, dist, count, prison, {x,y, dist, count, prison}")

            if prison ==2:
                break

            for k in range(4):
                new_x, new_y = x + dx[k], y+ dy[k]
                
                if 0<=new_x<N and 0<=new_y<M and visited[new_x][new_y] ==0:
                    if grid[new_x][new_y] == "#": # 문 지나면 추가
                        count+=1
                    if grid[new_x][new_y] == "$":
                        prison +=1
                    visited[new_x][new_y] =1
                    q.append((new_x, new_y, dist+1, count, prison))
        return count



    
    startlist = []
    for i in range(N):
        if grid[i][0] == "#":
            startlist.append((i,0))
        if grid[i][M-1] == "#":
            startlist.append((i,M-1))
    for j in range(1, M):
        if grid[0][j] == "#":
            startlist.append((0,j))
        if grid[N-1][j] == "#":
            startlist.append((N-1, j))
    if t ==0:
        print("startlist", startlist)
        answer = float('inf')
        for a,b in startlist:
            result = bfs(a,b)
            print("result", result)
            if result < answer:
                answer = result
        print("answer", answer)


