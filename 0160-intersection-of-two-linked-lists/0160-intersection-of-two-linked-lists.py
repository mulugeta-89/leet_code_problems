# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        container = set()
        first = headA
        second = headB
        while first:
            container.add(first)
            first = first.next
        while second:
            if second in container:
                return second
            second = second.next
        