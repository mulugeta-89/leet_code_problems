# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        startNode = None
        lastNode = None
        i = 1
        while curr:
            if i > right:
                break
            if i < left:
                startNode = curr
            if i == right:
                lastNode = curr
            i += 1
            curr = curr.next
        lastNode.next = None
        if left == 1:
            lastNode = head
            head = reverse(head)
        else:
            lastNode = startNode.next
            startNode.next = reverse(startNode.next)
        lastNode.next = curr
        return head

        
        