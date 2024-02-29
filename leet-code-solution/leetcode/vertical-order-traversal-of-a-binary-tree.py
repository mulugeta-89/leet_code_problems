# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root):
            if not root:
                return []
            queue = [(0,0,root)]
            sol_arr = []

            while queue:
                n = len(queue)
                current_level = []

                for _ in range(n):
                    left = queue.pop(0)
                    a,b,node = left
                    current_level.append((a,b,node.val))

                    if node.left:
                        queue.append((a+1, b-1, node.left))
                    if node.right:
                        queue.append((a+1, b+1, node.right))
                for item in current_level:
                    sol_arr.append(item)
            return sol_arr
        dicti = defaultdict(list)
        sol_arr = []
        a = bfs(root)
        a.sort(key=lambda x: (x[1], x[0], x[2]))
        for item in a:
            k,f,c = item
            dicti[f].append(c)
        for item in dicti:
            sol_arr.append(dicti[item])
        return sol_arr
        
        
        
        