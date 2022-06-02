# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1.因為數字是reversed order，故從最小的數字（頭）開始加
        # 2.有可能不用進位，也有可能需要進位，最多進1位（最大的情況是9+9+1=19）
        # 3.每一位都要sum來紀錄總和、也需要一個carry紀錄是否進位(0或1)
        # e.g. sum = 2 + 5 + 0(上一位的carry) = 7 ; carry = 7 // 10 = 0
        # a // b, a % b = divmod(a, b)

        ans = cur = ListNode()
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next

            if l2:
                carry += l2.val
                l2 = l2.next

            carry, val = divmod(carry, 10)
            cur.next = ListNode(val)
            cur = cur.next

        return ans.next

