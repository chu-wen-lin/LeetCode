class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:  # n == 0時是False，不會進while
            n = n & (n - 1)
            count += 1
        return count
