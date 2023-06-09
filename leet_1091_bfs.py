from typing import List
import collections


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        # 시작과 끝이 1이 아닌경우만 탐색

        dx = [1, -1, 0, 0, 1, 1, -1, -1]
        dy = [0, 0, 1, -1, 1, -1, 1, -1]

        visited = [[0]*n for _ in range(n)]
        dp = [[float('inf')]*n for _ in range(n)]
        q = collections.deque()

        # state initialize
        visited[0][0] = 1
        dp[0][0] = 1
        q.append((0, 0))

        while q:
            x, y = q.popleft()
            for k in range(8):
                new_x, new_y = x + dx[k], y + dy[k]
                if 0 <= new_x < n and 0 <= new_y < n and visited[new_x][new_y] == 0 \
                        and grid[new_x][new_y] == 0:
                    # 방문기록
                    visited[new_x][new_y] = 1
                    # 최소거리 갱신
                    dp[new_x][new_y] = min(dp[new_x][new_y], dp[x][y]+1)
                    # 큐에 원소 추가
                    q.append((new_x, new_y))

        if dp[n-1][n-1] == float('inf'):
            return -1
        else:
            return dp[n-1][n-1]


grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
a = Solution()
a.shortestPathBinaryMatrix(grid)
