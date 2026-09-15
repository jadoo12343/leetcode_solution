# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = temp = head
        for i in range(n):
            res = res.next
            
        if not res:
            return head.next
            
        while res.next:
            res = res.next
            temp = temp.next
            
        temp.next = temp.next.next
        return head