class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Time complexity: O(mn) 每一個grid只會走一次
        # Space complexity: O(mn) dp table
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # dp table的長寬都比原本的matrix多1，為了方便計算第一行和第一列的面積

        max_side = 0

        for i in range(m):
            for j in range(n):
                # if matrix[i][j] == '0': continue
                if matrix[i][j] == '1':
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i][j], dp[i + 1][j]) + 1
                    max_side = max(max_side, dp[i + 1][j + 1])
        print(dp)

        return max_side ** 2
