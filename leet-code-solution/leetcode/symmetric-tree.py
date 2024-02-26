# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def finder(root1, root2):
            if not root1 and not root2:
                return True
            if not (root1 and root2):
                return False
            sol = root1.val == root2.val
            left = finder(root1.left, root2.right)
            right = finder(root1.right, root2.left)
            return sol and left and right
        return finder(root.left, root.right)


        