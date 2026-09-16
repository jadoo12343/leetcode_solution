# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        cur = head

        dummy1 = ListNode(0)
        cur1 = dummy1

        dummy2 = ListNode(0)
        cur2 = dummy2

        while cur:
            if cur.val < x:
                cur1.next = cur
                cur1 = cur1.next
            else:
                cur2.next = cur
                cur2 = cur2.next

            cur = cur.next

        cur2.next = None
        cur1.next = dummy2.next

        return dummy1.next
