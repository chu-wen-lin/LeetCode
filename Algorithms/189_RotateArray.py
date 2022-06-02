class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # nums[:] = nums[-k:] +nums[:-k]  # k > len(nums) 時會出錯

        l = len(nums)
        k = k % l  # 當list長度大於k時，k不會改變；當list長度小於k時，k才會變

        nums[:] = nums[l - k:] + nums[:l - k]
