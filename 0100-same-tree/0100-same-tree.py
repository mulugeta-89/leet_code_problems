# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def bfs(root):
    if root is None:
        return
    visited = []
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        visited.append(node.val)
        if node.left:
            queue.append(node.left)
        else:
            visited.append(0)
        if node.right:
            queue.append(node.right)
        else:
            visited.append(1)
    return visited
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        a = bfs(p)
        b = bfs(q)
        return True if a==b else False
        