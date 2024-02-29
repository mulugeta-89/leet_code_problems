# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(nums):
            n = len(nums)
            if n == 0:
                return None
            middle = n//2
            root = TreeNode(nums[middle])
            root.left = construct(nums[:middle])
            root.right = construct(nums[middle+1:])
            return root
        return construct(nums)