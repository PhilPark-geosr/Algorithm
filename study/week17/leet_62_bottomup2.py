class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # make dynamic table
        dp =[[0]*n for _ in range(m)]
        
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):

                if i+1 <= m-1:
                    dp[i+1][j] += dp[i][j]
                if j+1 <= n-1:
                    dp[i][j+1] += dp[i][j]
                
        
        
        # print(dp)
        
        return dp[m-1][n-1]

a = Solution().uniquePaths(3, 7)
print(a)

