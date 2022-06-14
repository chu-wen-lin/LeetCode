class Solution:
    def reverseWords(self, s: str) -> str:
        # Solution 1: built-in string manipulation function
        # s = s.split()
        # for i, char in enumerate(s):
        #     s[i] = char[::-1]
        # return ' '.join(s)

        # Solution 2: two-pointers implementation, reverse each word within the string
        # Time complexity: O(N)
        # Space complexity: O(1)
        left = 0
        right = 0

        while right <= len(s):    # 把r == len(s)寫在s[r] == " "之前，就不會造成最後一個字list index out of range!
            if right == len(s) or s[right] == ' ':  # right pointer reached the end or reached whitespace
                s = s[:left] + s[left:right][::-1] + s[right:]  # reverse s[left:right]
                right += 1
                left = right  # advance left to the start of next word
            else:  # right pointer keeps moving forward until it reaches whitespace or the end
                right += 1

        return s
