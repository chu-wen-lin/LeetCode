# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:  # Linked List為空或只有一個節點時，反轉的結果就是自己
            return head
        # solution 1: recursively
        # Time Complexity: O(N), Space Complexity: O(N) because of the call stack
        # 怎麼處理2：我們應該把2->3的箭頭砍掉、2改指到1(2->1)。對每一個節點來說都是做這兩個步驟！
        # res = self.reverseList(head.next)
        #
        # head.next.next = head
        # head.next = None
        #
        # return res

        # solution 2: iteratively
        # Time Complexity: O(N), Space Complexity: O(1) 因為只需要存pointer變數
        # 需要previous、current、next三個pointer
        prev = None
        cur = head
        next = None

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev





