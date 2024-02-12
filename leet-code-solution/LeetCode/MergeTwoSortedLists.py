# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()
        current = start

        head1 = list1
        head2 = list2

        while head1 and head2:
            if head1.val <= head2.val:
                start.next = head1
                head1 = head1.next
            else:
                start.next = head2
                head2 = head2.next
            start = start.next
        if head1:
            start.next = head1
        if head2:
            start.next = head2
        return current.next