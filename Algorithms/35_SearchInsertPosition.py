class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Time complexity: O(logN) worst case: 折到最後一次(子array長度為1)才找到/確定沒有，則折半比對的次數為log2(N)次
        # Space complexity: O(1)
        # if nums[mid] == target, mid is exactly the position we should insert the target
        # [1,2,3,4,5,6,8,9], target = 3
        # ans is 2

        # solution 1: 可能會發生走到最後，發現left>len(nums) 且 target>nums[left]的情況，即target插入位置是在最後面，因此需再寫一個條件判斷處理
        # left, right = 0, len(nums) - 1
        #
        # while left < right:
        #     mid = left + (right - left) // 2
        #
        #     if nums[mid] == target:
        #         return mid
        #     elif target > nums[mid]:
        #         left = mid + 1  # the insertion position should be "at least at mid + 1", because it can be even larger
        #     elif target < nums[mid]:
        #         right = mid  # the insertion position should be "at most at mid", mid can be the potential candidate
        #
        # return left+1 if target > nums[left] else left


        # solution 2: 一開始就調整right指針的位置
        left, right = 0, len(nums)  # not len(nums) - 1, as we might need to insert at the end of nums!!!
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
