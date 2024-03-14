# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def inorder(root):
            if root:
                inorder(root.left)
                arr.append(root.val)
                inorder(root.right)
        inorder(root)
        head = None
        def binaryTree(arr):
            if len(arr) == 0:
                return None
            mid = len(arr)//2
            head = TreeNode(arr[mid])
            head.left = binaryTree(arr[:mid])
            head.right = binaryTree(arr[mid+1:])
            return head
        return binaryTree(arr)



        