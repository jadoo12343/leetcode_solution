# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        cur = head
        l1 = ListNode(0)
        l2 = ListNode(0)
        prev , temp = l1 , l2
        while cur :
            if cur.val < x :
                prev.next = cur
                prev = prev.next
            else:
                temp.next = cur
                temp = temp.next
            cur = cur.next
        temp.next = None
        prev.next = l2.next
        return l1.next
        