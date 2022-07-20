from typing import List


class Solution:
    def twoSumLessThanK(self, A: List[int], K: int):
        # Time Complexity: O(NlogN) cause we need to sort A in advance
        # Space Complexity: O(1)
        max_sum = -1

        # base case
        if not A:
            return max_sum

        # In order to implement two pointer methods, we need to sort the array in advance!
        A.sort()

        left, right = 0, len(A) - 1  # two pointers point at head and tail

        while left < right:
            total = A[left] + A[right]
            if total < K:  # if current sum < K, then updates res and left++ to increase sum
                max_sum = max(max_sum, total)
                left += 1
            else:
                right -= 1  # right-- to decrease the sum

        return max_sum

    # What if we want to return [i, j] paris instead
    def twoSumLessThanK_modified(self, A: List[int], K: int):
        if not A:  # base case
            return []

        # in order to implement two pointer methods, we need to sort the array in advance
        A.sort()

        for i in range(1, K):  # Search possible answer (i+j may equals to K-1, K-2, K-3...)
            left, right = 0, len(A) - 1
            res = set()

            while left < right:
                total = A[left] + A[right]
                if total == K-i:
                    res.add((A[left], A[right]))
                    left += 1   # or right -= 1
                elif total > K-i:
                    right -= 1
                else:  # less than
                    left += 1

            if res:
                return [list(ele) for ele in res]  # return answer once we find pairs

        return []



