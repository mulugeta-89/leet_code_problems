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
            sol = 0
            queue = deque([(0, root)])
            left_most = queue[0][0]
            right_most = -float("inf")
            
            while queue:
                n = len(queue)
                left_most = queue[0][0]
                current_level = []
                for _ in range(n):
                    left = queue.popleft()
                    ind, node = left
                    right_most = max(right_most, ind)

                    if node.left:
                        queue.append((2*ind + 1,node.left))
                    if node.right:
                        queue.append((2*ind + 2,node.right))
                sol = max(sol, right_most-left_most+1)
            return sol
        return bfs(root)