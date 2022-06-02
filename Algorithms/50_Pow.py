class Solution:
    # def myPow(self, x, n):    # solution 1 - recursive: time: O(logN) space:O(logN)
    #         if n == 0:
    #             return 1

    #         if n < 0: # dealing with negative power
    #             return self.myPow(1/x, -n)
    #         if n % 2:  # odd power
    #             return x * self.myPow(x, n - 1)
    #         else: # even power
    #             return self.myPow(x * x, n / 2)`

    def myPow(self, x, n):  # solution 1 - iterative: time: O(logN) space:O(1)
        if n < 0:  # negative power
            x = 1 / x
            n = -n

        ans = 1
        while n:
            if n % 2:  # odd power
                ans *= x
            x *= x
            n //= 2
        return ans
