# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101,head)
        prev , cur = dummy , head
        if not head :
            return head
        while cur :
            if cur.next is None or cur.val != cur.next.val:
                prev = cur
                cur = cur.next
            else:
                while cur.next and cur.val == cur.next.val :
                    cur = cur.next
                prev.next = cur.next
                cur = cur.next
        return dummy.next

