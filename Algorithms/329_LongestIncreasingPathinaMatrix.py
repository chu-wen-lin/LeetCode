class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 對每個點來說，都是檢查其沒出界的上下左右鄰居，若鄰居的值比自己大就是有效的鄰居，可以往那走！路徑長+=1
        # 需要一個m*n的2-D array來建構dp table。dp[x][y]：(x, y)作為起點的最長路徑，即鄰居中的最長路徑+自己的1步
        # dp[x][y] = 1 + max(dp[x-1][y], dp[x][y-1], dp[x+1][y], dp[x][y+1])

        # Time complexity: O(m*n) 共m*n的點，每一個點都需要走訪，每一個點找左右鄰居最大值+1這個動作的複雜度是O(1)
        # Space complexity: O(m*n)  dfs的recursion深度，worst case需要搜到底才會return
        # 1 2 3
        # 2 3 4
        # 3 4 5

        m = len(matrix)
        n = len(matrix[0])
        if m == 1 and n == 1:    # [[0]] 的路徑長也是1!
            return 1

        dp = [[-1] * n for _ in range(m)]
        ans = 0

        def dfs(x: int, y: int):
            if dp[x][y] != -1:  # (x, y)已經被走過
                return dp[x][y]

            # 檢查(x, y)的上下左右鄰居是否出界、比自己的值大！
            cur_val = matrix[x][y]

            # 上
            if x - 1 >= 0 and cur_val < matrix[x - 1][y]:
                up = dfs(x - 1, y)
            else:
                up = 0

            # 下
            if x + 1 < m and cur_val < matrix[x + 1][y]:
                down = dfs(x + 1, y)
            else:
                down = 0

            # 左
            if y - 1 >= 0 and cur_val < matrix[x][y - 1]:
                left = dfs(x, y - 1)
            else:
                left = 0

            # 右
            if y + 1 < n and cur_val < matrix[x][y + 1]:
                right = dfs(x, y + 1)
            else:
                right = 0

            dp[x][y] = 1 + max(up, down, left, right)

            return dp[x][y]

        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))

        return ans
