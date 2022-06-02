# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # leaf nodes: 最下層(左右腳都是null)的nodes

        # solution 1: recursive
        # def traverse(root, leaves):
        #     if root:
        #         if not root.left and not root.right:
        #             leaves.append(root.val)
        #
        #         # 題目說leaf value sequence是由左到右，所以左腳要比右腳先遍歷
        #         traverse(root.left, leaves)
        #         traverse(root.right, leaves)
        #
        #         return leaves
        #
        # return traverse(root1, []) == traverse(root2, [])

        # solution 2: iterative
        def traverse(root, leaves):
            if root:
                stack = []
                stack.append(root)

                while stack:
                    current_node = stack.pop()
                    if not current_node.left and not current_node.right:
                        leaves.append(current_node.val)

                    if current_node.right:
                        stack.append(current_node.right)
                    if current_node.left:
                        stack.append(current_node.left)
                return leaves

        return traverse(root1, []) == traverse(root2, [])
