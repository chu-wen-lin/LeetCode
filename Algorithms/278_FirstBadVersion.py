# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2
            print(left, mid, right)
            if isBadVersion(mid):  # returns true means bad version
                right = mid
            else:
                left = mid + 1

        return left
