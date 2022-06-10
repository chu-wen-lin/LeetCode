class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # time complexity: O(C(n, k))
        # space complexity: O(k)
        res = []
        sub_res = []

        def backtrack(start):
            if len(sub_res) == k:
                res.append(sub_res.copy())
                # 因為sub_res的值在recursion的過程中會一直被改變
                # 若直接append sub_res，則res裡的全部元素id會指到跟當前的sub_res同一個記憶體位置（即res裡全部的元素一起被修改）
                return

            for i in range(start, n + 1):
                sub_res.append(i)
                backtrack(i + 1)
                sub_res.pop()

        backtrack(1)

        return res

        # use built-in function
        # from itertools import combinations
        # return list(combinations(range(1, n+1), k))
