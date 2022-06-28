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
                right -= 1  # right-- to decrease sum

        return max_sum


