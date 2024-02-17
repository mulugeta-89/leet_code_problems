# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        container = []
        while pointer:
            container.append([pointer.val, pointer])
            pointer = pointer.next
        container.sort(key=lambda x: x[0])
        for item in container:
            item[1].next = None
        other_pointer = container[0][1]
        for i in range(1, len(container)):
            container[i-1][1].next = container[i][1]
        return other_pointer
        