class Solution:
    def romanToInt(self, s: str) -> int:
        # 1. iterate string backwards to make the subtraction correct
        # 2. add current value into res if previous value <= current value;
        #    subtract when current value is < previous value
        #    e.g. "IV" --> 5-1, "IX" --> 10-1

        # Time complexity:  O(N), N is the length of the string. we go through all characters in the string
        # Space complexity: O(1) input size doesn't affect length of map_dict

        map_dict = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        res, prev = 0, 0

        for char in s[::-1]:
            cur = map_dict[char]

            if cur >= prev:
                res += cur
            else:
                res -= cur

            prev = cur

        return res
