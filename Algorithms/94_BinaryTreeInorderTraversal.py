# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:  # base case
            return root

        # recursive
        # 1. recur on left node(subtree)
        left = self.inorderTraversal(root.left)

        # 2. current node
        current = [root.val]

        # 3. recur on right node(subtree)
        right = self.inorderTraversal(root.right)

        return left + current + right

