class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] : i,j로 도달하는 경우의 수
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]

        dp=[[-1]*(n) for _ in range(m)]

        def dfs(i, j):
            if i< 0 or j <0:
                return 0
            if (i, j) == (0,0):
                return 1
            if dp[i][j] !=-1:
                return dp[i][j]

            dp[i][j] = dfs(i-1, j) + dfs(i, j-1)    
            return dp[i][j]   



        #정답
        return dfs(m-1, n-1)


a = Solution()
print(a.uniquePaths(3, 7))