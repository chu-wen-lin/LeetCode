class Solution:
    def convertToBase7(self, num: int) -> str:
        # 7進位制的意思即個位數為幾倍的7^0、十位數為幾倍的7^1、百位數為幾倍的7^2⋯⋯
        # 因此第一次取floor的餘數即為個位數，若商數小於7則為十位數！若大於等於7則繼續除，這次的餘數為十位數，商若大於7則繼續除。以此類推
        # solution 1: recursive
        # Time Complexity: O(log_{7}^{N})
        # Space Complexity: O(log_{7}^{N})  recursion的深度

        # if num < 0:
        #     return "-" + self.convertToBase7(-num)
        #
        # if not num:  # num == 0
        #     return str("0")
        #
        # if num < 7:
        #     return str(num)
        #
        # quotient, remainder = divmod(num, 7)
        # return self.convertToBase7(quotient) + str(remainder)

        # solution 2: iterative
        # Time Complexity: O(log_{7}^{N})
        # Space Complexity: O(1)
        abs_num = abs(num)
        res = ""

        while abs_num != 0:
            res = str(abs_num % 7) + res
            abs_num //= 7

        return "-" * (num < 0) + res if res else "0"
