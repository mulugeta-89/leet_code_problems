# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        curr_next = curr.next
        while(curr_next):
            a = math.gcd(curr.val, curr_next.val)
            new_node = ListNode(a)
            curr.next = new_node
            new_node.next = curr_next
            curr = new_node.next
            curr_next = curr.next
        return head
        