# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tail = ListNode((l1.val + l2.val)%10)
        head = tail
        remainder = (l1.val + l2.val)//10
        l1 = l1.next
        l2 = l2.next
        
        while l1 is not None and l2 is not None:
            sums = (l1.val + l2.val + remainder)
            tail.next = ListNode(sums%10)
            tail = tail.next
            remainder = sums//10
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            sums = l1.val + remainder
            tail.next = ListNode(sums%10)
            tail = tail.next
            remainder = sums//10
            l1 = l1.next
        while l2 is not None:
            sums = l2.val + remainder
            tail.next = ListNode(sums%10)
            tail = tail.next
            remainder = sums//10
            l2 = l2.next
        if remainder:
            tail.next = ListNode(remainder)
        return head        