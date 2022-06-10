class Solution:
    def climbStairs(self, n: int) -> int:
        # solution 1: 使用dictionary作為備忘錄作法
        # Time Complexity = 子問題個數*計算每個子問題的時間 = O(N) * O(1) = O(N)
        # 利用dictionary記住已經算過的。總共只需計算f(1)+f(2)+...+f(n)
        # Space Complexity: O(N)
        #         if n == 1 or n == 2:
        #             return n
        #         memo = {1:1, 2:2}

        #         def helper(n: int) -> int:
        #             if n in memo:
        #                 return memo[n]
        #             else:
        #                 memo[n] = helper(n-1) + helper(n-2)
        #                 return memo[n]

        #         return helper(n)

        # solution 2: 使用list作為備忘錄(記住每次運算的結果)的bottom-up做法
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        #         if n == 1 or n == 2:
        #             return n
        #         memo = [0] * (n+1)   #第0個位置空著不用
        #         memo[1], memo[2] = 1, 2 #base cases

        #         for i in range(3, n+1):
        #             memo[i] = memo[i-1] + memo[i-2]

        #         return memo[n]

        # solution 3: 不要把全部的子問題答案都記下來，而只需紀錄當下想求得的問題的前兩個子問題以降低空間複雜度
        # Time Complexity依然是O(N)，但Space complexity由O(N)降至O(1)

        if n == 1 or n == 2:
            return n

        memo_i_2, memo_i_1 = 1, 2
        for i in range(3, n + 1):
            memo_i = memo_i_1 + memo_i_2
            memo_i_1, memo_i_2 = memo_i, memo_i_1  # 迭代更新前兩個子問題的解
        return memo_i
