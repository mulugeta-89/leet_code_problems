class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for item in s:
            if item == "(":
                stack.append(item)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(item)
        return len(stack)
        