class Solution:
    def reverseBits(self, n: int) -> int:

        # bit operators

        res = 0

        for i in range(32):
            if n & 1 == 1:  # n的最後一個bit是1
                res = (res << 1) + 1
            else:  # n的最後一個bit是0
                res = res << 1
            n = n >> 1

        return res
