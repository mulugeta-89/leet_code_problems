# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def valid(root):
            if root:
                valid(root.left)
                arr.append(root.val)
                valid(root.right)
        valid(root)
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                return False
        return True
        

        