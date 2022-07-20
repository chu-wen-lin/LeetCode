from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(mn)
        # Space Complexity: O(mn) 最差的情況是全部的橘子都爛掉，此時queue會存m*n個座標

        m, n = len(grid), len(grid[0])
        fresh_left, time = 0, 0
        q = deque()

        # 走訪一次(m*n格)得知t=0時有幾顆新鮮橘子、幾個腐爛橘子等等要走訪（裝進queue）
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh_left += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        # 當queue不為0且尚有新鮮橘子，則將目前的座標(同一層node)pop出來，將他們四周的新鮮橘子腐爛、更新fresh_left、將被腐爛的座標裝進queue(下一層node)，該層做完則時間單位加1
        # 注意！while條件中的「尚有新鮮橘子」是為了避免最後一層橘子已被標為腐爛（全軍覆沒）、但因為同時有把他們加進queue，故queue下一次才會清空，time會多加一次
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q and fresh_left:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    if 0 <= r + dr < m and 0 <= c + dc < n and grid[r + dr][c + dc] == 1:
                        grid[r + dr][c + dc] = 2
                        fresh_left -= 1
                        q.append((r + dr, c + dc))

            time += 1

        return -1 if fresh_left else time
