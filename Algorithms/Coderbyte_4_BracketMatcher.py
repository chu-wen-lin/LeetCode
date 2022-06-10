# Check if the brackets in a string are correctly matched up.
def BracketMatcher(strParam: str):
    # Time Complexity: O(N)  cause we iterate strParam exactly once
    # Space Complexity: O(N) worst case: strParam only contains left bracket, then the len(stack) equals to len(strParam)
    # "(((((("
    stack = []

    for ele in strParam:     # 除了括弧以外的字串都不需處理，continue就好
        # 當前元素是左括號
        if ele == "(":
            stack.append(ele)

        elif ele == ")":  # 當前元素是右括號
            # if not stack:
            #     return 0
            # else:
            #     stack.pop()  # 不用檢查pop出來的是不是左括號，一定是！

            # 這邊也可以改成用try-except寫
            try:
                stack.pop()
            except IndexError:  # pop from empty list
                return 0

    return 0 if stack else 1  # stack不為空，表示有左括號沒有被配對到


# keep this function call here
print(BracketMatcher("(c(oder)) b(yte)"))
