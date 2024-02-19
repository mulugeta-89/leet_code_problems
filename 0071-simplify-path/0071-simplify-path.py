class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for item in path:
            if stack and item == "..":
                stack.pop()
            else:
                count_dot = 0
                for i in item:
                    if i == ".":
                        count_dot += 1
                str_out = "".join(x for x in item if x != "." and x != "_")
                if len(str_out)>0 or count_dot >=3:
                    stack.append(item)
        sol = "/" if not stack else ""
        for item in stack:
            sol = sol + "/" + item
        return sol
        