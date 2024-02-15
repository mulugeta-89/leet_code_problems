# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        found_cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                found_cycle = True
                fast = head
                break
        if not found_cycle:
            return None
        while fast is not slow:
            slow = slow.next
            fast = fast.next
        return slow

        