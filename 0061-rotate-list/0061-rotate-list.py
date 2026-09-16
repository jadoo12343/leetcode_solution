# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        n=1
        cur = head
        while cur.next:
            n+=1
            cur = cur.next
        
        k %= n
        if k == 0:
            return head
        cur.next = head
        steps = n - k - 1
        new_cur = head
        for _ in range(steps):
            new_cur = new_cur.next
        new_head = new_cur.next
        new_cur.next = None
        return new_head



        