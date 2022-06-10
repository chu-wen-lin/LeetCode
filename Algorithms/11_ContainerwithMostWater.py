class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers
        # time: O(N)  雙指針遍歷一遍height長度
        # space: O(1)  存變量left, right, res
        # 矩形的寬 = left, right之間的距離
        # 矩形的長 ＝ min(height[i], height[j])
        # 因為面積取決於較短的高，所以移動較長的高一定沒辦法使面積更大！故我們移動較短的高，這麼做當然有可能使下一次的面積更小，但只有這樣才存在讓面積變大的可能性

        left, right = 0, len(height) - 1
        res = 0  # 目前最大的矩形面積

        while left < right:
            print(left, right)
            current_area = (right - left) * min(height[left], height[right])
            res = max(res, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res
