# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def getSize(head):
    length = 0
    while head:
        head = head.next
        length += 1
    return length

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = getSize(head)
        sol_arr = []
        arr = []
        min_item = length//k
        extra_ones = length%k
        for i in range(k):
            arr.append(min_item)
        for i in range(extra_ones):
            arr[i] += 1
        next_one = None
        for i in range(len(arr)):
            pointer = head
            if pointer:
                for j in range(arr[i]-1):
                    pointer = pointer.next
                next_one = pointer.next
                pointer.next = None
                sol_arr.append(head)
                head = next_one
            else:
                sol_arr.append(None)
        return sol_arr


        