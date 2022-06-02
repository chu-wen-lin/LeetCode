# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #         # 如果只有一個list，就返回該list；如果兩個都是空的，就返回空的（前兩種可能都會直接跳到29行，dummy會接上其一或兩者皆為None，就維持著None

        #         #Time complexity: O(M+N)  M:len(l1) N:len(l2)
        #         #Space complexity: O(1) we do not create anything that will scale as our input gets arbitrarily.
        dummy = cur = ListNode(0)  # dummy & cur share same memory address

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next

            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        cur.next = l1 or l2  # 把剩下的node都接上去
        return dummy.next
