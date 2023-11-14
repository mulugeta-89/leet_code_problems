# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def bfs(root):
    if root is None:
        return []
    queue = []
    visited = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        visited.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return visited
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        a = bfs(root1)
        b = bfs(root2)
        c = a+b
        c.sort()
        return c
        