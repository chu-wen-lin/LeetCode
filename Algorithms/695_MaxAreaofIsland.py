class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        length = len(grid)
        width = len(grid[0])

        # 想法：兩層迴圈搜索目前最大島嶼面積

        def dfs(m: int, n: int) -> int:  # 回傳這次找到的面積
            if m < 0 or n < 0 or m >= length or n >= width:  # 超出邊界
                return 0

            if grid[m][n] == 0:  # 這裡是水(本來就是水或已經走訪過)
                return 0

            grid[m][n] = 0  # 將走訪過的陸地標記為水

            return 1 + dfs(m - 1, n) + dfs(m + 1, n) + dfs(m, n - 1) + dfs(m, n + 1)

        res = 0  # 紀錄目前最大的島嶼面積
        for m in range(length):
            for n in range(width):
                res = max(res, dfs(m, n))

        return res
