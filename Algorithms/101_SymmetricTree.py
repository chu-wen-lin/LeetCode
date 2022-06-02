# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 想法：一層一層檢查，level-order traversal
        # 1. queue = List[tuple] 存對稱位置需要比較的兩兩節點。越上層的組越早存進去越早出來比
        #    e.g. 第三層：左腳的左腳 == 右腳的右腳、左腳的右腳 == 右腳的左腳
        # 2. break point:比的過程發現某一組不對稱就return False 或 一直比較直到queue為空就return True
        # 3. tuple裡的兩個元素比較過程的條件判斷：
        #    (1)僅其一是null -> non-symmetric，return False
        #    (2)都不是null，但元素不相同 -> non-symmetric，return False
        #    (3)都不是null，且元素相同 -> 這組過關，但還需繼續比較，continue、把各自的子孫再存進去queue
        #    (4)都是null -> 這組過關，但還需繼續比較，continue

        if not root:
            return True

        # 從第二層開始比
        queue = [(root.left, root.right)]

        while queue:
            left, right = queue.pop(0)  # first-in-first-out

            if not left and not right:
                continue

            elif (left and right) and left.val != right.val:
                return False

            elif not left or not right:
                return False

            else:  # (left and right) and left.val == right.val

                # 把各自的子孫存進去queue，晚點比較
                queue.append((left.left, right.right))
                queue.append((left.right, right.left))

        return True
