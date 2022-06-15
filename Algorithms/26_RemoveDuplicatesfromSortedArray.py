class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        fast = 0
        slow = 0

        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        return slow + 1
