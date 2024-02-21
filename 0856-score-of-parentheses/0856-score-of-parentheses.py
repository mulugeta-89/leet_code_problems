class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        sol = 0
        for item in s:
            if item == "(":
                stack.append(item)
            else:
                if stack[-1] == "(":
                    stack.pop()
                    stack.append("1")
                else:
                    count = 0
                    while stack[-1] != "(":
                        count += int(stack[-1])
                        stack.pop()
                    stack.pop()
                    stack.append(str(2*count))
        while len(stack) > 0:
            sol += int(stack[-1])
            stack.pop()
        return sol
        