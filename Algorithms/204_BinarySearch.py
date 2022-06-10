class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:  # 沒有等於的話，當array中僅有一元素時(e.g. [[2]])會出錯
            mid = (left + right) // 2  # 奇數個正中間的index 或 偶數個中間偏左的index
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid -1
            elif target > nums[mid]:
                left = mid + 1
        return -1
