# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        else:
            while head.next and head.next.next:
                if head == head.next:
                    return True
                    break
                else:
                    head = head.next
                    head.next = head.next.next
        return False
            
         
        