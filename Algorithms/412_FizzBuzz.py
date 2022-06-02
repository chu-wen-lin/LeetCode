class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # list[k]的複雜度是O(k)；但list.append()僅O(1)
        # ans = [None] * n
        ans = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                # ans[i-1] = "FizzBuzz"
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                # ans[i-1] = "Fizz"
                ans.append("Fizz")
            elif i % 5 == 0:
                # ans[i-1] = "Buzz"
                ans.append("Buzz")
            else:
                # ans[i-1] = str(i)
                ans.append(str(i))

        return ans
