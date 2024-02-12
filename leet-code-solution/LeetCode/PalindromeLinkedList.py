# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        first = head
        arr = []
        while first:
            arr.append(first.val)
            first = first.next
        return arr == arr[::-1]