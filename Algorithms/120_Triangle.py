class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
        # At each step, we have two choices:
        # Move to lower-left element (i + 1 and j)
        # Move to lower-right element (i + 1 and j + 1)
        # Time Complexity: O(N^2)  N is the height of triangle/len(triangle)
        # Space Complexity: O(N^2) We built a 2-D list according to triangle.

        dp = [[-1 for j in range(i + 1)] for i in range(len(triangle))]

        def dfs(i, j):
            if i == len(triangle):
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            lower_left = dfs(i + 1, j)
            lower_right = dfs(i + 1, j + 1)
            dp[i][j] = triangle[i][j] + min(lower_left, lower_right)

            return dp[i][j]

        return dfs(0, 0)
