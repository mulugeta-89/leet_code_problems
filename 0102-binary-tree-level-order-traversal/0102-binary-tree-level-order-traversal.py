# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        queue = []
        small = []
        big = []
        queue.append(root)
        big.insert(0, [root.val])
        while queue:
            intermidiate = []
            for node in queue:
                if node.left:
                    small.append(node.left.val)
                    intermidiate.append(node.left)
                if node.right:
                    small.append(node.right.val)
                    intermidiate.append(node.right)
            if intermidiate:
                queue = intermidiate.copy()
                big.append(small)
            else:
                break
            small = []

        return big
        