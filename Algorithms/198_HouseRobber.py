class Solution:
    def rob(self, nums: List[int]) -> int:
        # 對每一個位置來說，可以選擇:
        # 1. 不搶該家、到下家搶
        # 2. 搶該家、到下下家搶
        # 對每個位置來說可以搶到的最大值：max(現在這家+前前家可以拿到的最大值, 前一家可以拿到的最大值+現在這家不搶)

        # Solution 1: Iterative + memo (bottom-up)
        # Time Complexity: O(N)
        # Space Complexity: O(N), required for memo
        n = len(nums)

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums)

        #         memo = [0] * n
        #         memo[0]= nums[0]   # 對第一個位置來說，能搶到的最大值就是第一家
        #         memo[1] = max(nums[0], nums[1])  # 對第二個位置來說，能搶到的最大值是第一家或第二家

        #         for i in range(2, n):
        #             memo[i] = max(nums[i] + memo[i-2], memo[i-1])

        #         return memo[-1]

        # Solution 2: Iterative + variables (bottom-up, space-Optimized)
        # Time Complexity: O(N)
        # Space Complexity: O(1) 計算當前位置最大值，只需要前一個位置最大值和前前位置的最大值

        cur_max, prev_1, prev_2 = 0, 0, 0

        for i in range(n):
            cur_max = max(nums[i] + prev_2, prev_1)

            prev_2 = prev_1
            prev_1 = cur_max

        return cur_max



