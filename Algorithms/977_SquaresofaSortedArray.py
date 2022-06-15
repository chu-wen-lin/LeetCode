class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Solution 1：一次動兩個pointer，最後left可能和right交錯，所以還要多加一個if判斷
        #         left, right = 0, len(nums) - 1
        #         res = []

        #         while left < right:
        #             if abs(nums[left]) > abs(nums[right]):
        #                 res.insert(0, nums[left] ** 2)
        #                 left += 1
        #             elif abs(nums[left] < abs(nums[right])):
        #                 res.insert(0, nums[right] ** 2)
        #                 right -= 1

        #             else:
        #                 res.insert(0, nums[left] ** 2)
        #                 res.insert(0, nums[right] ** 2)
        #                 left += 1
        #                 right -= 1

        #         if left == right:
        #             res.insert(0, nums[left] ** 2)
        #         return res

        # Solution 2: 即使遇到左右值一樣大，也只能一次動一個（預設先塞右邊的進去res）
        # Time Complexity: O(N)  worst case: 平方(或取絕對值)後數列是呈現單調遞增或單調遞減
        # e.g.[-4, -3, -2, -1, 0] 只有left會動，從頭走到尾 / [1, 2, 3, 4, 5] 只有right會動，從尾走到頭
        # Space Complexity: O(N) res的長度會隨著輸入nums的長度改變

        left, right = 0, len(nums) - 1
        res = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res.insert(0, nums[left] ** 2)
                left += 1
            else:
                res.insert(0, nums[right] ** 2)
                right -= 1
        return res
