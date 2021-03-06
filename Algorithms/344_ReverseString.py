class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        # other solutions: use built-in functions(not recommended!)
        # s[:] = s[::-1]  #pythonic但不是in-place，右邊的list應該會暫開一個新的記憶體存，最後指回去s才釋放
        # s.reverse() #in-place

        # notes: 若傳入格式非list而是string(s: str)，則使用slicing的效率是最好的s[::-1]
        # ''.join(reversed(s)) is much slower!

