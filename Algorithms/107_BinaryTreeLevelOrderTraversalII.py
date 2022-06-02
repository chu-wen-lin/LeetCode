# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:  # if root is an empty list, return itself
            return root

        queue = []  # store the nodes to go through in the next round
        res = []
        queue.append(root)

        while queue:
            same_level_nodes = []
            for _ in range(len(queue)):
                current_node = queue.pop(0)
                same_level_nodes.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            res.append(same_level_nodes)

        res.reverse()
        return res
