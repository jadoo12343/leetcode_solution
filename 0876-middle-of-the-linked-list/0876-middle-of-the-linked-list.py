# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start=end=head
        while end is not None and end.next is not None:
            end=end.next.next
            start=start.next
        return start

        