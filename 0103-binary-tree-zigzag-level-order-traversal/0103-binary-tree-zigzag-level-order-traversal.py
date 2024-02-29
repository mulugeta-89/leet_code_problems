# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root):
            if not root:
                return []
            sol = []
            count = 0
            queue = [root]

            while queue:
                n = len(queue)
                count += 1
                current_level = []
                for _ in range(n):
                    node = queue.pop(0)
                    current_level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                if count%2 == 0:
                    current_level.reverse()
                sol.append(current_level)
            return sol
        arr = bfs(root)
        return arr
        

        