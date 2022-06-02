class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:  # 0或負數都不是2的次方數
            return False

        return n & (n - 1) == 0
