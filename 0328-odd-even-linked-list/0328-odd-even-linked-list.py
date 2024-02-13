# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        start = head
        start2 = head.next
        heade = head.next

        while start2 and start2.next:
            start.next = start.next.next
            start2.next = start2.next.next
            start = start.next
            start2 = start2.next

        start.next = heade
        return head



    
        