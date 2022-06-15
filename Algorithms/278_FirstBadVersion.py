# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):  # true(bad version)
                right = mid  # mid might be the first bad version
            else:  # if false(not bad version)
                left = mid + 1   # then mid will never be the first bad version, that's why I skip mid

        return left
