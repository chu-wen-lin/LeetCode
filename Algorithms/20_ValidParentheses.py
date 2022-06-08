class Solution:
    def isValid(self, s: str) -> bool:
        # 每一個'('要有一個')' 另外兩種括號也是
        # 遇到左括號時，存入stack；遇到右括號時若stack為空則不valid、不為空則pop stack並檢查有沒有match
        # 若都走完一遍stack還不為空（有未被配對的左括號），則return False

        # "[()]": True
        # "[(])" : False
        # "{[([{}])]}[]": True
        # "((": False
        # "){": False
        # ")(": False
        # ")(){}": False

        # Time Complexity: O(N) 遍歷整個s
        # Space Complexity: O(N) worst case: s要走到正中間(N/2)才開始有配對

        n = len(s)
        if n == 1 or n % 2:  # s長度只有1或只有奇數個括號
            return False

        d = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for ele in s:
            # 當前元素是左括號
            if ele in d:  # 不要用 in d.keys() -> O(N)
                stack.append(ele)

            # 當前元素是右括號
            elif not stack or d[stack.pop()] != ele:  # 如果第一個元素是右括號，一定不valid，此時stack為空，return False
                return False

        # if stack is empty: return True
        # if stack is not empty(有未被配對的左括號): return False
        return not stack
