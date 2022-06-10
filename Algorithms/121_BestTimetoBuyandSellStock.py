class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        # [9, 10, 1] -> profit: 1
        # 買一定要發生在賣之前
        # 對每個位置i的數來說，最大獲利 = 目前價錢(prices[i]) - 前面出現的最低價格
        # ans存當前最大獲利

        # solution 1: brute force
        # time:O(N^2) space: O(1)

        #         ans = 0

        #         for i in range(len(prices)):
        #             for j in range(i+1,len(prices)):
        #                 ans = max(ans, prices[j] - prices[i])

        #         return ans

        # solution 2: dynamic programming
        # dp[i] = max(dp[i - 1], prices[i] - min_price)
        # time: O(N) space: O(N) dp table

        #         dp = [0] * len(prices)  # dp[i]即第i+1天的最大獲利
        #         min_price = prices[0]

        #         for i in range(len(prices)):
        #             # 第i天時不交易，獲利即前一天的最大獲利 或 用price[i]賣出成本為min_price的股票
        #             dp[i] = max(dp[i - 1], prices[i] - min_price)
        #             min_price = min(min_price, prices[i])

        #         return dp[-1]

        # solution 3: dp的空間優化版本
        # time: O(N) N 是prices的長度
        # space: O(1) 只需額外空間儲存變數

        buy, ans = float('inf'), 0
        for p in prices:
            # ans = max(ans, p - buy)  # profit要用上一回的買入價格計算，故ans要比buy早更新。以i的價錢賣出和之前的最大獲利比是否可以獲得更高的獲利
            # buy = min(buy, p)  # 找最低買進價格，最終一定會更新成數組中最小的數
            # 也可以用swap較簡潔
            ans, buy = max(ans, p - buy), min(buy, p)
        return ans
