from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # 最左和最右兩邊的水都會流掉，這是為什麼i=0那邊不會積水的原因
        # base case: height的長度只有2（即最多只有兩根相鄰高度不為0的柱子）
        if len(height) <= 2:
            return 0

        # 1. 當i左邊最高的柱子(left_max)與右邊最高的柱子(right_max)都比height[i]還高，i才能接到雨水
        # 2. 能夠存的雨水量是min(left_max, right_max) - height[i]

        # Solution 1: brute force
        # Time complexity: O(N^2)
        # Space complexity: O(1)

        #         res = 0
        #         for i in range(len(height)):
        #             l_max, r_max = 0, 0
        #             for j in range(0, i):
        #                 l_max = max(l_max, height[j])
        #             for j in range(i, len(height)):
        #                 r_max = max(r_max, height[j])

        #             if min(l_max, r_max) > height[i]:
        #                 res += min(l_max, r_max) - height[i]

        #         return res

        # Solution 2: dynamic programming
        # 第一種方法在每一個位置i，都算i的l_max和r_max。但其實可以避免重複計算，也就是分別從最左邊開始算到當前的柱高最大值、從最右邊往回算當前柱高最大值。對每個位置i取兩者的min減去位置i的高度，即位置i可接的雨水量。這個方法降低了時間複雜度，但空間複雜度變差了，因為我們需要開兩個長度與height相同的array/list存當前柱高最大值
        # Time complexity: O(N)
        # Space complexity: O(N)

        # res = 0
        # n = len(height)
        # l_max, r_max = [height[0]] * n, [height[n - 1]] * n
        #
        # for i in range(1, len(height)):
        #     l_max[i] = max(l_max[i - 1], height[i - 1])
        #
        # for i in range(len(height) - 2, -1, -1):
        #     r_max[i] = max(r_max[i + 1], height[i + 1])
        #
        # for i in range(len(height)):
        #     if min(l_max[i], r_max[i]) > height[i]:
        #         res += min(l_max[i], r_max[i]) - height[i]
        #
        # return res

        # Solution 3: two pointers
        # Time complexity: O(N) 遍歷一遍height
        # Space complexity: O(1) 只需要額外的常數空間（只需紀錄變數res, left, right, left_max, right_max）
        # 1. 對於左指針i，它左側的最大值left_max絕對真的是左側最大，因為left_max是i一步一步走出來的；
        # 但右側的真實最大值 >= right_max，因為i不知道i和j之間是否有其他的數大於right_max
        # 2. 對於右指針j，它左側的真實最大值 >= left_max，right_max則是絕對
        # 3. 對於左指針i來說，當left_max < right_max，可以接的水量就是只受left_max影響；
        # 對於右指針j來說，當left_max >= right_max，可以接的水量就是由right_max決定
        # 4. 當left==right時，必會停在這個array的最大值（最高的柱子），而最高點是沒辦法接雨水的，所以while條件不用寫成<=

        res = 0
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                if left_max > height[left]:
                    res += left_max - height[left]

                left += 1
            else:
                if right_max > height[right]:
                    res += right_max - height[right]

                right -= 1

        return res

