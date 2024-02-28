# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def bfs(root):
            if not root:
                return []
            sol = []
            queue = [(0, root)]
            
            while queue:
                n = len(queue)
                current_level = []
                for _ in range(n):
                    left = queue.pop(0)
                    ind, node = left
                    current_level.append(ind)

                    if node.left:
                        queue.append((2*ind + 1,node.left))
                    if node.right:
                        queue.append((2*ind + 2,node.right))
                sol.append(current_level)
            return sol
        indices = bfs(root)
        maxi = 0
        for i in range(len(indices)-1, -1, -1):
            calc = indices[i][-1] - indices[i][0] + 1
            if calc > maxi:
                maxi = calc
        return maxi 
        