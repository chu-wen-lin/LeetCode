# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 三種方法的time complexity都是O(N)，N是node數量。第一和三種方法的space complexity是O(N)；第二種是O(1)：只需紀錄slow和fast
        # solution1 : output to array
        # array = [head]
        # while array[-1].next:
        #     array.append(array[-1].next)
        # return array[len(array) // 2]

        # solution 2: two pointers - fast and slow。slow一次走一步、fast一次走兩步，當fast走到底時，slow必會在中間
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next  # 在倒數第二個時，fast會被更新為none，便跳出迴圈

        return slow

        # solution 3: dictionary(nodes[depth] = head)
#         depth = 1
#         nodes = {}

#         while head:
#             nodes[depth] = head
#             head = head.next
#             depth += 1
#         return nodes[(depth + 1)// 2]


