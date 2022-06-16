class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a dictionary called seen to record the last occurrence(index) of chr according to right pointer
        # If chr not in seen, keep moving right pointer, keep renewing the window size and keep storing their index into seen
        # If chr in seen, (1) if seen[chr] is not in sliding window -> have no effect on current size of longest string, so just renew the index of chr
        #                 (2) if seen[chr] is in sliding window -> shrink the window size by moving the left pointer to seen[chr]+1 and renew the index of chr

        # Time Complexity: O(N)
        # Space Complexity: O(N)  If all the characters in the input string are unique, len(seen) == len(s)

        left, right = 0, 0
        res = 0  # record current longest length of substring
        seen = {}

        while right < len(s):
            cur_chr = s[right]
            if cur_chr not in seen:
                res = max(res, right-left+1)
            else:
                if right > seen.get(cur_chr) >= left:   # repeated chr in sliding window
                    left = seen.get(cur_chr) + 1
                else:
                    res = max(res, right-left+1)
            seen[cur_chr] = right
            right += 1

        return res

