# Return the factorial(階乘) for a given number.

# Time complexity: O(len(num)) because we iterate from num, num-1, ..., 2
# Space complexity: O(1) just need to memorize variable ans while algorithm is operating
def FirstFactorial(num: int):
    ans = 1
    while num != 1:
        ans *= num
        num -= 1

    return ans


print(FirstFactorial())

