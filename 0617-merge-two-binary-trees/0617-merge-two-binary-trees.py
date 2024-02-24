# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and root2:
            return root2
        if not root2 and root1:
            return root1
        def bfs(root1, root2):
            if not root1 and not root2:
                return
            if root1 and root2:
                root1.val = root1.val + root2.val
                bfs(root1.left, root2.left)
                bfs(root1.right, root2.right)
                if root2.left and not root1.left:
                    root1.left = root2.left
                if root2.right and not root1.right:
                    root1.right = root2.right
        bfs(root1, root2)
        return root1


        