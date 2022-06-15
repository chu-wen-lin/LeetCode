class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # (not accepted) solution 1
        # 我們發現翻轉次數k與nums長度相同時，翻轉後的nums會與原本的nums一模一樣
        # n = len(nums)
        # k = k % n  # k<n: k不會改變；k>n: k才會改變成k除以n的餘數。nums[:] = nums[-k:] +nums[:-k]  在 k > len(nums) 時會出錯
        #
        # nums[:] = nums[n - k:] + nums[:n - k] # create extra space, not in-place

        # 觀察output與input，發現可先將整個list翻轉，前後(以n-k分隔)再分別翻轉一次，共翻轉三次即得到解答
        # 1. 翻轉整個list  [7,6,5,4,3,2,1]
        # 2. 將0~k-1位置的元素翻轉 [5,6,7,4,3,2,1]
        # 3. 將k~n-1位置的元素翻轉 [5,6,7,1,2,3,4]
        # in-place：兩兩元素交換位置，用two pointer去做，每swap一次左右指標均往中間移動一格，直到兩個指標相交

        # (not accepted) solution 2: fail to rotate the original list
        #         def swap(nums: List[int]) -> None:
        #             left = 0
        #             right = len(nums) - 1

        #             while left < right:
        #                 nums[left], nums[right] = nums[right], nums[left]
        #                 left += 1
        #                 right -= 1

        #         swap(nums) #[7,6,5,4,3,2,1]
        #         swap(nums[:k])  #[5,6,7,4,3,2,1]expected 但事實上這段list的結果會另開記憶體存，不會改變原本的nums
        #         swap(nums[k:]) #[5,6,7,1,2,3,4] expected 但同上

        # solution 3: 僅傳入index，就能修改到原本的list
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        n = len(nums)
        k = k % n

        def swap(left: int, right: int):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        swap(0, n-1)
        swap(0, k-1)
        swap(k, n-1)


