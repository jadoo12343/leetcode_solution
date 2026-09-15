# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        head = None
        change = 0
        while l1 or l2:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0

            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0

            summ = val1 + val2 + change
            if not res:
                head = res = ListNode(summ % 10)
            else:
                res.next = ListNode(summ % 10)
                res = res.next
            
            change = summ // 10
        if change:
            res.next = ListNode(change)
        return head