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
        res = []
        stack = [root]

        while stack:
            root = stack.pop()
            res.append(root.val)
            for node in root.children[::-1]:
                stack.append(node)

        return res
