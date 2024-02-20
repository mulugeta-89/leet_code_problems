class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "/" or token == "*" or token == "+" or token == "-":
                first = stack.pop()
                second = stack.pop()
                if token == "/":
                    sol = int(second / first)
                elif token == "+":
                    sol = first + second
                elif token == "-":
                    sol = second - first
                else:
                    sol = first * second
                stack.append(sol)
            else:
                stack.append(int(token))
        return stack[0]
        