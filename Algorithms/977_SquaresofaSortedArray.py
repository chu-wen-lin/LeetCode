class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # solution 1：一次動兩個pointer，最後left可能和right交錯，所以還要多加一個if判斷
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

        # solution 2: 即使遇到左右值一樣大，也只能一次動一個（預設先塞右邊的進去res）

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
