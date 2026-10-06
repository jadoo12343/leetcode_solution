# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        
        res = []
        while head:
            res.append(head.val)
            head = head.next
        
        res.sort()
    
        sol = ListNode(res[0])
        current = sol
    
        for value in res[1:]:
            current.next = ListNode(value)
            current = current.next
        
        return sol

