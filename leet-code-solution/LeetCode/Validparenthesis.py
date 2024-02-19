class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dicti = {"(":")", "{":"}", "[":"]"}
        for item in s:
            if item == "(" or item == "[" or item == "{":
                stack.append(item)
            else:
                if stack:
                    if item != dicti[stack[-1]]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        return not stack