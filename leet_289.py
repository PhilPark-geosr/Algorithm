from typing import List
class Solution:

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dx = [1,-1,0,0, 1,1, -1, -1]
        dy = [0, 0, 1,-1, 1,-1, 1, -1]
        m = len(board)
        n = len(board[0])
        def check(i, j, arr: List[List[int]]):
            # (i,j) 주변의 원소들 중 1의 갯수 구하기
            count=0
            for k in range(8):
                new_i, new_j = i+dx[k], j + dy[k]
                if 0<=new_i<m and 0<=new_j<n:
                    if arr[new_i][new_j] ==1:
                        count+=1
            return count
        
        dp = [[0]*n for _ in range(m)] #dp[i][j] : (i, j)에 1몇개 있는지
        for i in range(m):
            for j in range(n):
                dp[i][j] = check(i,j,board)

        # print(dp)

        # board값 변화
        for i in range(m):
            for j in range(n):
                if board[i][j] ==1 and dp[i][j] < 2:
                    board[i][j] =0
                elif board[i][j] ==1 and dp[i][j] >3:
                    board[i][j] =0
                elif board[i][j] ==0 and dp[i][j] ==3:
                    board[i][j] =1
                else:
                    pass
        # print(board)
        

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
a = Solution()
a.gameOfLife(board)