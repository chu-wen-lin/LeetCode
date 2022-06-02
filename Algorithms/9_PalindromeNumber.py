class Solution:
    def isPalindrome(self, x: int) -> bool:
        # base case:
        # negative integers or integer ends with 0 (but not 0)
        # will never be palindrome
        if x < 0 or (x > 0 and x % 10 == 0):
            return False

        # solution 1: convert to string and check each character with two pointer methods
        #         x = str(x)
        #         left = 0
        #         right = len(x) - 1

        #         while left <= right:
        #             if x[left] == x[right]:
        #                 left += 1
        #                 right -= 1
        #             else:
        #                 return False
        #         return True

        # solution 2: compare x with a new number in reverse order
        #         inputx = x
        #         newNum = 0
        #         while inputx > 0:
        #             newNum *= 10
        #             newNum += inputx % 10
        #             inputx //= 10

        #         return x == newNum

        # improved solution 2: just convert half of the integer and then check if it's palindrome

        half_rev = 0
        while x > half_rev:
            half_rev = half_rev * 10 + x % 10
            x = x // 10

        return x == half_rev or x == half_rev // 10
        # even length int: x and half_rev are the same;
        # odd length int: x == half_rev // 10 (e.g. x=1, half_rev=12)
