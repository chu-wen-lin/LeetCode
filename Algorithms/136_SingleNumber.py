class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # ^(XOR)：只有在一個位元為0、另一個位元為1時，才會為1。0 ^ 0 = 0、1 ^ 1 = 0
        # a ^ a = 0 ;  a ^ 0 = a

        res = 0
        for n in nums:
            res = res ^ n
            print(res)
        return res
