class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Two pointer: fast and slow
        # fast持續一次動一格，交換條件是當slow位置為0、fast位置不為0時
        # 對slow來說，若他的位置為0，則須等待fast位置不為0才能交換；若他的位置不為0，則沒有元素需要交換、不需等待交換時機，slow往後一格。
        # Time complexity: O(N) fast一定會走完整個nums（slow則不一定。e.g. [0,0,0則slow一直停在index=0）
        # Space complexity: O(1)

        slow = 0
        for fast in range(len(nums)):
            # 當fast走到非0時，slow又為0可以換時，就交換
            if nums[fast] != 0 and nums[slow] == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]  # slow所在位子變成非0、fast所在位置變成0

            if nums[slow] != 0:
                slow += 1
