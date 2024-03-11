# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(nums):
            if nums == []:
                return None
            maxi = max(nums)
            ind = nums.index(maxi)
            root = TreeNode(maxi)
            root.left = construct(nums[:ind])
            root.right = construct(nums[ind+1:])
            return root
        return construct(nums)
        