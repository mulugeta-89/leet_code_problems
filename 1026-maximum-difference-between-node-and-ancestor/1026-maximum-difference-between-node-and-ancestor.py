# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sol = -1
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def findDiff(root, current_max, current_min):
            if not root:
                return self.sol
            self.sol = max(self.sol,abs(root.val-current_max), abs(root.val-current_min))
            current_max = max(root.val, current_max)
            current_min = min(root.val, current_min)
            
            findDiff(root.left, current_max, current_min)
            findDiff(root.right, current_max, current_min)
        findDiff(root, root.val, root.val)
        return self.sol
        