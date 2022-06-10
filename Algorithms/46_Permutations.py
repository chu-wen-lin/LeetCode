class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time complexity: O(N!)
        # Space complexity: O(N)
        res = []
        sub_res = []
        n = len(nums)
        used = [False] * n

        def backtrack(used: List[bool]):
            if len(sub_res) == n:
                res.append(sub_res.copy())
                # 因為sub_res的值在recursion的過程中會一直被改變
                # 若直接append sub_res，則res裡的全部元素id會指到跟當前的sub_res同一個記憶體位置（即res裡全部的元素一起被修改）最終回傳結果是[[],[],[]...]
                return

            for i in range(len(nums)):
                if not used[i]:
                    sub_res.append(nums[i])
                    used[i] = True
                    backtrack(used)
                    ele = sub_res.pop()
                    # print(ele, sub_res)
                    used[i] = False
                    # print(nums[i], used[i])

        backtrack(used)

        return res
