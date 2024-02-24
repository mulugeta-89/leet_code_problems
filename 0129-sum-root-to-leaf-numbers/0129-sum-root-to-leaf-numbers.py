# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr = []
        sol = ""
        def bfs(root,sol):
            if not root:
                return ""
            sol += str(root.val)
            if not root.left and not root.right:
                arr.append(sol)
            left = bfs(root.left,sol)
            right = bfs(root.right, sol)
        bfs(root,sol)
        sol = 0
        for item in arr:
            sol += int(item)
        return sol
        
        