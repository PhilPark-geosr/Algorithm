class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # make dynamic table
        dy =[[0]*n for _ in range(m)]
        

        
        # print(dy)
        for i in range(m):
        
            for j in range(n):
                # print(i,j, dy)
                if i ==0 and j ==0:
                    dy[i][j] =1
                elif i ==0 and j !=0:
                    dy[i][j] = dy[i][j-1]
                elif j == 0 and i!=0:
                    dy[i][j] = dy[i-1][j]
                else:
                    dy[i][j] = dy[i][j-1] + dy[i-1][j]
        # print(dy)
        return dy[m-1][n-1]
    


