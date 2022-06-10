# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        # 此題需注意的點是：題目規定同層的node要裝在同個list，故需要level變數記當前node在哪一層

        # recursive
        # time: O(N) 因為每個點都剛好會被走訪一次
        # space:O(N) 因為最差的情況是skewed tree 走到最底層才會return回來
        #         ans = []

        #         def bfs(node, level, ans):
        #             if not node:
        #                 return

        #             if level > len(ans):
        #                 ans.append([node.val])
        #             else:
        #                 ans[level-1] += [node.val]

        #             bfs(node.left, level+1, ans)
        #             bfs(node.right, level+1, ans)

        #         bfs(root, 1, ans)

        #         return ans

        # iterative
        # time: O(N)
        # space: O(N)
        from collections import deque
        queue = deque([root])
        ans = []

        while queue:
            sub_ans = []
            # print(queue, len(queue))
            # 一定只有同一層的node會同時在queue裡，單次迴圈中就是要把所有同層的node都pop出來
            for _ in range(len(queue)):
                node = queue.popleft()
                sub_ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(sub_ans)
        return ans
