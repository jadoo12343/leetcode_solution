# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        a = []
        while head :
            a.append(head.val)
            head = head.next
        num = str("".join(map(str, a)))
        decimal_num = int(num, 2)
        return decimal_num
            
        