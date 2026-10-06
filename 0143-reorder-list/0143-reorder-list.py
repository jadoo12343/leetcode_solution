# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow , fast = head , head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        temp = slow.next
        slow.next = None
        
        prev = None
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        temp = prev

        first = head
        while temp:
            temp1 = first.next
            temp2 = temp.next
            first.next = temp
            temp.next = temp1
            first = temp1
            temp = temp2