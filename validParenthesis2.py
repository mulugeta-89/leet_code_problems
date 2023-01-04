def is_valid(letters):
    co_ordinates = {
        "(": ")",
        "{": "}",
        "[" : "]"
    }
    stack = []
    for item in letters:
        if item in co_ordinates:
            stack.append(item)
        else:
            if not stack:
                return False
            if item != co_ordinates[stack[-1]]:
                return False
            else:
                stack.pop()
    return not stack

print(is_valid("{}]"))