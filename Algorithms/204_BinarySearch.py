class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 一開始left、right就要用index，而不是值本身。不然找到target後return沒辦法取到index
        left, right = 0, len(nums)  # right不能用-1，因為需要找mid（left+right），負的index沒辦法找mid
        while left < right:
            mid = (left + right) // 2  # 奇數個正中間的index 或 偶數個中間偏左的index
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1
        return -1
