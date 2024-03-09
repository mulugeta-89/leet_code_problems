# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dicti = defaultdict(int)
        def inorder(root):
            if root:
                inorder(root.left)
                dicti[root.val] += 1
                inorder(root.right)
        inorder(root)
        maxi = max(dicti.values())
        sol_arr = []
        for k in dicti:
            if dicti[k] == maxi:
                sol_arr.append(k)
        return sol_arr
                
        