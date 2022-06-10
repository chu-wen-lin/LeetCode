# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return root

        # solution 1: recursive
        # time: O(N) space:O(N) 因為最差的情況skewed tree需要recurse到最底層才會return回來
        # res = []
        #
        # def dfs_preorder(node):
        #     if not node:
        #         return
        #
        #     else:
        #         res.append(node.val)
        #
        #         for child in node.children:
        #             dfs_preorder(child)
        #
        # dfs_preorder(root)
        #
        # return res

        # solution 2: iterative
        # time: O(N) space:O(N) 因為stack的最多（最差情況）存N-1個node，當樹的第二層全部都有葉子時
        res = []
        stack = [root]

        while stack:
            root = stack.pop()   # 最晚進去的node要先被走訪
            res.append(root.val)
            for node in root.children[::-1]:  # 因為我們希望等等node最左邊的小孩先被pop出來，所以小孩被加進stack的順序應該是由右（最後面）到左（最前面）
                stack.append(node)

        return res
