# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # solution 1
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next  # skip duplicated node
            else:
                cur = cur.next  # not duplicate of current node, move to next node

        return head

        # solution 2
#         if not head:
#             return head

#         slow, fast = head, head

#         while fast:
#             if fast.val != slow.val:
#                 slow.next = fast
#                 slow = slow.next

#             fast = fast.next

#         slow.next = None   # 斷開與最後面重複元素的連結
#         return head
