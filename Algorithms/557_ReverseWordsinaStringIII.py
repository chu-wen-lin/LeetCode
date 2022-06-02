class Solution:
    def reverseWords(self, s: str) -> str:
        # solution 1: built-in string manipulation function
        # s = s.split()
        # for i, char in enumerate(s):
        #     s[i] = char[::-1]
        # return ' '.join(s)

        # solution 2: two-pointers implementation, reverse each word within string
        l = 0
        r = 0

        while r <= len(s):
            print(r)
            if r == len(s) or s[r] == ' ':  # r reached whitespace
                # reverse s[l:r] and advance l and r to the start of next word
                s = s[:l] + s[l:r][::-1] + s[r:]
                r += 1
                l = r
            else:
                r += 1

        # s = s[:l] + s[l:r][::-1]
        # 把r == len(s)寫在s[r] == " "之前，就不會造成最後一個字list index out of range!也就不用額外加這一句ㄌ
        return s
