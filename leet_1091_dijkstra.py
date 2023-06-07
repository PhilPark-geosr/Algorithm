from typing import List
import collections
import heapq
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] ==1 or grid[n-1][n-1] ==1 :
            return -1
        # 시작과 끝이 1이 아닌경우만 탐색
        
        dx = [1,-1,0,0, 1,1, -1, -1]
        dy = [0, 0, 1,-1, 1,-1, 1, -1]
        visited = [[0]*n for _ in range(n)]
        dp = [[float('inf')]*n for _ in range(n)]
        # q = collections.deque()
        q = []
        visited[0][0] =1
        dp[0][0] =1
        heapq.heappush(q, (1, 0,0))

        while q:
            # x,y = q.popleft()
            dist, x, y = heapq.heappop(q)

            if dp[x][y] < dist:
                continue
            for k in range(8):
                new_x, new_y = x + dx[k], y + dy[k]
                if 0<=new_x<n and 0<=new_y<n and visited[new_x][new_y] ==0 \
                and grid[new_x][new_y] ==0:
                    visited[new_x][new_y] =1

                    new_cost = dist + 1
                    if new_cost < dp[new_x][new_y]:
                        dp[new_x][new_y] = new_cost
                        heapq.heappush(q, (new_cost, new_x, new_y))  
                    # dp[new_x][new_y] = min(dp[new_x][new_y], dp[x][y]+1)
                    # q.append((new_x, new_y))

        
        if dp[n-1][n-1] == float('inf'):
            return -1
        else:
            return dp[n-1][n-1]
                    
    