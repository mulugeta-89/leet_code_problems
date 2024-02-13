# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller = ListNode("#")
        greater = ListNode("*")
        hsmaller = smaller
        hgreater = greater

        current = head
        while current:
            value = current.val
            if value < x:
                hsmaller.next = ListNode(value)
                hsmaller = hsmaller.next
            else:
                hgreater.next = ListNode(value)
                hgreater = hgreater.next
            current = current.next
        hsmaller.next = greater.next
        return smaller.next
            

        