# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dicti = {}
        for i, v in enumerate(inorder):
            dicti[v] = i
        def builder(low, high):
            if low > high:
                return
            root = TreeNode(postorder.pop())
            mid = dicti[root.val]
            root.right = builder(mid+1, high)
            root.left = builder(low, mid-1)
            return root
        return builder(0, len(inorder)-1)
        